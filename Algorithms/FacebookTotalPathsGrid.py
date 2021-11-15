def TotalPathsCount(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q, count = [(0, i) for i in range(n) if grid[0][i] == 0], 0
	for start in q:
		pq = [(start)]
		while pq:
			i, j = pq.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x, y = i + dx, j + dy
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 1: continue 
				elif x == m - 1 : count += 1 
				grid[x][y] = 1
				pq.append((x, y))
	return count 



grid = [[1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1]]
print(TotalPathsCount(grid))

