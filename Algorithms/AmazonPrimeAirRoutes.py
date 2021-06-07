def PrimeAirRoutes(forwardRouteList, returnRouteList, MaxTravelDist): # Change the names of a few local variables before submission
	# forwardRouteList and returnRouteList are lists of lists 
	if not forwardRouteList or not returnRouteList: return -1
	res = []
	for i in forwardRouteList:
		for j in returnRouteList:
			if i[1] + j[1] <= MaxTravelDist:
				res.append([i[0], j[0], i[1] + j[1]])
	if not res: return [[]]  
	else: global_max = max([i[2] for i in res])
	return [[i[0], i[1]] for i in res if i[2] == global_max]


ins = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
outs = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
target = 10000
print(PrimeAirRoutes(ins, outs, target))