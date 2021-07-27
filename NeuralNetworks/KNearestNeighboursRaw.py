
def PredictLabel(test_feature, inputs, k):
	k_nearest_neighbours = findKNearestNeighbours(test_feature, inputs, k)
	label_key = 'is_intrusive'
	k_nearest_labels = [inputs[pid][label_key] for pid in k_nearest_neighbours]
	return round(sum(k_nearest_labels) / k)


def findKNearestNeighbours(features, input, k):
	def get_euclidian_distance(test_feature, inp_feature):
		squared_dist = []
		for i in range(len(test_feature)):
			# Assume that both test_feature and imp_feature have same length
			tmp = (test_feature[i] - inp_feature[i]) **2 
			squared_dist.append(tmp)
		return (sum(squared_dist))**0.5

	dist = {}
	for pid, dictt in input.items():
		distance = get_euclidian_distance(features, dictt['features'])
		dist[pid] = distance 
	return sorted(dist, key = lambda x : x[1])[:k]






# Input = {process_id : 
#				{'features' : [int list], 'label' : [0 or 1]}
#		  }