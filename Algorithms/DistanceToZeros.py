def TruncateWithDistanceToZero(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q = []
	visited = set()
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 0 : 
				q.append((i, j))
	while q:
		i, j = q.pop(0)
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y)in visited or grid[x][y] != 1 :
				continue 
			grid[x][y] = grid[i][j] + 1
			visited.add((x, y))
			q.append((x, y))
	return grid 

grid = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(TruncateWithDistanceToZero(grid))
