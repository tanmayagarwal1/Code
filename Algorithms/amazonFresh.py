def AmazonFresh(allLocations, numDeliveries):
	res = []
	if not allLocations: return -1
	for count, i in enumerate(allLocations):
		if int((i[0]**2 + i[1]**2)**0.5) <= numDeliveries:
			res.append(count)
	return [allLocations[i] for i in res]


arr = [[1,2], [3,4], [1, -1]]
print(AmazonFresh(arr, 2))