from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import functools
from tensorflow.python.distribute import distribution_strategy_context as ds_context
from tensorflow.python.eager import context
from tensorflow.python.framework import ops
from tensorflow.python.framework import tensor_shape
from tensorflow.python.keras import activations
from tensorflow.python.keras import backend as K
from tensorflow.python.keras import constraints
from tensorflow.python.keras import initializers
from tensorflow.python.keras import regularizers
from tensorflow.python.keras.engine.base_layer import Layer
from tensorflow.python.keras.engine.input_spec import InputSpec
from tensorflow.python.keras.saving.saved_model import layer_serialization
from tensorflow.python.keras.utils import generic_utils
from tensorflow.python.keras.utils import tf_utils
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import control_flow_util
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import state_ops
from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.training.tracking import base as trackable
from tensorflow.python.training.tracking import data_structures
from tensorflow.python.util import nest
from tensorflow.python.util.compat import collections_abc
from tensorflow.python.util.tf_export import keras_export
from tensorflow.tools.docs import doc_controls
from tensorflow.python.keras.utils import conv_utils
from tensorflow.python.ops import nn


RECURRENT_DROPOUT_WARNING_MSG = (
    'RNN `implementation=2` is not supported when `recurrent_dropout` is set. '
    'Using `implementation=1`.')


@keras_export('keras.layers.StackedRNNCells')
class StackedRNNCells(Layer):

  def __init__(self, cells, **kwargs):
    for cell in cells:
      if not 'call' in dir(cell):
        raise ValueError('All cells must have a `call` method. '
                         'received cells:', cells)
      if not 'state_size' in dir(cell):
        raise ValueError('All cells must have a '
                         '`state_size` attribute. '
                         'received cells:', cells)
    self.cells = cells
    # reverse_state_order determines whether the state size will be in a reverse
    # order of the cells' state. User might want to set this to True to keep the
    # existing behavior. This is only useful when use RNN(return_state=True)
    # since the state will be returned as the same order of state_size.
    self.reverse_state_order = kwargs.pop('reverse_state_order', False)
    if self.reverse_state_order:
      logging.warning('reverse_state_order=True in StackedRNNCells will soon '
                      'be deprecated. Please update the code to work with the '
                      'natural order of states if you rely on the RNN states, '
                      'eg RNN(return_state=True).')
    super(StackedRNNCells, self).__init__(**kwargs)

  @property
  def state_size(self):
    return tuple(c.state_size for c in
                 (self.cells[::-1] if self.reverse_state_order else self.cells))

  @property
  def output_size(self):
    if getattr(self.cells[-1], 'output_size', None) is not None:
      return self.cells[-1].output_size
    elif _is_multiple_state(self.cells[-1].state_size):
      return self.cells[-1].state_size[0]
    else:
      return self.cells[-1].state_size

  def get_initial_state(self, inputs=None, batch_size=None, dtype=None):
    initial_states = []
    for cell in self.cells[::-1] if self.reverse_state_order else self.cells:
      get_initial_state_fn = getattr(cell, 'get_initial_state', None)
      if get_initial_state_fn:
        initial_states.append(get_initial_state_fn(
            inputs=inputs, batch_size=batch_size, dtype=dtype))
      else:
        initial_states.append(_generate_zero_filled_state_for_cell(
            cell, inputs, batch_size, dtype))

    return tuple(initial_states)

  def call(self, inputs, states, constants=None, training=None, **kwargs):
    # Recover per-cell states.
    state_size = (self.state_size[::-1]
                  if self.reverse_state_order else self.state_size)
    nested_states = nest.pack_sequence_as(state_size, nest.flatten(states))

    # Call the cells in order and store the returned states.
    new_nested_states = []
    for cell, states in zip(self.cells, nested_states):
      states = states if nest.is_sequence(states) else [states]
      # TF cell does not wrap the state into list when there is only one state.
      is_tf_rnn_cell = getattr(cell, '_is_tf_rnn_cell', None) is not None
      states = states[0] if len(states) == 1 and is_tf_rnn_cell else states
      if generic_utils.has_arg(cell.call, 'training'):
        kwargs['training'] = training
      else:
        kwargs.pop('training', None)
      # Use the __call__ function for callable objects, eg layers, so that it
      # will have the proper name scopes for the ops, etc.
      cell_call_fn = cell.__call__ if callable(cell) else cell.call
      if generic_utils.has_arg(cell.call, 'constants'):
        inputs, states = cell_call_fn(inputs, states,
                                      constants=constants, **kwargs)
      else:
        inputs, states = cell_call_fn(inputs, states, **kwargs)
      new_nested_states.append(states)

    return inputs, nest.pack_sequence_as(state_size,
                                         nest.flatten(new_nested_states))

  @tf_utils.shape_type_conversion
  def build(self, input_shape):
    if isinstance(input_shape, list):
      input_shape = input_shape[0]
    for cell in self.cells:
      if isinstance(cell, Layer) and not cell.built:
        with K.name_scope(cell.name):
          cell.build(input_shape)
          cell.built = True
      if getattr(cell, 'output_size', None) is not None:
        output_dim = cell.output_size
      elif _is_multiple_state(cell.state_size):
        output_dim = cell.state_size[0]
      else:
        output_dim = cell.state_size
      input_shape = tuple([input_shape[0]] +
                          tensor_shape.as_shape(output_dim).as_list())
    self.built = True

  def get_config(self):
    cells = []
    for cell in self.cells:
      cells.append({
          'class_name': cell.__class__.__name__,
          'config': cell.get_config()
      })
    config = {'cells': cells}
    base_config = super(StackedRNNCells, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))

  @classmethod
  def from_config(cls, config, custom_objects=None):
    from tensorflow.python.keras.layers import deserialize as deserialize_layer  # pylint: disable=g-import-not-at-top
    cells = []
    for cell_config in config.pop('cells'):
      cells.append(
          deserialize_layer(cell_config, custom_objects=custom_objects))
    return cls(cells, **config)


