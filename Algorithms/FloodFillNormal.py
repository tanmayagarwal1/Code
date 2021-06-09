def FloodFill(grid, sr, sc, newCol):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	if grid[sr][sc] == newCol : 
		printgrid(grid)
		return 
	HelperFill(grid, sr, sc, newCol, grid[sr][sc])
	printgrid(grid)
	return

def HelperFill(grid, i, j, color, curr_col):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != curr_col:
		return 
	grid[i][j] = color
	neighbour = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbour:
		HelperFill(grid, i + dx, j + dy, color, curr_col)
	return 

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()

grid = [[0,0,0],[0,1,1]]
FloodFill(grid, 1, 1, 1)


