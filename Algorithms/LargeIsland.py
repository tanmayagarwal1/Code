def MaxIsland(grid):
	def Helper(grid, i, j, idx):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return 0
		grid[i][j] = idx 
		Phi = Helper(grid, i + 1, j, idx)
		Psi = Helper(grid, i, j + 1, idx)
		Mu  = Helper(grid, i, j - 1, idx)
		Nu  = Helper(grid, i - 1, j, idx)
		return Phi + Psi + Mu + Nu + 1

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	idx = 2 
	d = {0 : 0}
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1 :
				d[idx] = Helper(grid, i, j, idx)
				idx += 1
	res = max(d.values())
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 0 :
				possible = set()
				neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
				for dx, dy in neighbours:
					x = i + dx 
					y = j + dy 
					if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
						continue 
					possible.add(grid[x][y])
				res = max(res, sum(d[area] for area in possible) + 1)
	return res 




grid = [[1,1],[1,0]]
print(MaxIsland(grid))