import math
def AlexaSuggestions(allLocations, numRestaurants):
	if len(allLocations) == 0:
		return -1 
	res = []
	for count, i in enumerate(allLocations):
		if math.floor((i[0]**2 + i[1]**2)**0.5) <= numRestaurants:
			res.append(count)
	return [allLocations[i] for i in res]

arr = [[1, 2], [3, 4], [1, -1]]
target = 2
print(AlexaSuggestions(arr, target))