@keras_export('keras.layers.RNN')
class RNN(Layer):  
  def __init__(self,
               cell,
               return_sequences=False,
               return_state=False,
               go_backwards=False,
               stateful=False,
               unroll=False,
               time_major=False,
               **kwargs):
    if isinstance(cell, (list, tuple)):
      cell = StackedRNNCells(cell)
    if not 'call' in dir(cell):
      raise ValueError('`cell` should have a `call` method. '
                       'The RNN was passed:', cell)
    if not 'state_size' in dir(cell):
      raise ValueError('The RNN cell should have '
                       'an attribute `state_size` '
                       '(tuple of integers, '
                       'one integer per RNN state).')
    # If True, the output for masked timestep will be zeros, whereas in the
    # False case, output from previous timestep is returned for masked timestep.
    self.zero_output_for_mask = kwargs.pop('zero_output_for_mask', False)

    if 'input_shape' not in kwargs and (
        'input_dim' in kwargs or 'input_length' in kwargs):
      input_shape = (kwargs.pop('input_length', None),
                     kwargs.pop('input_dim', None))
      kwargs['input_shape'] = input_shape

    super(RNN, self).__init__(**kwargs)
    self.cell = cell
    self.return_sequences = return_sequences
    self.return_state = return_state
    self.go_backwards = go_backwards
    self.stateful = stateful
    self.unroll = unroll
    self.time_major = time_major

    self.supports_masking = True
    # The input shape is unknown yet, it could have nested tensor inputs, and
    # the input spec will be the list of specs for nested inputs, the structure
    # of the input_spec will be the same as the input.
    self.input_spec = None
    self.state_spec = None
    self._states = None
    self.constants_spec = None
    self._num_constants = 0

    if stateful:
      if ds_context.has_strategy():
        raise ValueError('RNNs with stateful=True not yet supported with '
                         'tf.distribute.Strategy.')

  @property
  def states(self):
    if self._states is None:
      state = nest.map_structure(lambda _: None, self.cell.state_size)
      return state if nest.is_sequence(self.cell.state_size) else [state]
    return self._states

  @states.setter
  # Automatic tracking catches "self._states" which adds an extra weight and
  # breaks HDF5 checkpoints.
  @trackable.no_automatic_dependency_tracking
  def states(self, states):
    self._states = states

  def compute_output_shape(self, input_shape):
    if isinstance(input_shape, list):
      input_shape = input_shape[0]
    # Check whether the input shape contains any nested shapes. It could be
    # (tensor_shape(1, 2), tensor_shape(3, 4)) or (1, 2, 3) which is from numpy
    # inputs.
    try:
      input_shape = tensor_shape.as_shape(input_shape)
    except (ValueError, TypeError):
      # A nested tensor input
      input_shape = nest.flatten(input_shape)[0]

    batch = input_shape[0]
    time_step = input_shape[1]
    if self.time_major:
      batch, time_step = time_step, batch

    if _is_multiple_state(self.cell.state_size):
      state_size = self.cell.state_size
    else:
      state_size = [self.cell.state_size]

    def _get_output_shape(flat_output_size):
      output_dim = tensor_shape.as_shape(flat_output_size).as_list()
      if self.return_sequences:
        if self.time_major:
          output_shape = tensor_shape.as_shape([time_step, batch] + output_dim)
        else:
          output_shape = tensor_shape.as_shape([batch, time_step] + output_dim)
      else:
        output_shape = tensor_shape.as_shape([batch] + output_dim)
      return output_shape

    if getattr(self.cell, 'output_size', None) is not None:
      # cell.output_size could be nested structure.
      output_shape = nest.flatten(nest.map_structure(
          _get_output_shape, self.cell.output_size))
      output_shape = output_shape[0] if len(output_shape) == 1 else output_shape
    else:
      # Note that state_size[0] could be a tensor_shape or int.
      output_shape = _get_output_shape(state_size[0])

    if self.return_state:
      def _get_state_shape(flat_state):
        state_shape = [batch] + tensor_shape.as_shape(flat_state).as_list()
        return tensor_shape.as_shape(state_shape)
      state_shape = nest.map_structure(_get_state_shape, state_size)
      return generic_utils.to_list(output_shape) + nest.flatten(state_shape)
    else:
      return output_shape

  def compute_mask(self, inputs, mask):
    # Time step masks must be the same for each input.
    # This is because the mask for an RNN is of size [batch, time_steps, 1],
    # and specifies which time steps should be skipped, and a time step
    # must be skipped for all inputs.
    # TODO(scottzhu): Should we accept multiple different masks?
    mask = nest.flatten(mask)[0]
    output_mask = mask if self.return_sequences else None
    if self.return_state:
      state_mask = [None for _ in self.states]
      return [output_mask] + state_mask
    else:
      return output_mask

  def build(self, input_shape):
    if isinstance(input_shape, list):
      input_shape = input_shape[0]
      # The input_shape here could be a nest structure.

    # do the tensor_shape to shapes here. The input could be single tensor, or a
    # nested structure of tensors.
    def get_input_spec(shape):
      """Convert input shape to InputSpec."""
      if isinstance(shape, tensor_shape.TensorShape):
        input_spec_shape = shape.as_list()
      else:
        input_spec_shape = list(shape)
      batch_index, time_step_index = (1, 0) if self.time_major else (0, 1)
      if not self.stateful:
        input_spec_shape[batch_index] = None
      input_spec_shape[time_step_index] = None
      return InputSpec(shape=tuple(input_spec_shape))

    def get_step_input_shape(shape):
      if isinstance(shape, tensor_shape.TensorShape):
        shape = tuple(shape.as_list())
      # remove the timestep from the input_shape
      return shape[1:] if self.time_major else (shape[0],) + shape[2:]

    # Check whether the input shape contains any nested shapes. It could be
    # (tensor_shape(1, 2), tensor_shape(3, 4)) or (1, 2, 3) which is from numpy
    # inputs.
    try:
      input_shape = tensor_shape.as_shape(input_shape)
    except (ValueError, TypeError):
      # A nested tensor input
      pass

    if not nest.is_sequence(input_shape):
      # This indicates the there is only one input.
      if self.input_spec is not None:
        self.input_spec[0] = get_input_spec(input_shape)
      else:
        self.input_spec = [get_input_spec(input_shape)]
      step_input_shape = get_step_input_shape(input_shape)
    else:
      if self.input_spec is not None:
        self.input_spec[0] = nest.map_structure(get_input_spec, input_shape)
      else:
        self.input_spec = generic_utils.to_list(
            nest.map_structure(get_input_spec, input_shape))
      step_input_shape = nest.map_structure(get_step_input_shape, input_shape)

    # allow cell (if layer) to build before we set or validate state_spec.
    if isinstance(self.cell, Layer) and not self.cell.built:
      with K.name_scope(self.cell.name):
        self.cell.build(step_input_shape)
        self.cell.built = True

    # set or validate state_spec
    if _is_multiple_state(self.cell.state_size):
      state_size = list(self.cell.state_size)
    else:
      state_size = [self.cell.state_size]

    if self.state_spec is not None:
      # initial_state was passed in call, check compatibility
      self._validate_state_spec(state_size, self.state_spec)
    else:
      self.state_spec = [
          InputSpec(shape=[None] + tensor_shape.as_shape(dim).as_list())
          for dim in state_size
      ]
    if self.stateful:
      self.reset_states()
    self.built = True

  @staticmethod
  def _validate_state_spec(cell_state_sizes, init_state_specs):
    """Validate the state spec between the initial_state and the state_size.

    Args:
      cell_state_sizes: list, the `state_size` attribute from the cell.
      init_state_specs: list, the `state_spec` from the initial_state that is
        passed in `call()`.

    Raises:
      ValueError: When initial state spec is not compatible with the state size.
    """
    validation_error = ValueError(
        'An `initial_state` was passed that is not compatible with '
        '`cell.state_size`. Received `state_spec`={}; '
        'however `cell.state_size` is '
        '{}'.format(init_state_specs, cell_state_sizes))
    flat_cell_state_sizes = nest.flatten(cell_state_sizes)
    flat_state_specs = nest.flatten(init_state_specs)

    if len(flat_cell_state_sizes) != len(flat_state_specs):
      raise validation_error
    for cell_state_spec, cell_state_size in zip(flat_state_specs,
                                                flat_cell_state_sizes):
      if not tensor_shape.TensorShape(
          # Ignore the first axis for init_state which is for batch
          cell_state_spec.shape[1:]).is_compatible_with(
              tensor_shape.TensorShape(cell_state_size)):
        raise validation_error

  @doc_controls.do_not_doc_inheritable
  def get_initial_state(self, inputs):
    get_initial_state_fn = getattr(self.cell, 'get_initial_state', None)

    if nest.is_sequence(inputs):
      # The input are nested sequences. Use the first element in the seq to get
      # batch size and dtype.
      inputs = nest.flatten(inputs)[0]

    input_shape = array_ops.shape(inputs)
    batch_size = input_shape[1] if self.time_major else input_shape[0]
    dtype = inputs.dtype
    if get_initial_state_fn:
      init_state = get_initial_state_fn(
          inputs=None, batch_size=batch_size, dtype=dtype)
    else:
      init_state = _generate_zero_filled_state(batch_size, self.cell.state_size,
                                               dtype)
    # Keras RNN expect the states in a list, even if it's a single state tensor.
    if not nest.is_sequence(init_state):
      init_state = [init_state]
    # Force the state to be a list in case it is a namedtuple eg LSTMStateTuple.
    return list(init_state)

  def __call__(self, inputs, initial_state=None, constants=None, **kwargs):
    inputs, initial_state, constants = _standardize_args(inputs,
                                                         initial_state,
                                                         constants,
                                                         self._num_constants)

    if initial_state is None and constants is None:
      return super(RNN, self).__call__(inputs, **kwargs)

    # If any of `initial_state` or `constants` are specified and are Keras
    # tensors, then add them to the inputs and temporarily modify the
    # input_spec to include them.

    additional_inputs = []
    additional_specs = []
    if initial_state is not None:
      additional_inputs += initial_state
      self.state_spec = nest.map_structure(
          lambda s: InputSpec(shape=K.int_shape(s)), initial_state)
      additional_specs += self.state_spec
    if constants is not None:
      additional_inputs += constants
      self.constants_spec = [
          InputSpec(shape=K.int_shape(constant)) for constant in constants
      ]
      self._num_constants = len(constants)
      additional_specs += self.constants_spec
    # additional_inputs can be empty if initial_state or constants are provided
    # but empty (e.g. the cell is stateless).
    flat_additional_inputs = nest.flatten(additional_inputs)
    is_keras_tensor = K.is_keras_tensor(
        flat_additional_inputs[0]) if flat_additional_inputs else True
    for tensor in flat_additional_inputs:
      if K.is_keras_tensor(tensor) != is_keras_tensor:
        raise ValueError('The initial state or constants of an RNN'
                         ' layer cannot be specified with a mix of'
                         ' Keras tensors and non-Keras tensors'
                         ' (a "Keras tensor" is a tensor that was'
                         ' returned by a Keras layer, or by `Input`)')

    if is_keras_tensor:
      # Compute the full input spec, including state and constants
      full_input = [inputs] + additional_inputs
      if self.built:
        # Keep the input_spec since it has been populated in build() method.
        full_input_spec = self.input_spec + additional_specs
      else:
        # The original input_spec is None since there could be a nested tensor
        # input. Update the input_spec to match the inputs.
        full_input_spec = generic_utils.to_list(
            nest.map_structure(lambda _: None, inputs)) + additional_specs
      # Perform the call with temporarily replaced input_spec
      self.input_spec = full_input_spec
      output = super(RNN, self).__call__(full_input, **kwargs)
      # Remove the additional_specs from input spec and keep the rest. It is
      # important to keep since the input spec was populated by build(), and
      # will be reused in the stateful=True.
      self.input_spec = self.input_spec[:-len(additional_specs)]
      return output
    else:
      if initial_state is not None:
        kwargs['initial_state'] = initial_state
      if constants is not None:
        kwargs['constants'] = constants
      return super(RNN, self).__call__(inputs, **kwargs)

  def call(self,
           inputs,
           mask=None,
           training=None,
           initial_state=None,
           constants=None):
    # The input should be dense, padded with zeros. If a ragged input is fed
    # into the layer, it is padded and the row lengths are used for masking.
    inputs, row_lengths = K.convert_inputs_if_ragged(inputs)
    is_ragged_input = (row_lengths is not None)
    self._validate_args_if_ragged(is_ragged_input, mask)

    inputs, initial_state, constants = self._process_inputs(
        inputs, initial_state, constants)

    self._maybe_reset_cell_dropout_mask(self.cell)
    if isinstance(self.cell, StackedRNNCells):
      for cell in self.cell.cells:
        self._maybe_reset_cell_dropout_mask(cell)

    if mask is not None:
      # Time step masks must be the same for each input.
      # TODO(scottzhu): Should we accept multiple different masks?
      mask = nest.flatten(mask)[0]

    if nest.is_sequence(inputs):
      # In the case of nested input, use the first element for shape check.
      input_shape = K.int_shape(nest.flatten(inputs)[0])
    else:
      input_shape = K.int_shape(inputs)
    timesteps = input_shape[0] if self.time_major else input_shape[1]
    if self.unroll and timesteps is None:
      raise ValueError('Cannot unroll a RNN if the '
                       'time dimension is undefined. \n'
                       '- If using a Sequential model, '
                       'specify the time dimension by passing '
                       'an `input_shape` or `batch_input_shape` '
                       'argument to your first layer. If your '
                       'first layer is an Embedding, you can '
                       'also use the `input_length` argument.\n'
                       '- If using the functional API, specify '
                       'the time dimension by passing a `shape` '
                       'or `batch_shape` argument to your Input layer.')

    kwargs = {}
    if generic_utils.has_arg(self.cell.call, 'training'):
      kwargs['training'] = training

    # TF RNN cells expect single tensor as state instead of list wrapped tensor.
    is_tf_rnn_cell = getattr(self.cell, '_is_tf_rnn_cell', None) is not None
    # Use the __call__ function for callable objects, eg layers, so that it
    # will have the proper name scopes for the ops, etc.
    cell_call_fn = self.cell.__call__ if callable(self.cell) else self.cell.call
    if constants:
      if not generic_utils.has_arg(self.cell.call, 'constants'):
        raise ValueError('RNN cell does not support constants')

      def step(inputs, states):
        constants = states[-self._num_constants:]  # pylint: disable=invalid-unary-operand-type
        states = states[:-self._num_constants]  # pylint: disable=invalid-unary-operand-type

        states = states[0] if len(states) == 1 and is_tf_rnn_cell else states
        output, new_states = cell_call_fn(
            inputs, states, constants=constants, **kwargs)
        if not nest.is_sequence(new_states):
          new_states = [new_states]
        return output, new_states
    else:

      def step(inputs, states):
        states = states[0] if len(states) == 1 and is_tf_rnn_cell else states
        output, new_states = cell_call_fn(inputs, states, **kwargs)
        if not nest.is_sequence(new_states):
          new_states = [new_states]
        return output, new_states
    last_output, outputs, states = K.rnn(
        step,
        inputs,
        initial_state,
        constants=constants,
        go_backwards=self.go_backwards,
        mask=mask,
        unroll=self.unroll,
        input_length=row_lengths if row_lengths is not None else timesteps,
        time_major=self.time_major,
        zero_output_for_mask=self.zero_output_for_mask)

    if self.stateful:
      updates = [
          state_ops.assign(self_state, state) for self_state, state in zip(
              nest.flatten(self.states), nest.flatten(states))
      ]
      self.add_update(updates)

    if self.return_sequences:
      output = K.maybe_convert_to_ragged(is_ragged_input, outputs, row_lengths)
    else:
      output = last_output

    if self.return_state:
      if not isinstance(states, (list, tuple)):
        states = [states]
      else:
        states = list(states)
      return generic_utils.to_list(output) + states
    else:
      return output

  def _process_inputs(self, inputs, initial_state, constants):
    # input shape: `(samples, time (padded with zeros), input_dim)`
    # note that the .build() method of subclasses MUST define
    # self.input_spec and self.state_spec with complete input shapes.
    if (isinstance(inputs, collections_abc.Sequence)
        and not isinstance(inputs, tuple)):
      # get initial_state from full input spec
      # as they could be copied to multiple GPU.
      if not self._num_constants:
        initial_state = inputs[1:]
      else:
        initial_state = inputs[1:-self._num_constants]
        constants = inputs[-self._num_constants:]
      if len(initial_state) == 0:
        initial_state = None
      inputs = inputs[0]

    if self.stateful:
      if initial_state is not None:
        # When layer is stateful and initial_state is provided, check if the
        # recorded state is same as the default value (zeros). Use the recorded
        # state if it is not same as the default.
        non_zero_count = math_ops.add_n([math_ops.count_nonzero_v2(s)
                                         for s in nest.flatten(self.states)])
        # Set strict = True to keep the original structure of the state.
        initial_state = control_flow_ops.cond(non_zero_count > 0,
                                              true_fn=lambda: self.states,
                                              false_fn=lambda: initial_state,
                                              strict=True)
      else:
        initial_state = self.states
    elif initial_state is None:
      initial_state = self.get_initial_state(inputs)

    if len(initial_state) != len(self.states):
      raise ValueError('Layer has ' + str(len(self.states)) +
                       ' states but was passewwd ' + str(len(initial_state)) +
                       ' initial states.')
    return inputs, initial_state, constants

  def _validate_args_if_ragged(self, is_ragged_input, mask):
    if not is_ragged_input:
      return

    if mask is not None:
      raise ValueError('The mask that was passed in was ' + str(mask) +
                       ' and cannot be applied to RaggedTensor inputs. Please '
                       'make sure that there is no mask passed in by upstream '
                       'layers.')
    if self.unroll:
      raise ValueError('The input received contains RaggedTensors and does '
                       'not support unrolling. Disable unrolling by passing '
                       '`unroll=False` in the RNN Layer constructor.')

  def _maybe_reset_cell_dropout_mask(self, cell):
    if isinstance(cell, DropoutRNNCellMixin):
      cell.reset_dropout_mask()
      cell.reset_recurrent_dropout_mask()

  def reset_states(self, states=None):
    if not self.stateful:
      raise AttributeError('Layer must be stateful.')
    spec_shape = None
    if self.input_spec is not None:
      spec_shape = nest.flatten(self.input_spec[0])[0].shape
    if spec_shape is None:
      # It is possible to have spec shape to be None, eg when construct a RNN
      # with a custom cell, or standard RNN layers (LSTM/GRU) which we only know
      # it has 3 dim input, but not its full shape spec before build().
      batch_size = None
    else:
      batch_size = spec_shape[1] if self.time_major else spec_shape[0]
    if not batch_size:
      raise ValueError('If a RNN is stateful, it needs to know '
                       'its batch size. Specify the batch size '
                       'of your input tensors: \n'
                       '- If using a Sequential model, '
                       'specify the batch size by passing '
                       'a `batch_input_shape` '
                       'argument to your first layer.\n'
                       '- If using the functional API, specify '
                       'the batch size by passing a '
                       '`batch_shape` argument to your Input layer.')

    if nest.flatten(self.states)[0] is None:
      def create_state_variable(state):
        return K.zeros([batch_size] + tensor_shape.as_shape(state).as_list())
      self.states = nest.map_structure(
          create_state_variable, self.cell.state_size)
      if not nest.is_sequence(self.states):
        self.states = [self.states]
    elif states is None:
      for state, size in zip(nest.flatten(self.states),
                             nest.flatten(self.cell.state_size)):
        K.set_value(state, np.zeros([batch_size] +
                                    tensor_shape.as_shape(size).as_list()))
    else:
      flat_states = nest.flatten(self.states)
      flat_input_states = nest.flatten(states)
      if len(flat_input_states) != len(flat_states):
        raise ValueError('Layer ' + self.name + ' expects ' +
                         str(len(flat_states)) + ' states, '
                         'but it received ' + str(len(flat_input_states)) +
                         ' state values. Input received: ' + str(states))
      set_value_tuples = []
      for i, (value, state) in enumerate(zip(flat_input_states,
                                             flat_states)):
        if value.shape != state.shape:
          raise ValueError(
              'State ' + str(i) + ' is incompatible with layer ' +
              self.name + ': expected shape=' + str(
                  (batch_size, state)) + ', found shape=' + str(value.shape))
        set_value_tuples.append((state, value))
      K.batch_set_value(set_value_tuples)
      

  def get_config(self):
    config = {
        'return_sequences': self.return_sequences,
        'return_state': self.return_state,
        'go_backwards': self.go_backwards,
        'stateful': self.stateful,
        'unroll': self.unroll,
        'time_major': self.time_major
    }
    if self._num_constants:
      config['num_constants'] = self._num_constants
    if self.zero_output_for_mask:
      config['zero_output_for_mask'] = self.zero_output_for_mask

    cell_config = self.cell.get_config()
    config['cell'] = {
        'class_name': self.cell.__class__.__name__,
        'config': cell_config
    }
    base_config = super(RNN, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))

  @classmethod
  def from_config(cls, config, custom_objects=None):
    from tensorflow.python.keras.layers import deserialize as deserialize_layer  # pylint: disable=g-import-not-at-top
    cell = deserialize_layer(config.pop('cell'), custom_objects=custom_objects)
    num_constants = config.pop('num_constants', 0)
    layer = cls(cell, **config)
    layer._num_constants = num_constants
    return layer

  @property
  def _trackable_saved_model_saver(self):
    return layer_serialization.RNNSavedModelSaver(self)


