def PrimeAirRoutes(ins, outs, target):
	# ins and outs are lists of lists 
	res = []
	for i in ins:
		for j in outs:
			if i[1] + j[1] <= target:
				res.append([i[0], j[0], i[1] + j[1]])
	if not res: return -1 
	else: global_max = max([i[2] for i in res])
	return [[i[0], i[1]] for i in res if i[2] == global_max]


ins = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
outs = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
target = 10000
print(PrimeAirRoutes(ins, outs, target))