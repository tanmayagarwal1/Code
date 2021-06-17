def MineSweeper(grid, click):
	i, j = click 
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1))

	def isAvailable(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
			return False 
		return True 

	def HelperSweep(grid, i, j):
		if not isAvailable(grid, i, j) or grid[i][j] == 'E':
			return 
		count = 0 
		for dx, dy in neighbours:
			if isAvailable(grid, i + dx, j + dy) and grid[i + dx][j + dy] == 'M':
				count += 1
		if count:
			grid[i][j] = count 
		else:
			grid[i][j] = 'B'
			for dx, dy in neighbours:
				HelperSweep(grid, i + dx, j + dy)

	if grid[i][j] == 'M':
		grid[i][j] = "X"
	elif grid[i][j] == 'E':
		HelperSweep(grid, i, j)
	return grid 

grid = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
click = [1, 2]
print(MineSweeper(grid, click))


