def HighestPeak(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	dp = [[-1 for _ in range(n)] for _ in range(m)]
	q = []
	for i in range(m):
		for j in range(n):
			if grid[i][j]:
				q.append((i, j))
				dp[i][j] = 0 
	while q:
		i, j = q.pop(0)
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or dp[x][y] != -1:
				continue 
			dp[x][y] = 1 + dp[i][j]
			q.append((x, y))
	return dp

grid = [[0,0,1],[1,0,0],[0,0,0]]
print(HighestPeak(grid)) 