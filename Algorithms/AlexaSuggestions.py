import math
def AlexaSuggestions(arr, target):
	if len(arr) == 0 or len(arr[0]) == 0:
		return -1 
	res = []
	for count, i in enumerate(arr):
		if math.floor((i[0]**2 + i[1]**2)**0.5) <= target:
			res.append(count)
	return [arr[i] for i in res]

arr = [[1, 2], [3, 4], [1, -1]]
target = 2
print(AlexaSuggestions(arr, target))