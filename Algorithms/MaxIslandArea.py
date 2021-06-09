def CountIsland(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	#grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	q = []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				x = HelperCount(grid, i, j)
				q.append(x)
	res = q[0]
	for i in range(len(q)):
		res = max(res, q[i])
	return res 

def HelperCount(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1 :
		return 0
	grid[i][j] = "#"
	phi = HelperCount(grid, i + 1, j) 
	psi = HelperCount(grid, i, j + 1)
	mu  = HelperCount(grid, i - 1, j)
	nu  = HelperCount(grid, i, j - 1)
	return phi + psi + mu + nu + 1

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,1,0,0,0],
		[0,1,1,0,1,0,0,0,0,0,0,0,0],
		[0,1,0,0,1,1,0,0,1,0,1,0,0],
		[0,1,0,0,1,1,0,0,1,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,0,0],
		[0,0,0,0,0,0,0,1,1,1,0,0,0],
		[0,0,0,0,0,0,0,1,1,0,0,0,0]]



print(CountIsland(grid))