@keras_export('keras.layers.AbstractRNNCell')
class AbstractRNNCell(Layer):


  def call(self, inputs, states):

    raise NotImplementedError('Abstract method')

  @property
  def state_size(self):

 
    raise NotImplementedError('Abstract method')

  @property
  def output_size(self):

    raise NotImplementedError('Abstract method')

  def get_initial_state(self, inputs=None, batch_size=None, dtype=None):
    return _generate_zero_filled_state_for_cell(self, inputs, batch_size, dtype)


@doc_controls.do_not_generate_docs
class DropoutRNNCellMixin(object):


  def __init__(self, *args, **kwargs):
    self._create_non_trackable_mask_cache()
    super(DropoutRNNCellMixin, self).__init__(*args, **kwargs)

  @trackable.no_automatic_dependency_tracking
  def _create_non_trackable_mask_cache(self):

    self._dropout_mask_cache = K.ContextValueCache(self._create_dropout_mask)
    self._recurrent_dropout_mask_cache = K.ContextValueCache(
        self._create_recurrent_dropout_mask)

  def reset_dropout_mask(self):

    self._dropout_mask_cache.clear()

  def reset_recurrent_dropout_mask(self):

    self._recurrent_dropout_mask_cache.clear()

  def _create_dropout_mask(self, inputs, training, count=1):
    return _generate_dropout_mask(
        array_ops.ones_like(inputs),
        self.dropout,
        training=training,
        count=count)

  def _create_recurrent_dropout_mask(self, inputs, training, count=1):
    return _generate_dropout_mask(
        array_ops.ones_like(inputs),
        self.recurrent_dropout,
        training=training,
        count=count)

  def get_dropout_mask_for_cell(self, inputs, training, count=1):
    if self.dropout == 0:
      return None
    init_kwargs = dict(inputs=inputs, training=training, count=count)
    return self._dropout_mask_cache.setdefault(kwargs=init_kwargs)

  def get_recurrent_dropout_mask_for_cell(self, inputs, training, count=1):
    if self.recurrent_dropout == 0:
      return None
    init_kwargs = dict(inputs=inputs, training=training, count=count)
    return self._recurrent_dropout_mask_cache.setdefault(kwargs=init_kwargs)

  def __getstate__(self):
    # Used for deepcopy. The caching can't be pickled by python, since it will
    # contain tensor and graph.
    state = super(DropoutRNNCellMixin, self).__getstate__()
    state.pop('_dropout_mask_cache', None)
    state.pop('_recurrent_dropout_mask_cache', None)
    return state

  def __setstate__(self, state):
    state['_dropout_mask_cache'] = K.ContextValueCache(
        self._create_dropout_mask)
    state['_recurrent_dropout_mask_cache'] = K.ContextValueCache(
        self._create_recurrent_dropout_mask)
    super(DropoutRNNCellMixin, self).__setstate__(state)


@keras_export('keras.layers.SimpleRNNCell')
class SimpleRNNCell(DropoutRNNCellMixin, Layer):
  def __init__(self,
               units,
               activation='tanh',
               use_bias=True,
               kernel_initializer='glorot_uniform',
               recurrent_initializer='orthogonal',
               bias_initializer='zeros',
               kernel_regularizer=None,
               recurrent_regularizer=None,
               bias_regularizer=None,
               kernel_constraint=None,
               recurrent_constraint=None,
               bias_constraint=None,
               dropout=0.,
               recurrent_dropout=0.,
               **kwargs):
    # By default use cached variable under v2 mode, see b/143699808.
    if ops.executing_eagerly_outside_functions():
      self._enable_caching_device = kwargs.pop('enable_caching_device', True)
    else:
      self._enable_caching_device = kwargs.pop('enable_caching_device', False)
    super(SimpleRNNCell, self).__init__(**kwargs)
    self.units = units
    self.activation = activations.get(activation)
    self.use_bias = use_bias

    self.kernel_initializer = initializers.get(kernel_initializer)
    self.recurrent_initializer = initializers.get(recurrent_initializer)
    self.bias_initializer = initializers.get(bias_initializer)

    self.kernel_regularizer = regularizers.get(kernel_regularizer)
    self.recurrent_regularizer = regularizers.get(recurrent_regularizer)
    self.bias_regularizer = regularizers.get(bias_regularizer)

    self.kernel_constraint = constraints.get(kernel_constraint)
    self.recurrent_constraint = constraints.get(recurrent_constraint)
    self.bias_constraint = constraints.get(bias_constraint)

    self.dropout = min(1., max(0., dropout))
    self.recurrent_dropout = min(1., max(0., recurrent_dropout))
    self.state_size = self.units
    self.output_size = self.units

  @tf_utils.shape_type_conversion
  def build(self, input_shape):
    default_caching_device = _caching_device(self)
    self.kernel = self.add_weight(
        shape=(input_shape[-1], self.units),
        name='kernel',
        initializer=self.kernel_initializer,
        regularizer=self.kernel_regularizer,
        constraint=self.kernel_constraint,
        caching_device=default_caching_device)
    self.recurrent_kernel = self.add_weight(
        shape=(self.units, self.units),
        name='recurrent_kernel',
        initializer=self.recurrent_initializer,
        regularizer=self.recurrent_regularizer,
        constraint=self.recurrent_constraint,
        caching_device=default_caching_device)
    if self.use_bias:
      self.bias = self.add_weight(
          shape=(self.units,),
          name='bias',
          initializer=self.bias_initializer,
          regularizer=self.bias_regularizer,
          constraint=self.bias_constraint,
          caching_device=default_caching_device)
    else:
      self.bias = None
    self.built = True

  def call(self, inputs, states, training=None):
    prev_output = states[0] if nest.is_sequence(states) else states
    dp_mask = self.get_dropout_mask_for_cell(inputs, training)
    rec_dp_mask = self.get_recurrent_dropout_mask_for_cell(
        prev_output, training)

    if dp_mask is not None:
      h = K.dot(inputs * dp_mask, self.kernel)
    else:
      h = K.dot(inputs, self.kernel)
    if self.bias is not None:
      h = K.bias_add(h, self.bias)

    if rec_dp_mask is not None:
      prev_output = prev_output * rec_dp_mask
    output = h + K.dot(prev_output, self.recurrent_kernel)
    if self.activation is not None:
      output = self.activation(output)

    new_state = [output] if nest.is_sequence(states) else output
    return output, new_state

  def get_initial_state(self, inputs=None, batch_size=None, dtype=None):
    return _generate_zero_filled_state_for_cell(self, inputs, batch_size, dtype)

  def get_config(self):
    config = {
        'units':
            self.units,
        'activation':
            activations.serialize(self.activation),
        'use_bias':
            self.use_bias,
        'kernel_initializer':
            initializers.serialize(self.kernel_initializer),
        'recurrent_initializer':
            initializers.serialize(self.recurrent_initializer),
        'bias_initializer':
            initializers.serialize(self.bias_initializer),
        'kernel_regularizer':
            regularizers.serialize(self.kernel_regularizer),
        'recurrent_regularizer':
            regularizers.serialize(self.recurrent_regularizer),
        'bias_regularizer':
            regularizers.serialize(self.bias_regularizer),
        'kernel_constraint':
            constraints.serialize(self.kernel_constraint),
        'recurrent_constraint':
            constraints.serialize(self.recurrent_constraint),
        'bias_constraint':
            constraints.serialize(self.bias_constraint),
        'dropout':
            self.dropout,
        'recurrent_dropout':
            self.recurrent_dropout
    }
    config.update(_config_for_enable_caching_device(self))
    base_config = super(SimpleRNNCell, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))


