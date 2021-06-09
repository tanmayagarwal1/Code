
'''This is my variation of flood fill. Instead of starting from source we start from the top'''
def FloodFill(grid, newCol):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				HelperFill(grid, i, j, newCol)
				break 
	printgrid(grid)
	return

def HelperFill(grid, i, j, color):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
		return 
	grid[i][j] = color
	neighbour = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbour:
		HelperFill(grid, i + dx, j + dy, color)
	return 

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()

grid = [[1,1,1],[1,1,0],[1,0,1]]
FloodFill(grid, 2)
