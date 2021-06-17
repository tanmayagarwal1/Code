def TruncateZero(grid):
	m, n, q = len(grid), len(grid[0]), []
	if m == 0 or n == 0 :
		return - 1
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 0:
				q.append((i, j))
	while q:
		dx, dy  = q.pop(0)
		for i in range(m):
			grid[i][dy] = 0 
		for j in range(n):
			grid[dx][i] = 0 
	return grid

grid = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(TruncateZero(grid))