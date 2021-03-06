from  heapq import heappop, heappush
def AmazonFresh(allLocations, numDeliveries):
	res = []
	if not allLocations: return -1
	for count, i in enumerate(allLocations):
		if int((i[0]**2 + i[1]**2)**0.5) <= numDeliveries:
			res.append(count)
	if not res : return [[]]
	return [allLocations[i] for i in res]


def AmazonFreshHeap(allLocations, numOfDeliveries):
	heap = []
	for idx, location in enumerate( allLocations ):
	    heappush(heap, (location[0]**2 + location[1]**2, location[0], idx))
	    
	res = []
	while numOfDeliveries != 0:
	    res.append(allLocations[ heappop(heap)[2] ])
	    numOfDeliveries -=1
	if not res : return [[]]
	res.sort(key = lambda x : x[1])
	return res[::-1]


arr = [[1,2], [3,4], [1, -1]]
print(AmazonFreshHeap(arr, 2))