@keras_export('keras.layers.SimpleRNN')
class SimpleRNN(RNN):

  def __init__(self,
               units,
               activation='tanh',
               use_bias=True,
               kernel_initializer='glorot_uniform',
               recurrent_initializer='orthogonal',
               bias_initializer='zeros',
               kernel_regularizer=None,
               recurrent_regularizer=None,
               bias_regularizer=None,
               activity_regularizer=None,
               kernel_constraint=None,
               recurrent_constraint=None,
               bias_constraint=None,
               dropout=0.,
               recurrent_dropout=0.,
               return_sequences=False,
               return_state=False,
               go_backwards=False,
               stateful=False,
               unroll=False,
               **kwargs):
    if 'implementation' in kwargs:
      kwargs.pop('implementation')
      logging.warning('The `implementation` argument '
                      'in `SimpleRNN` has been deprecated. '
                      'Please remove it from your layer call.')
    if 'enable_caching_device' in kwargs:
      cell_kwargs = {'enable_caching_device':
                     kwargs.pop('enable_caching_device')}
    else:
      cell_kwargs = {}
    cell = SimpleRNNCell(
        units,
        activation=activation,
        use_bias=use_bias,
        kernel_initializer=kernel_initializer,
        recurrent_initializer=recurrent_initializer,
        bias_initializer=bias_initializer,
        kernel_regularizer=kernel_regularizer,
        recurrent_regularizer=recurrent_regularizer,
        bias_regularizer=bias_regularizer,
        kernel_constraint=kernel_constraint,
        recurrent_constraint=recurrent_constraint,
        bias_constraint=bias_constraint,
        dropout=dropout,
        recurrent_dropout=recurrent_dropout,
        dtype=kwargs.get('dtype'),
        trainable=kwargs.get('trainable', True),
        **cell_kwargs)
    super(SimpleRNN, self).__init__(
        cell,
        return_sequences=return_sequences,
        return_state=return_state,
        go_backwards=go_backwards,
        stateful=stateful,
        unroll=unroll,
        **kwargs)
    self.activity_regularizer = regularizers.get(activity_regularizer)
    self.input_spec = [InputSpec(ndim=3)]

  def call(self, inputs, mask=None, training=None, initial_state=None):
    self._maybe_reset_cell_dropout_mask(self.cell)
    return super(SimpleRNN, self).call(
        inputs, mask=mask, training=training, initial_state=initial_state)

  @property
  def units(self):
    return self.cell.units

  @property
  def activation(self):
    return self.cell.activation

  @property
  def use_bias(self):
    return self.cell.use_bias

  @property
  def kernel_initializer(self):
    return self.cell.kernel_initializer

  @property
  def recurrent_initializer(self):
    return self.cell.recurrent_initializer

  @property
  def bias_initializer(self):
    return self.cell.bias_initializer

  @property
  def kernel_regularizer(self):
    return self.cell.kernel_regularizer

  @property
  def recurrent_regularizer(self):
    return self.cell.recurrent_regularizer

  @property
  def bias_regularizer(self):
    return self.cell.bias_regularizer

  @property
  def kernel_constraint(self):
    return self.cell.kernel_constraint

  @property
  def recurrent_constraint(self):
    return self.cell.recurrent_constraint

  @property
  def bias_constraint(self):
    return self.cell.bias_constraint

  @property
  def dropout(self):
    return self.cell.dropout

  @property
  def recurrent_dropout(self):
    return self.cell.recurrent_dropout

  def get_config(self):
    config = {
        'units':
            self.units,
        'activation':
            activations.serialize(self.activation),
        'use_bias':
            self.use_bias,
        'kernel_initializer':
            initializers.serialize(self.kernel_initializer),
        'recurrent_initializer':
            initializers.serialize(self.recurrent_initializer),
        'bias_initializer':
            initializers.serialize(self.bias_initializer),
        'kernel_regularizer':
            regularizers.serialize(self.kernel_regularizer),
        'recurrent_regularizer':
            regularizers.serialize(self.recurrent_regularizer),
        'bias_regularizer':
            regularizers.serialize(self.bias_regularizer),
        'activity_regularizer':
            regularizers.serialize(self.activity_regularizer),
        'kernel_constraint':
            constraints.serialize(self.kernel_constraint),
        'recurrent_constraint':
            constraints.serialize(self.recurrent_constraint),
        'bias_constraint':
            constraints.serialize(self.bias_constraint),
        'dropout':
            self.dropout,
        'recurrent_dropout':
            self.recurrent_dropout
    }
    base_config = super(SimpleRNN, self).get_config()
    config.update(_config_for_enable_caching_device(self.cell))
    del base_config['cell']
    return dict(list(base_config.items()) + list(config.items()))

  @classmethod
  def from_config(cls, config):
    if 'implementation' in config:
      config.pop('implementation')
    return cls(**config)


@keras_export(v1=['keras.layers.GRUCell'])
class GRUCell(DropoutRNNCellMixin, Layer):

  def __init__(self,
               units,
               activation='tanh',
               recurrent_activation='hard_sigmoid',
               use_bias=True,
               kernel_initializer='glorot_uniform',
               recurrent_initializer='orthogonal',
               bias_initializer='zeros',
               kernel_regularizer=None,
               recurrent_regularizer=None,
               bias_regularizer=None,
               kernel_constraint=None,
               recurrent_constraint=None,
               bias_constraint=None,
               dropout=0.,
               recurrent_dropout=0.,
               implementation=1,
               reset_after=False,
               **kwargs):
    # By default use cached variable under v2 mode, see b/143699808.
    if ops.executing_eagerly_outside_functions():
      self._enable_caching_device = kwargs.pop('enable_caching_device', True)
    else:
      self._enable_caching_device = kwargs.pop('enable_caching_device', False)
    super(GRUCell, self).__init__(**kwargs)
    self.units = units
    self.activation = activations.get(activation)
    self.recurrent_activation = activations.get(recurrent_activation)
    self.use_bias = use_bias

    self.kernel_initializer = initializers.get(kernel_initializer)
    self.recurrent_initializer = initializers.get(recurrent_initializer)
    self.bias_initializer = initializers.get(bias_initializer)

    self.kernel_regularizer = regularizers.get(kernel_regularizer)
    self.recurrent_regularizer = regularizers.get(recurrent_regularizer)
    self.bias_regularizer = regularizers.get(bias_regularizer)

    self.kernel_constraint = constraints.get(kernel_constraint)
    self.recurrent_constraint = constraints.get(recurrent_constraint)
    self.bias_constraint = constraints.get(bias_constraint)

    self.dropout = min(1., max(0., dropout))
    self.recurrent_dropout = min(1., max(0., recurrent_dropout))
    if self.recurrent_dropout != 0 and implementation != 1:
      logging.debug(RECURRENT_DROPOUT_WARNING_MSG)
      self.implementation = 1
    else:
      self.implementation = implementation
    self.reset_after = reset_after
    self.state_size = self.units
    self.output_size = self.units

  @tf_utils.shape_type_conversion
  def build(self, input_shape):
    input_dim = input_shape[-1]
    default_caching_device = _caching_device(self)
    self.kernel = self.add_weight(
        shape=(input_dim, self.units * 3),
        name='kernel',
        initializer=self.kernel_initializer,
        regularizer=self.kernel_regularizer,
        constraint=self.kernel_constraint,
        caching_device=default_caching_device)
    self.recurrent_kernel = self.add_weight(
        shape=(self.units, self.units * 3),
        name='recurrent_kernel',
        initializer=self.recurrent_initializer,
        regularizer=self.recurrent_regularizer,
        constraint=self.recurrent_constraint,
        caching_device=default_caching_device)

    if self.use_bias:
      if not self.reset_after:
        bias_shape = (3 * self.units,)
      else:
        # separate biases for input and recurrent kernels
        # Note: the shape is intentionally different from CuDNNGRU biases
        # `(2 * 3 * self.units,)`, so that we can distinguish the classes
        # when loading and converting saved weights.
        bias_shape = (2, 3 * self.units)
      self.bias = self.add_weight(shape=bias_shape,
                                  name='bias',
                                  initializer=self.bias_initializer,
                                  regularizer=self.bias_regularizer,
                                  constraint=self.bias_constraint,
                                  caching_device=default_caching_device)
    else:
      self.bias = None
    self.built = True

  def call(self, inputs, states, training=None):
    h_tm1 = states[0] if nest.is_sequence(states) else states  # previous memory

    dp_mask = self.get_dropout_mask_for_cell(inputs, training, count=3)
    rec_dp_mask = self.get_recurrent_dropout_mask_for_cell(
        h_tm1, training, count=3)

    if self.use_bias:
      if not self.reset_after:
        input_bias, recurrent_bias = self.bias, None
      else:
        input_bias, recurrent_bias = array_ops.unstack(self.bias)

    if self.implementation == 1:
      if 0. < self.dropout < 1.:
        inputs_z = inputs * dp_mask[0]
        inputs_r = inputs * dp_mask[1]
        inputs_h = inputs * dp_mask[2]
      else:
        inputs_z = inputs
        inputs_r = inputs
        inputs_h = inputs

      x_z = K.dot(inputs_z, self.kernel[:, :self.units])
      x_r = K.dot(inputs_r, self.kernel[:, self.units:self.units * 2])
      x_h = K.dot(inputs_h, self.kernel[:, self.units * 2:])

      if self.use_bias:
        x_z = K.bias_add(x_z, input_bias[:self.units])
        x_r = K.bias_add(x_r, input_bias[self.units: self.units * 2])
        x_h = K.bias_add(x_h, input_bias[self.units * 2:])

      if 0. < self.recurrent_dropout < 1.:
        h_tm1_z = h_tm1 * rec_dp_mask[0]
        h_tm1_r = h_tm1 * rec_dp_mask[1]
        h_tm1_h = h_tm1 * rec_dp_mask[2]
      else:
        h_tm1_z = h_tm1
        h_tm1_r = h_tm1
        h_tm1_h = h_tm1

      recurrent_z = K.dot(h_tm1_z, self.recurrent_kernel[:, :self.units])
      recurrent_r = K.dot(h_tm1_r,
                          self.recurrent_kernel[:, self.units:self.units * 2])
      if self.reset_after and self.use_bias:
        recurrent_z = K.bias_add(recurrent_z, recurrent_bias[:self.units])
        recurrent_r = K.bias_add(recurrent_r,
                                 recurrent_bias[self.units:self.units * 2])

      z = self.recurrent_activation(x_z + recurrent_z)
      r = self.recurrent_activation(x_r + recurrent_r)

      # reset gate applied after/before matrix multiplication
      if self.reset_after:
        recurrent_h = K.dot(h_tm1_h, self.recurrent_kernel[:, self.units * 2:])
        if self.use_bias:
          recurrent_h = K.bias_add(recurrent_h, recurrent_bias[self.units * 2:])
        recurrent_h = r * recurrent_h
      else:
        recurrent_h = K.dot(r * h_tm1_h,
                            self.recurrent_kernel[:, self.units * 2:])

      hh = self.activation(x_h + recurrent_h)
    else:
      if 0. < self.dropout < 1.:
        inputs = inputs * dp_mask[0]

      # inputs projected by all gate matrices at once
      matrix_x = K.dot(inputs, self.kernel)
      if self.use_bias:
        # biases: bias_z_i, bias_r_i, bias_h_i
        matrix_x = K.bias_add(matrix_x, input_bias)

      x_z, x_r, x_h = array_ops.split(matrix_x, 3, axis=-1)

      if self.reset_after:
        # hidden state projected by all gate matrices at once
        matrix_inner = K.dot(h_tm1, self.recurrent_kernel)
        if self.use_bias:
          matrix_inner = K.bias_add(matrix_inner, recurrent_bias)
      else:
        # hidden state projected separately for update/reset and new
        matrix_inner = K.dot(h_tm1, self.recurrent_kernel[:, :2 * self.units])

      recurrent_z, recurrent_r, recurrent_h = array_ops.split(
          matrix_inner, [self.units, self.units, -1], axis=-1)

      z = self.recurrent_activation(x_z + recurrent_z)
      r = self.recurrent_activation(x_r + recurrent_r)

      if self.reset_after:
        recurrent_h = r * recurrent_h
      else:
        recurrent_h = K.dot(r * h_tm1,
                            self.recurrent_kernel[:, 2 * self.units:])

      hh = self.activation(x_h + recurrent_h)
    # previous and candidate state mixed by update gate
    h = z * h_tm1 + (1 - z) * hh
    new_state = [h] if nest.is_sequence(states) else h
    return h, new_state

  def get_config(self):
    config = {
        'units': self.units,
        'activation': activations.serialize(self.activation),
        'recurrent_activation':
            activations.serialize(self.recurrent_activation),
        'use_bias': self.use_bias,
        'kernel_initializer': initializers.serialize(self.kernel_initializer),
        'recurrent_initializer':
            initializers.serialize(self.recurrent_initializer),
        'bias_initializer': initializers.serialize(self.bias_initializer),
        'kernel_regularizer': regularizers.serialize(self.kernel_regularizer),
        'recurrent_regularizer':
            regularizers.serialize(self.recurrent_regularizer),
        'bias_regularizer': regularizers.serialize(self.bias_regularizer),
        'kernel_constraint': constraints.serialize(self.kernel_constraint),
        'recurrent_constraint':
            constraints.serialize(self.recurrent_constraint),
        'bias_constraint': constraints.serialize(self.bias_constraint),
        'dropout': self.dropout,
        'recurrent_dropout': self.recurrent_dropout,
        'implementation': self.implementation,
        'reset_after': self.reset_after
    }
    config.update(_config_for_enable_caching_device(self))
    base_config = super(GRUCell, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))

  def get_initial_state(self, inputs=None, batch_size=None, dtype=None):
    return _generate_zero_filled_state_for_cell(self, inputs, batch_size, dtype)


