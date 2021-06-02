def DeviceApplicationPair(foregroundAppList, backgroundAppList, deviceCapacity):
	if len(foregroundAppList) == 0 or len(foregroundAppList[0]) == 0 :
		return -1 
	res = []
	for i in foregroundAppList:
		for j in backgroundAppList:
			if i[1] + j[1] <= deviceCapacity:
				res.append([i[0], j[0], i[1] + j[1]])
	if not res: return [[]]
	global_max = max([i[2] for i in res])
	return [[i[0], i[1]] for i in res if i[2] == global_max]

ins = [[1, 3], [2, 5], [3, 7], [4, 10]]
outs = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
print(DeviceApplicationPair(ins, outs, target))