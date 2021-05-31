import math
def AmazonFresh(arr, target):
	res = []
	if not arr: return -1
	for count, i in enumerate(arr):
		if math.floor((i[0]**2 + i[1]**2)**0.5) <= target:
			res.append(count)
	return [arr[i] for i in res]


arr = [[1,2], [3,4], [1, -1]]
print(AmazonFresh(arr, 2))