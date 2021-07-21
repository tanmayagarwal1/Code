def NumIslands(grid):
	def Helper(grid, i, j):
		q = [(i, j)]
		while q:
			i, j = q.pop(0)
			grid[i][j] = - 1
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
					continue 
				q.append((x, y))
		return 1 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	count = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1: 
				count += Helper(grid, i, j)
	return count 

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(NumIslands(grid))