@keras_export(v1=['keras.layers.GRU'])
class GRU(RNN):

  def __init__(self,
               units,
               activation='tanh',
               recurrent_activation='hard_sigmoid',
               use_bias=True,
               kernel_initializer='glorot_uniform',
               recurrent_initializer='orthogonal',
               bias_initializer='zeros',
               kernel_regularizer=None,
               recurrent_regularizer=None,
               bias_regularizer=None,
               activity_regularizer=None,
               kernel_constraint=None,
               recurrent_constraint=None,
               bias_constraint=None,
               dropout=0.,
               recurrent_dropout=0.,
               implementation=1,
               return_sequences=False,
               return_state=False,
               go_backwards=False,
               stateful=False,
               unroll=False,
               reset_after=False,
               **kwargs):
    if implementation == 0:
      logging.warning('`implementation=0` has been deprecated, '
                      'and now defaults to `implementation=1`.'
                      'Please update your layer call.')
    if 'enable_caching_device' in kwargs:
      cell_kwargs = {'enable_caching_device':
                     kwargs.pop('enable_caching_device')}
    else:
      cell_kwargs = {}
    cell = GRUCell(
        units,
        activation=activation,
        recurrent_activation=recurrent_activation,
        use_bias=use_bias,
        kernel_initializer=kernel_initializer,
        recurrent_initializer=recurrent_initializer,
        bias_initializer=bias_initializer,
        kernel_regularizer=kernel_regularizer,
        recurrent_regularizer=recurrent_regularizer,
        bias_regularizer=bias_regularizer,
        kernel_constraint=kernel_constraint,
        recurrent_constraint=recurrent_constraint,
        bias_constraint=bias_constraint,
        dropout=dropout,
        recurrent_dropout=recurrent_dropout,
        implementation=implementation,
        reset_after=reset_after,
        dtype=kwargs.get('dtype'),
        trainable=kwargs.get('trainable', True),
        **cell_kwargs)
    super(GRU, self).__init__(
        cell,
        return_sequences=return_sequences,
        return_state=return_state,
        go_backwards=go_backwards,
        stateful=stateful,
        unroll=unroll,
        **kwargs)
    self.activity_regularizer = regularizers.get(activity_regularizer)
    self.input_spec = [InputSpec(ndim=3)]

  def call(self, inputs, mask=None, training=None, initial_state=None):
    self._maybe_reset_cell_dropout_mask(self.cell)
    return super(GRU, self).call(
        inputs, mask=mask, training=training, initial_state=initial_state)

  @property
  def units(self):
    return self.cell.units

  @property
  def activation(self):
    return self.cell.activation

  @property
  def recurrent_activation(self):
    return self.cell.recurrent_activation

  @property
  def use_bias(self):
    return self.cell.use_bias

  @property
  def kernel_initializer(self):
    return self.cell.kernel_initializer

  @property
  def recurrent_initializer(self):
    return self.cell.recurrent_initializer

  @property
  def bias_initializer(self):
    return self.cell.bias_initializer

  @property
  def kernel_regularizer(self):
    return self.cell.kernel_regularizer

  @property
  def recurrent_regularizer(self):
    return self.cell.recurrent_regularizer

  @property
  def bias_regularizer(self):
    return self.cell.bias_regularizer

  @property
  def kernel_constraint(self):
    return self.cell.kernel_constraint

  @property
  def recurrent_constraint(self):
    return self.cell.recurrent_constraint

  @property
  def bias_constraint(self):
    return self.cell.bias_constraint

  @property
  def dropout(self):
    return self.cell.dropout

  @property
  def recurrent_dropout(self):
    return self.cell.recurrent_dropout

  @property
  def implementation(self):
    return self.cell.implementation

  @property
  def reset_after(self):
    return self.cell.reset_after

  def get_config(self):
    config = {
        'units':
            self.units,
        'activation':
            activations.serialize(self.activation),
        'recurrent_activation':
            activations.serialize(self.recurrent_activation),
        'use_bias':
            self.use_bias,
        'kernel_initializer':
            initializers.serialize(self.kernel_initializer),
        'recurrent_initializer':
            initializers.serialize(self.recurrent_initializer),
        'bias_initializer':
            initializers.serialize(self.bias_initializer),
        'kernel_regularizer':
            regularizers.serialize(self.kernel_regularizer),
        'recurrent_regularizer':
            regularizers.serialize(self.recurrent_regularizer),
        'bias_regularizer':
            regularizers.serialize(self.bias_regularizer),
        'activity_regularizer':
            regularizers.serialize(self.activity_regularizer),
        'kernel_constraint':
            constraints.serialize(self.kernel_constraint),
        'recurrent_constraint':
            constraints.serialize(self.recurrent_constraint),
        'bias_constraint':
            constraints.serialize(self.bias_constraint),
        'dropout':
            self.dropout,
        'recurrent_dropout':
            self.recurrent_dropout,
        'implementation':
            self.implementation,
        'reset_after':
            self.reset_after
    }
    config.update(_config_for_enable_caching_device(self.cell))
    base_config = super(GRU, self).get_config()
    del base_config['cell']
    return dict(list(base_config.items()) + list(config.items()))

  @classmethod
  def from_config(cls, config):
    if 'implementation' in config and config['implementation'] == 0:
      config['implementation'] = 1
    return cls(**config)


