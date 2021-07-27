def MaxDistanceFromLand(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
	if not q or q == m * n : return -1 
	dist = 0 
	while q :
		dist += 1
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 0:
					continue 
				grid[x][y] = 1
				q.append((x, y))
	return dist - 1

grid = [[1, 0, 0], 
		[0, 0, 0], 
		[0, 0, 0]]

print(MaxDistanceFromLand(grid))