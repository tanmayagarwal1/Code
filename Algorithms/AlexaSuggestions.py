def AlexaSuggestions(allLocations, numRestaurants):
	if len(allLocations) == 0:
		return -1 
	res = []
	for count, i in enumerate(allLocations):
		if int((i[0]**2 + i[1]**2)**0.5) <= numRestaurants:
			res.append(count)
	return [allLocations[i] for i in res]

from heapq import heappop, heappush
def AlexaSugeestionsHeap(allLocations, numRestaurants):
	heap = []
	for idx, location in enumerate( allLocations ):
	    heappush(heap, (location[0]**2 + location[1]**2, location[0], idx))
	    
	res = []
	while numRestaurants != 0:
	    res.append(allLocations[ heappop(heap)[2] ])
	    numRestaurants -=1
	res.sort(key = lambda x : x[1])
	return res

arr = [[1, 2], [3, 4], [1, -1]]
target = 2
print(AlexaSuggestions(arr, target))