def MineSweeper(grid, clicks):
	i, j = clicks
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 :
		return - 1
	if grid[i][j] == "M":
		grid[i][j] = "X"
	elif grid[i][j] == "E":
		dfs(grid, i, j)
	return grid 

def dfs(grid, i, j):
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
	if not Available(grid, i, j) or grid[i][j] != "E":
		return 
	count = 0 
	for dx, dy in neighbours:
		if Available(grid, i + dx, j + dy) and grid[i + dx][j + dy] == "M":
			count += 1
	if count:
		grid[i][j] = count 
	else:
		grid[i][j] = "B"
		for dx, dy in neighbours:
			dfs(grid, i + dx, j + dy)
	 

def Available(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
		return False 
	return True 


grid = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
print(MineSweeper(grid, click))

