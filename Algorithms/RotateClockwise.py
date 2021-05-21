def Rotate(grid): # Clockwise
	n = len(grid)
	grid.reverse()
	for i in range(n):
		for j in range(i+1, n):
			grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
	printsol(grid)

def printsol(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end= ' ')
		print()

grid = [[1,2,3],
		[4,5,6],
		[7,8,9]]

Rotate(grid)
