import collections
def maxSeatAllocation(n, reserved):
	if not reserved : raise ValueError 
	d = {}
	for i, j in reserved:
		if i not in d :
			d[i] = set()
		if j in list(range(2, 6)):
			d[i].add(0)
		if j in list(range(4, 8)):
			d[i].add(1)
		if j in list(range(6, 10)):
			d[i].add(2)
	res = 2 * n 
	for i in d:
		if len(d[i]) == 3 :
			res -= 2
		elif len(d[i]) > 0:
			res -= 1
	return res 


n = 3
reserved = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
print(maxSeatAllocation(n, reserved))
