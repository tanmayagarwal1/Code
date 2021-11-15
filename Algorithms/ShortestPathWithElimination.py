def ShortestPath(grid, k):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q = [(0, 0, k, 0)]
	seen = set([0, 0, k])
	if k > ((m - 1) + (n - 1)):
		return (m - 1) + (n - 1)
	while q:
		i, j, k, steps = q.pop(0)
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : continue 
			if grid[x][y] == 1 and k > 0 and (x, y, k - 1) not in seen:
				seen.add((x, y, k - 1))
				q.append((x, y, k - 1, steps + 1))
			if grid[x][y] == 0 and (x, y, k) not in seen : 
				if x == m - 1 and y == n - 1  : return steps + 1 
				seen.add((x, y, k))
				q.append((x, y, k, steps + 1))
	return - 1 

grid = 	[[0,0,0],
		 [1,1,0],
		 [0,0,0],
		 [0,1,1],
		 [0,0,0]]
k = 1

print(ShortestPath(grid, k))

