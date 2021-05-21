import math
import numpy as np 
import matplotlib.pyplot as plt 
def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a
def relu(x):
	q = []
	for item in x:
		q.append(max(0,item))
	return q
x = np.arange(-10, 10, 0.2)
sig = sigmoid(x)
relu = relu(x)
fig, ax = plt.subplots()
ax.plot(x, sig, 'k-', label='sigmoid', color = 'red')
ax.plot(x, relu, 'k:', label='relu', color = 'blue')
#ax.plot(x, softmax, 'k--', label='softmax', color = 'yellow')

legend = ax.legend(loc='upper center', shadow=True)

# Put a nicer background color on the legend.

plt.show()