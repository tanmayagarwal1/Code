def ispathCrossing(path):
	if not path : raise ValueError 
	d = {'N' : (0, 1), 'S' : (0, -1), 'E' : (1, 0), 'W' : (-1, 0)}
	curr = (0, 0)
	res = {curr}
	for direction in path:
		curr = (curr[0] + d[direction][0], curr[1] + d[direction][1])
		if curr in res : return True 
		res.add(curr)
	return False

path = 'NES'
print(ispathCrossing((path)))

