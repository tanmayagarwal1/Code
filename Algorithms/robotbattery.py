def Robot(grid, battery):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return -1
	if not grid[0][0] : count = 0
	battery = battery//2
	Dfs(grid, 0, 0)
	q = [(0, 0)]
	while q :
		i, j = q.pop(0)
		count += 1
		battery -= 1
		if battery <= 1 : return count 
		nieghbours = ((0, 1), (0,-1), (1,0), (-1,0))
		for dx, dy in nieghbours:
			x = i + dx
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != -1:
				continue 
			grid[i][j] = 1
			q.append((x, y))
	return count

def Dfs(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 0:
		return 
	grid[i][j] = - 1
	nieghbours = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in nieghbours:
		Dfs(grid, i + dx, j + dy)
	return 



grid = [[0, 0, 0], 
		[0, 1, 0], 
		[0, 0, 0]]
print(Robot(grid, 8))
