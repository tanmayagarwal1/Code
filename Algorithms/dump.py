def Robot(grid, battery):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return - 1
	if not grid[0][0] : count = 1
	battery = battery//2 - 1
	Dfs(grid, 0, 0, count, battery)
	printgrid(grid)

def Dfs(grid, i, j, count, battery):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 0 or battery == 0:
		return 0 
	grid[i][j] = - 1
	Phi = Dfs(grid, i, j + 1, count, battery - 1)
	Psi = Dfs(grid, i + 1, j, count, battery - 1)
	mu  = Dfs(grid, i, j - 1, count, battery - 1)
	nu  = Dfs(grid, i - 1, j, count, battery - 1)
	return Phi + Psi + mu + nu + 1 

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Robot(grid, 8))