@keras_export(v1=['keras.layers.LSTMCell'])
class LSTMCell(DropoutRNNCellMixin, Layer):

  def __init__(self,
               units,
               activation='tanh',
               recurrent_activation='hard_sigmoid',
               use_bias=True,
               kernel_initializer='glorot_uniform',
               recurrent_initializer='orthogonal',
               bias_initializer='zeros',
               unit_forget_bias=True,
               kernel_regularizer=None,
               recurrent_regularizer=None,
               bias_regularizer=None,
               kernel_constraint=None,
               recurrent_constraint=None,
               bias_constraint=None,
               dropout=0.,
               recurrent_dropout=0.,
               implementation=1,
               **kwargs):
    # By default use cached variable under v2 mode, see b/143699808.
    if ops.executing_eagerly_outside_functions():
      self._enable_caching_device = kwargs.pop('enable_caching_device', True)
    else:
      self._enable_caching_device = kwargs.pop('enable_caching_device', False)
    super(LSTMCell, self).__init__(**kwargs)
    self.units = units
    self.activation = activations.get(activation)
    self.recurrent_activation = activations.get(recurrent_activation)
    self.use_bias = use_bias

    self.kernel_initializer = initializers.get(kernel_initializer)
    self.recurrent_initializer = initializers.get(recurrent_initializer)
    self.bias_initializer = initializers.get(bias_initializer)
    self.unit_forget_bias = unit_forget_bias

    self.kernel_regularizer = regularizers.get(kernel_regularizer)
    self.recurrent_regularizer = regularizers.get(recurrent_regularizer)
    self.bias_regularizer = regularizers.get(bias_regularizer)

    self.kernel_constraint = constraints.get(kernel_constraint)
    self.recurrent_constraint = constraints.get(recurrent_constraint)
    self.bias_constraint = constraints.get(bias_constraint)

    self.dropout = min(1., max(0., dropout))
    self.recurrent_dropout = min(1., max(0., recurrent_dropout))
    if self.recurrent_dropout != 0 and implementation != 1:
      logging.debug(RECURRENT_DROPOUT_WARNING_MSG)
      self.implementation = 1
    else:
      self.implementation = implementation
    # tuple(_ListWrapper) was silently dropping list content in at least 2.7.10,
    # and fixed after 2.7.16. Converting the state_size to wrapper around
    # NoDependency(), so that the base_layer.__setattr__ will not convert it to
    # ListWrapper. Down the stream, self.states will be a list since it is
    # generated from nest.map_structure with list, and tuple(list) will work
    # properly.
    self.state_size = data_structures.NoDependency([self.units, self.units])
    self.output_size = self.units

  @tf_utils.shape_type_conversion
  def build(self, input_shape):
    default_caching_device = _caching_device(self)
    input_dim = input_shape[-1]
    self.kernel = self.add_weight(
        shape=(input_dim, self.units * 4),
        name='kernel',
        initializer=self.kernel_initializer,
        regularizer=self.kernel_regularizer,
        constraint=self.kernel_constraint,
        caching_device=default_caching_device)
    self.recurrent_kernel = self.add_weight(
        shape=(self.units, self.units * 4),
        name='recurrent_kernel',
        initializer=self.recurrent_initializer,
        regularizer=self.recurrent_regularizer,
        constraint=self.recurrent_constraint,
        caching_device=default_caching_device)

    if self.use_bias:
      if self.unit_forget_bias:

        def bias_initializer(_, *args, **kwargs):
          return K.concatenate([
              self.bias_initializer((self.units,), *args, **kwargs),
              initializers.get('ones')((self.units,), *args, **kwargs),
              self.bias_initializer((self.units * 2,), *args, **kwargs),
          ])
      else:
        bias_initializer = self.bias_initializer
      self.bias = self.add_weight(
          shape=(self.units * 4,),
          name='bias',
          initializer=bias_initializer,
          regularizer=self.bias_regularizer,
          constraint=self.bias_constraint,
          caching_device=default_caching_device)
    else:
      self.bias = None
    self.built = True

  def _compute_carry_and_output(self, x, h_tm1, c_tm1):
    """Computes carry and output using split kernels."""
    x_i, x_f, x_c, x_o = x
    h_tm1_i, h_tm1_f, h_tm1_c, h_tm1_o = h_tm1
    i = self.recurrent_activation(
        x_i + K.dot(h_tm1_i, self.recurrent_kernel[:, :self.units]))
    f = self.recurrent_activation(x_f + K.dot(
        h_tm1_f, self.recurrent_kernel[:, self.units:self.units * 2]))
    c = f * c_tm1 + i * self.activation(x_c + K.dot(
        h_tm1_c, self.recurrent_kernel[:, self.units * 2:self.units * 3]))
    o = self.recurrent_activation(
        x_o + K.dot(h_tm1_o, self.recurrent_kernel[:, self.units * 3:]))
    return c, o

  def _compute_carry_and_output_fused(self, z, c_tm1):
    """Computes carry and output using fused kernels."""
    z0, z1, z2, z3 = z
    i = self.recurrent_activation(z0)
    f = self.recurrent_activation(z1)
    c = f * c_tm1 + i * self.activation(z2)
    o = self.recurrent_activation(z3)
    return c, o

  def call(self, inputs, states, training=None):
    h_tm1 = states[0]  # previous memory state
    c_tm1 = states[1]  # previous carry state

    dp_mask = self.get_dropout_mask_for_cell(inputs, training, count=4)
    rec_dp_mask = self.get_recurrent_dropout_mask_for_cell(
        h_tm1, training, count=4)

    if self.implementation == 1:
      if 0 < self.dropout < 1.:
        inputs_i = inputs * dp_mask[0]
        inputs_f = inputs * dp_mask[1]
        inputs_c = inputs * dp_mask[2]
        inputs_o = inputs * dp_mask[3]
      else:
        inputs_i = inputs
        inputs_f = inputs
        inputs_c = inputs
        inputs_o = inputs
      k_i, k_f, k_c, k_o = array_ops.split(
          self.kernel, num_or_size_splits=4, axis=1)
      x_i = K.dot(inputs_i, k_i)
      x_f = K.dot(inputs_f, k_f)
      x_c = K.dot(inputs_c, k_c)
      x_o = K.dot(inputs_o, k_o)
      if self.use_bias:
        b_i, b_f, b_c, b_o = array_ops.split(
            self.bias, num_or_size_splits=4, axis=0)
        x_i = K.bias_add(x_i, b_i)
        x_f = K.bias_add(x_f, b_f)
        x_c = K.bias_add(x_c, b_c)
        x_o = K.bias_add(x_o, b_o)

      if 0 < self.recurrent_dropout < 1.:
        h_tm1_i = h_tm1 * rec_dp_mask[0]
        h_tm1_f = h_tm1 * rec_dp_mask[1]
        h_tm1_c = h_tm1 * rec_dp_mask[2]
        h_tm1_o = h_tm1 * rec_dp_mask[3]
      else:
        h_tm1_i = h_tm1
        h_tm1_f = h_tm1
        h_tm1_c = h_tm1
        h_tm1_o = h_tm1
      x = (x_i, x_f, x_c, x_o)
      h_tm1 = (h_tm1_i, h_tm1_f, h_tm1_c, h_tm1_o)
      c, o = self._compute_carry_and_output(x, h_tm1, c_tm1)
    else:
      if 0. < self.dropout < 1.:
        inputs = inputs * dp_mask[0]
      z = K.dot(inputs, self.kernel)
      z += K.dot(h_tm1, self.recurrent_kernel)
      if self.use_bias:
        z = K.bias_add(z, self.bias)

      z = array_ops.split(z, num_or_size_splits=4, axis=1)
      c, o = self._compute_carry_and_output_fused(z, c_tm1)

    h = o * self.activation(c)
    return h, [h, c]

  def get_config(self):
    config = {
        'units':
            self.units,
        'activation':
            activations.serialize(self.activation),
        'recurrent_activation':
            activations.serialize(self.recurrent_activation),
        'use_bias':
            self.use_bias,
        'kernel_initializer':
            initializers.serialize(self.kernel_initializer),
        'recurrent_initializer':
            initializers.serialize(self.recurrent_initializer),
        'bias_initializer':
            initializers.serialize(self.bias_initializer),
        'unit_forget_bias':
            self.unit_forget_bias,
        'kernel_regularizer':
            regularizers.serialize(self.kernel_regularizer),
        'recurrent_regularizer':
            regularizers.serialize(self.recurrent_regularizer),
        'bias_regularizer':
            regularizers.serialize(self.bias_regularizer),
        'kernel_constraint':
            constraints.serialize(self.kernel_constraint),
        'recurrent_constraint':
            constraints.serialize(self.recurrent_constraint),
        'bias_constraint':
            constraints.serialize(self.bias_constraint),
        'dropout':
            self.dropout,
        'recurrent_dropout':
            self.recurrent_dropout,
        'implementation':
            self.implementation
    }
    config.update(_config_for_enable_caching_device(self))
    base_config = super(LSTMCell, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))

  def get_initial_state(self, inputs=None, batch_size=None, dtype=None):
    return list(_generate_zero_filled_state_for_cell(
        self, inputs, batch_size, dtype))


@keras_export('keras.experimental.PeepholeLSTMCell')
class PeepholeLSTMCell(LSTMCell):

  def build(self, input_shape):
    super(PeepholeLSTMCell, self).build(input_shape)
    # The following are the weight matrices for the peephole connections. These
    # are multiplied with the previous internal state during the computation of
    # carry and output.
    self.input_gate_peephole_weights = self.add_weight(
        shape=(self.units,),
        name='input_gate_peephole_weights',
        initializer=self.kernel_initializer)
    self.forget_gate_peephole_weights = self.add_weight(
        shape=(self.units,),
        name='forget_gate_peephole_weights',
        initializer=self.kernel_initializer)
    self.output_gate_peephole_weights = self.add_weight(
        shape=(self.units,),
        name='output_gate_peephole_weights',
        initializer=self.kernel_initializer)

  def _compute_carry_and_output(self, x, h_tm1, c_tm1):
    x_i, x_f, x_c, x_o = x
    h_tm1_i, h_tm1_f, h_tm1_c, h_tm1_o = h_tm1
    i = self.recurrent_activation(
        x_i + K.dot(h_tm1_i, self.recurrent_kernel[:, :self.units]) +
        self.input_gate_peephole_weights * c_tm1)
    f = self.recurrent_activation(x_f + K.dot(
        h_tm1_f, self.recurrent_kernel[:, self.units:self.units * 2]) +
                                  self.forget_gate_peephole_weights * c_tm1)
    c = f * c_tm1 + i * self.activation(x_c + K.dot(
        h_tm1_c, self.recurrent_kernel[:, self.units * 2:self.units * 3]))
    o = self.recurrent_activation(
        x_o + K.dot(h_tm1_o, self.recurrent_kernel[:, self.units * 3:]) +
        self.output_gate_peephole_weights * c)
    return c, o

  def _compute_carry_and_output_fused(self, z, c_tm1):
    z0, z1, z2, z3 = z
    i = self.recurrent_activation(z0 +
                                  self.input_gate_peephole_weights * c_tm1)
    f = self.recurrent_activation(z1 +
                                  self.forget_gate_peephole_weights * c_tm1)
    c = f * c_tm1 + i * self.activation(z2)
    o = self.recurrent_activation(z3 + self.output_gate_peephole_weights * c)
    return c, o


