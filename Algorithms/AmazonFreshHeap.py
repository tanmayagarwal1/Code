from heapq import heappop, heappush
def AmazonFresh(allLocations, numOfDeliveries):
	heap = []
	for idx, location in enumerate( allLocations ):
	    heappush(heap, (location[0]**2 + location[1]**2, location[0], idx))
	    
	res = []
	while numOfDeliveries != 0:
	    res.append(allLocations[ heappop(heap)[2] ])
	    numOfDeliveries -=1
	res.sort(key = lambda x : x[1])
	return res

arr = [[1,2], [3,4], [1, -1]]
print(AmazonFresh(arr, 2))