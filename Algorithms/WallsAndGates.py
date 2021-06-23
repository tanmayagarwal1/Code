def WallsAndGates(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return - 1
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0 :
				HelperWall(grid, i, j, 0)
	return grid 

def HelperWall(grid, i, j, count):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] < count:
		return 
	grid[i][j] = count
	nieghbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
	for dx, dy in nieghbours:
		HelperWall(grid, i + dx, j + dy, count + 1)
	return 

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()


grid = [[float('inf'), -1, 0, float('inf')], [float('inf'), float('inf'), float('inf'), -1], \
		[float('inf'), -1, float('inf'), -1], [0, -1, float('inf'), float('inf')]]

printgrid(WallsAndGates(grid))