@keras_export(v1=['keras.layers.LSTM'])
class LSTM(RNN):

  def __init__(self,
               units,
               activation='tanh',
               recurrent_activation='hard_sigmoid',
               use_bias=True,
               kernel_initializer='glorot_uniform',
               recurrent_initializer='orthogonal',
               bias_initializer='zeros',
               unit_forget_bias=True,
               kernel_regularizer=None,
               recurrent_regularizer=None,
               bias_regularizer=None,
               activity_regularizer=None,
               kernel_constraint=None,
               recurrent_constraint=None,
               bias_constraint=None,
               dropout=0.,
               recurrent_dropout=0.,
               implementation=1,
               return_sequences=False,
               return_state=False,
               go_backwards=False,
               stateful=False,
               unroll=False,
               **kwargs):
    if implementation == 0:
      logging.warning('`implementation=0` has been deprecated, '
                      'and now defaults to `implementation=1`.'
                      'Please update your layer call.')
    if 'enable_caching_device' in kwargs:
      cell_kwargs = {'enable_caching_device':
                     kwargs.pop('enable_caching_device')}
    else:
      cell_kwargs = {}
    cell = LSTMCell(
        units,
        activation=activation,
        recurrent_activation=recurrent_activation,
        use_bias=use_bias,
        kernel_initializer=kernel_initializer,
        recurrent_initializer=recurrent_initializer,
        unit_forget_bias=unit_forget_bias,
        bias_initializer=bias_initializer,
        kernel_regularizer=kernel_regularizer,
        recurrent_regularizer=recurrent_regularizer,
        bias_regularizer=bias_regularizer,
        kernel_constraint=kernel_constraint,
        recurrent_constraint=recurrent_constraint,
        bias_constraint=bias_constraint,
        dropout=dropout,
        recurrent_dropout=recurrent_dropout,
        implementation=implementation,
        dtype=kwargs.get('dtype'),
        trainable=kwargs.get('trainable', True),
        **cell_kwargs)
    super(LSTM, self).__init__(
        cell,
        return_sequences=return_sequences,
        return_state=return_state,
        go_backwards=go_backwards,
        stateful=stateful,
        unroll=unroll,
        **kwargs)
    self.activity_regularizer = regularizers.get(activity_regularizer)
    self.input_spec = [InputSpec(ndim=3)]

  def call(self, inputs, mask=None, training=None, initial_state=None):
    self._maybe_reset_cell_dropout_mask(self.cell)
    return super(LSTM, self).call(
        inputs, mask=mask, training=training, initial_state=initial_state)

  @property
  def units(self):
    return self.cell.units

  @property
  def activation(self):
    return self.cell.activation

  @property
  def recurrent_activation(self):
    return self.cell.recurrent_activation

  @property
  def use_bias(self):
    return self.cell.use_bias

  @property
  def kernel_initializer(self):
    return self.cell.kernel_initializer

  @property
  def recurrent_initializer(self):
    return self.cell.recurrent_initializer

  @property
  def bias_initializer(self):
    return self.cell.bias_initializer

  @property
  def unit_forget_bias(self):
    return self.cell.unit_forget_bias

  @property
  def kernel_regularizer(self):
    return self.cell.kernel_regularizer

  @property
  def recurrent_regularizer(self):
    return self.cell.recurrent_regularizer

  @property
  def bias_regularizer(self):
    return self.cell.bias_regularizer

  @property
  def kernel_constraint(self):
    return self.cell.kernel_constraint

  @property
  def recurrent_constraint(self):
    return self.cell.recurrent_constraint

  @property
  def bias_constraint(self):
    return self.cell.bias_constraint

  @property
  def dropout(self):
    return self.cell.dropout

  @property
  def recurrent_dropout(self):
    return self.cell.recurrent_dropout

  @property
  def implementation(self):
    return self.cell.implementation

  def get_config(self):
    config = {
        'units':
            self.units,
        'activation':
            activations.serialize(self.activation),
        'recurrent_activation':
            activations.serialize(self.recurrent_activation),
        'use_bias':
            self.use_bias,
        'kernel_initializer':
            initializers.serialize(self.kernel_initializer),
        'recurrent_initializer':
            initializers.serialize(self.recurrent_initializer),
        'bias_initializer':
            initializers.serialize(self.bias_initializer),
        'unit_forget_bias':
            self.unit_forget_bias,
        'kernel_regularizer':
            regularizers.serialize(self.kernel_regularizer),
        'recurrent_regularizer':
            regularizers.serialize(self.recurrent_regularizer),
        'bias_regularizer':
            regularizers.serialize(self.bias_regularizer),
        'activity_regularizer':
            regularizers.serialize(self.activity_regularizer),
        'kernel_constraint':
            constraints.serialize(self.kernel_constraint),
        'recurrent_constraint':
            constraints.serialize(self.recurrent_constraint),
        'bias_constraint':
            constraints.serialize(self.bias_constraint),
        'dropout':
            self.dropout,
        'recurrent_dropout':
            self.recurrent_dropout,
        'implementation':
            self.implementation
    }
    config.update(_config_for_enable_caching_device(self.cell))
    base_config = super(LSTM, self).get_config()
    del base_config['cell']
    return dict(list(base_config.items()) + list(config.items()))

  @classmethod
  def from_config(cls, config):
    if 'implementation' in config and config['implementation'] == 0:
      config['implementation'] = 1
    return cls(**config)


def _generate_dropout_mask(ones, rate, training=None, count=1):
  def dropped_inputs():
    return K.dropout(ones, rate)

  if count > 1:
    return [
        K.in_train_phase(dropped_inputs, ones, training=training)
        for _ in range(count)
    ]
  return K.in_train_phase(dropped_inputs, ones, training=training)


def _standardize_args(inputs, initial_state, constants, num_constants):
  if isinstance(inputs, list):
    assert initial_state is None and constants is None
    if num_constants:
      constants = inputs[-num_constants:]
      inputs = inputs[:-num_constants]
    if len(inputs) > 1:
      initial_state = inputs[1:]
      inputs = inputs[:1]

    if len(inputs) > 1:
      inputs = tuple(inputs)
    else:
      inputs = inputs[0]

  def to_list_or_none(x):
    if x is None or isinstance(x, list):
      return x
    if isinstance(x, tuple):
      return list(x)
    return [x]

  initial_state = to_list_or_none(initial_state)
  constants = to_list_or_none(constants)

  return inputs, initial_state, constants


def _is_multiple_state(state_size):
  return (hasattr(state_size, '__len__') and
          not isinstance(state_size, tensor_shape.TensorShape))


def _generate_zero_filled_state_for_cell(cell, inputs, batch_size, dtype):
  if inputs is not None:
    batch_size = array_ops.shape(inputs)[0]
    dtype = inputs.dtype
  return _generate_zero_filled_state(batch_size, cell.state_size, dtype)


def _generate_zero_filled_state(batch_size_tensor, state_size, dtype):
  if batch_size_tensor is None or dtype is None:
    raise ValueError(
        'batch_size and dtype cannot be None while constructing initial state: '
        'batch_size={}, dtype={}'.format(batch_size_tensor, dtype))

  def create_zeros(unnested_state_size):
    flat_dims = tensor_shape.as_shape(unnested_state_size).as_list()
    init_state_size = [batch_size_tensor] + flat_dims
    return array_ops.zeros(init_state_size, dtype=dtype)

  if nest.is_sequence(state_size):
    return nest.map_structure(create_zeros, state_size)
  else:
    return create_zeros(state_size)


def _caching_device(rnn_cell):
  if context.executing_eagerly():
    # caching_device is not supported in eager mode.
    return None
  if not getattr(rnn_cell, '_enable_caching_device', False):
    return None

  if control_flow_util.IsInWhileLoop(ops.get_default_graph()):
    logging.warn('Variable read device caching has been disabled because the '
                 'RNN is in tf.while_loop loop context, which will cause '
                 'reading stalled value in forward path. This could slow down '
                 'the training due to duplicated variable reads. Please '
                 'consider updating your code to remove tf.while_loop if '
                 'possible.')
    return None
  if rnn_cell._dtype_policy.should_cast_variables:
    logging.warn('Variable read device caching has been disabled since it '
                 'doesn\'t work with the mixed precision API. This is '
                 'likely to cause a slowdown for RNN training due to '
                 'duplicated read of variable for each timestep, which '
                 'will be significant in a multi remote worker setting. '
                 'Please consider disabling mixed precision API if '
                 'the performance has been affected.')
    return None
  # Cache the value on the device that access the variable.
  return lambda op: op.device


def _config_for_enable_caching_device(rnn_cell):
  default_enable_caching_device = ops.executing_eagerly_outside_functions()
  if rnn_cell._enable_caching_device != default_enable_caching_device:
    return {'enable_caching_device': rnn_cell._enable_caching_device}
  return {}

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools

from tensorflow.python.framework import tensor_shape
from tensorflow.python.keras import backend
from tensorflow.python.keras.engine.base_layer import Layer
from tensorflow.python.keras.engine.input_spec import InputSpec
from tensorflow.python.keras.utils import conv_utils
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn
from tensorflow.python.util.tf_export import keras_export


class Pooling1D(Layer):
  def __init__(self, pool_function, pool_size, strides,
               padding='valid', data_format='channels_last',
               name=None, **kwargs):
    super(Pooling1D, self).__init__(name=name, **kwargs)
    if data_format is None:
      data_format = backend.image_data_format()
    if strides is None:
      strides = pool_size
    self.pool_function = pool_function
    self.pool_size = conv_utils.normalize_tuple(pool_size, 1, 'pool_size')
    self.strides = conv_utils.normalize_tuple(strides, 1, 'strides')
    self.padding = conv_utils.normalize_padding(padding)
    self.data_format = conv_utils.normalize_data_format(data_format)
    self.input_spec = InputSpec(ndim=3)

  def call(self, inputs):
    pad_axis = 2 if self.data_format == 'channels_last' else 3
    inputs = array_ops.expand_dims(inputs, pad_axis)
    outputs = self.pool_function(
        inputs,
        self.pool_size + (1,),
        strides=self.strides + (1,),
        padding=self.padding,
        data_format=self.data_format)
    return array_ops.squeeze(outputs, pad_axis)

  def compute_output_shape(self, input_shape):
    input_shape = tensor_shape.TensorShape(input_shape).as_list()
    if self.data_format == 'channels_first':
      steps = input_shape[2]
      features = input_shape[1]
    else:
      steps = input_shape[1]
      features = input_shape[2]
    length = conv_utils.conv_output_length(steps,
                                           self.pool_size[0],
                                           self.padding,
                                           self.strides[0])
    if self.data_format == 'channels_first':
      return tensor_shape.TensorShape([input_shape[0], features, length])
    else:
      return tensor_shape.TensorShape([input_shape[0], length, features])

  def get_config(self):
    config = {
        'strides': self.strides,
        'pool_size': self.pool_size,
        'padding': self.padding,
        'data_format': self.data_format,
    }
    base_config = super(Pooling1D, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))


@keras_export('keras.layers.MaxPool1D', 'keras.layers.MaxPooling1D')
class MaxPooling1D(Pooling1D):

  def __init__(self, pool_size=2, strides=None,
               padding='valid', data_format='channels_last', **kwargs):

    super(MaxPooling1D, self).__init__(
        functools.partial(backend.pool2d, pool_mode='max'),
        pool_size=pool_size,
        strides=strides,
        padding=padding,
        data_format=data_format,
        **kwargs)


@keras_export('keras.layers.AveragePooling1D', 'keras.layers.AvgPool1D')
class AveragePooling1D(Pooling1D):

  def __init__(self, pool_size=2, strides=None,
               padding='valid', data_format='channels_last', **kwargs):
    super(AveragePooling1D, self).__init__(
        functools.partial(backend.pool2d, pool_mode='avg'),
        pool_size=pool_size,
        strides=strides,
        padding=padding,
        data_format=data_format,
        **kwargs)


class Pooling2D(Layer):

  def __init__(self, pool_function, pool_size, strides,
               padding='valid', data_format=None,
               name=None, **kwargs):
    super(Pooling2D, self).__init__(name=name, **kwargs)
    if data_format is None:
      data_format = backend.image_data_format()
    if strides is None:
      strides = pool_size
    self.pool_function = pool_function
    self.pool_size = conv_utils.normalize_tuple(pool_size, 2, 'pool_size')
    self.strides = conv_utils.normalize_tuple(strides, 2, 'strides')
    self.padding = conv_utils.normalize_padding(padding)
    self.data_format = conv_utils.normalize_data_format(data_format)
    self.input_spec = InputSpec(ndim=4)

  def call(self, inputs):
    if self.data_format == 'channels_last':
      pool_shape = (1,) + self.pool_size + (1,)
      strides = (1,) + self.strides + (1,)
    else:
      pool_shape = (1, 1) + self.pool_size
      strides = (1, 1) + self.strides
    outputs = self.pool_function(
        inputs,
        ksize=pool_shape,
        strides=strides,
        padding=self.padding.upper(),
        data_format=conv_utils.convert_data_format(self.data_format, 4))
    return outputs

  def compute_output_shape(self, input_shape):
    input_shape = tensor_shape.TensorShape(input_shape).as_list()
    if self.data_format == 'channels_first':
      rows = input_shape[2]
      cols = input_shape[3]
    else:
      rows = input_shape[1]
      cols = input_shape[2]
    rows = conv_utils.conv_output_length(rows, self.pool_size[0], self.padding,
                                         self.strides[0])
    cols = conv_utils.conv_output_length(cols, self.pool_size[1], self.padding,
                                         self.strides[1])
    if self.data_format == 'channels_first':
      return tensor_shape.TensorShape(
          [input_shape[0], input_shape[1], rows, cols])
    else:
      return tensor_shape.TensorShape(
          [input_shape[0], rows, cols, input_shape[3]])

  def get_config(self):
    config = {
        'pool_size': self.pool_size,
        'padding': self.padding,
        'strides': self.strides,
        'data_format': self.data_format
    }
    base_config = super(Pooling2D, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))


@keras_export('keras.layers.MaxPool2D', 'keras.layers.MaxPooling2D')
class MaxPooling2D(Pooling2D):
  def __init__(self,
               pool_size=(2, 2),
               strides=None,
               padding='valid',
               data_format=None,
               **kwargs):
    super(MaxPooling2D, self).__init__(
        nn.max_pool,
        pool_size=pool_size, strides=strides,
        padding=padding, data_format=data_format, **kwargs)


@keras_export('keras.layers.AveragePooling2D', 'keras.layers.AvgPool2D')
class AveragePooling2D(Pooling2D):

  def __init__(self,
               pool_size=(2, 2),
               strides=None,
               padding='valid',
               data_format=None,
               **kwargs):
    super(AveragePooling2D, self).__init__(
        nn.avg_pool,
        pool_size=pool_size, strides=strides,
        padding=padding, data_format=data_format, **kwargs)


class Pooling3D(Layer):

  def __init__(self, pool_function, pool_size, strides,
               padding='valid', data_format='channels_last',
               name=None, **kwargs):
    super(Pooling3D, self).__init__(name=name, **kwargs)
    if data_format is None:
      data_format = backend.image_data_format()
    if strides is None:
      strides = pool_size
    self.pool_function = pool_function
    self.pool_size = conv_utils.normalize_tuple(pool_size, 3, 'pool_size')
    self.strides = conv_utils.normalize_tuple(strides, 3, 'strides')
    self.padding = conv_utils.normalize_padding(padding)
    self.data_format = conv_utils.normalize_data_format(data_format)
    self.input_spec = InputSpec(ndim=5)

  def call(self, inputs):
    pool_shape = (1,) + self.pool_size + (1,)
    strides = (1,) + self.strides + (1,)

    if self.data_format == 'channels_first':
      # TF does not support `channels_first` with 3D pooling operations,
      # so we must handle this case manually.
      # TODO(fchollet): remove this when TF pooling is feature-complete.
      inputs = array_ops.transpose(inputs, (0, 2, 3, 4, 1))

    outputs = self.pool_function(
        inputs,
        ksize=pool_shape,
        strides=strides,
        padding=self.padding.upper())

    if self.data_format == 'channels_first':
      outputs = array_ops.transpose(outputs, (0, 4, 1, 2, 3))
    return outputs

  def compute_output_shape(self, input_shape):
    input_shape = tensor_shape.TensorShape(input_shape).as_list()
    if self.data_format == 'channels_first':
      len_dim1 = input_shape[2]
      len_dim2 = input_shape[3]
      len_dim3 = input_shape[4]
    else:
      len_dim1 = input_shape[1]
      len_dim2 = input_shape[2]
      len_dim3 = input_shape[3]
    len_dim1 = conv_utils.conv_output_length(len_dim1, self.pool_size[0],
                                             self.padding, self.strides[0])
    len_dim2 = conv_utils.conv_output_length(len_dim2, self.pool_size[1],
                                             self.padding, self.strides[1])
    len_dim3 = conv_utils.conv_output_length(len_dim3, self.pool_size[2],
                                             self.padding, self.strides[2])
    if self.data_format == 'channels_first':
      return tensor_shape.TensorShape(
          [input_shape[0], input_shape[1], len_dim1, len_dim2, len_dim3])
    else:
      return tensor_shape.TensorShape(
          [input_shape[0], len_dim1, len_dim2, len_dim3, input_shape[4]])

  def get_config(self):
    config = {
        'pool_size': self.pool_size,
        'padding': self.padding,
        'strides': self.strides,
        'data_format': self.data_format
    }
    base_config = super(Pooling3D, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))


@keras_export('keras.layers.MaxPool3D', 'keras.layers.MaxPooling3D')
class MaxPooling3D(Pooling3D):

  def __init__(self,
               pool_size=(2, 2, 2),
               strides=None,
               padding='valid',
               data_format=None,
               **kwargs):
    super(MaxPooling3D, self).__init__(
        nn.max_pool3d,
        pool_size=pool_size, strides=strides,
        padding=padding, data_format=data_format, **kwargs)


@keras_export('keras.layers.AveragePooling3D', 'keras.layers.AvgPool3D')
class AveragePooling3D(Pooling3D):

  def __init__(self,
               pool_size=(2, 2, 2),
               strides=None,
               padding='valid',
               data_format=None,
               **kwargs):
    super(AveragePooling3D, self).__init__(
        nn.avg_pool3d,
        pool_size=pool_size, strides=strides,
        padding=padding, data_format=data_format, **kwargs)


class GlobalPooling1D(Layer):
  """Abstract class for different global pooling 1D layers."""

  def __init__(self, data_format='channels_last', **kwargs):
    super(GlobalPooling1D, self).__init__(**kwargs)
    self.input_spec = InputSpec(ndim=3)
    self.data_format = conv_utils.normalize_data_format(data_format)

  def compute_output_shape(self, input_shape):
    input_shape = tensor_shape.TensorShape(input_shape).as_list()
    if self.data_format == 'channels_first':
      return tensor_shape.TensorShape([input_shape[0], input_shape[1]])
    else:
      return tensor_shape.TensorShape([input_shape[0], input_shape[2]])

  def call(self, inputs):
    raise NotImplementedError

  def get_config(self):
    config = {'data_format': self.data_format}
    base_config = super(GlobalPooling1D, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))


@keras_export('keras.layers.GlobalAveragePooling1D',
              'keras.layers.GlobalAvgPool1D')
class GlobalAveragePooling1D(GlobalPooling1D):xx
  def __init__(self, data_format='channels_last', **kwargs):
    super(GlobalAveragePooling1D, self).__init__(data_format=data_format,
                                                 **kwargs)
    self.supports_masking = True

  def call(self, inputs, mask=None):
    steps_axis = 1 if self.data_format == 'channels_last' else 2
    if mask is not None:
      mask = math_ops.cast(mask, backend.floatx())
      mask = array_ops.expand_dims(
          mask, 2 if self.data_format == 'channels_last' else 1)
      inputs *= mask
      return backend.sum(inputs, axis=steps_axis) / math_ops.reduce_sum(
          mask, axis=steps_axis)
    else:
      return backend.mean(inputs, axis=steps_axis)

  def compute_mask(self, inputs, mask=None):
    return None


@keras_export('keras.layers.GlobalMaxPool1D', 'keras.layers.GlobalMaxPooling1D')
class GlobalMaxPooling1D(GlobalPooling1D):

  def call(self, inputs):
    steps_axis = 1 if self.data_format == 'channels_last' else 2
    return backend.max(inputs, axis=steps_axis)


class GlobalPooling2D(Layer):
  """Abstract class for different global pooling 2D layers.
  """

  def __init__(self, data_format=None, **kwargs):
    super(GlobalPooling2D, self).__init__(**kwargs)
    self.data_format = conv_utils.normalize_data_format(data_format)
    self.input_spec = InputSpec(ndim=4)

  def compute_output_shape(self, input_shape):
    input_shape = tensor_shape.TensorShape(input_shape).as_list()
    if self.data_format == 'channels_last':
      return tensor_shape.TensorShape([input_shape[0], input_shape[3]])
    else:
      return tensor_shape.TensorShape([input_shape[0], input_shape[1]])

  def call(self, inputs):
    raise NotImplementedError

  def get_config(self):
    config = {'data_format': self.data_format}
    base_config = super(GlobalPooling2D, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))


@keras_export('keras.layers.GlobalAveragePooling2D',
              'keras.layers.GlobalAvgPool2D')
class GlobalAveragePooling2D(GlobalPooling2D):
  def call(self, inputs):
    if self.data_format == 'channels_last':
      return backend.mean(inputs, axis=[1, 2])
    else:
      return backend.mean(inputs, axis=[2, 3])


@keras_export('keras.layers.GlobalMaxPool2D', 'keras.layers.GlobalMaxPooling2D')
class GlobalMaxPooling2D(GlobalPooling2D):

  def call(self, inputs):
    if self.data_format == 'channels_last':
      return backend.max(inputs, axis=[1, 2])
    else:
      return backend.max(inputs, axis=[2, 3])


class GlobalPooling3D(Layer):
  """Abstract class for different global pooling 3D layers."""

  def __init__(self, data_format=None, **kwargs):
    super(GlobalPooling3D, self).__init__(**kwargs)
    self.data_format = conv_utils.normalize_data_format(data_format)
    self.input_spec = InputSpec(ndim=5)

  def compute_output_shape(self, input_shape):
    input_shape = tensor_shape.TensorShape(input_shape).as_list()
    if self.data_format == 'channels_last':
      return tensor_shape.TensorShape([input_shape[0], input_shape[4]])
    else:
      return tensor_shape.TensorShape([input_shape[0], input_shape[1]])

  def call(self, inputs):
    raise NotImplementedError

  def get_config(self):
    config = {'data_format': self.data_format}
    base_config = super(GlobalPooling3D, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))


@keras_export('keras.layers.GlobalAveragePooling3D',
              'keras.layers.GlobalAvgPool3D')
class GlobalAveragePooling3D(GlobalPooling3D):

  def call(self, inputs):
    if self.data_format == 'channels_last':
      return backend.mean(inputs, axis=[1, 2, 3])
    else:
      return backend.mean(inputs, axis=[2, 3, 4])


@keras_export('keras.layers.GlobalMaxPool3D', 'keras.layers.GlobalMaxPooling3D')
class GlobalMaxPooling3D(GlobalPooling3D):

  def call(self, inputs):
    if self.data_format == 'channels_last':
      return backend.max(inputs, axis=[1, 2, 3])
    else:
      return backend.max(inputs, axis=[2, 3, 4])



AvgPool1D = AveragePooling1D
MaxPool1D = MaxPooling1D
AvgPool2D = AveragePooling2D
MaxPool2D = MaxPooling2D
AvgPool3D = AveragePooling3D
MaxPool3D = MaxPooling3D
GlobalMaxPool1D = GlobalMaxPooling1D
GlobalMaxPool2D = GlobalMaxPooling2D
GlobalMaxPool3D = GlobalMaxPooling3D
GlobalAvgPool1D = GlobalAveragePooling1D
GlobalAvgPool2D = GlobalAveragePooling2D
GlobalAvgPool3D = GlobalAveragePooling3D





