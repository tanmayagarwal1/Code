def FloodFill(grid, sr, sc, newCol):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	if grid[sr][sc] == newCol : 
		printgrid(grid)
		return 
	old = grid[sr][sc]
	q = [(sr, sc)]
	while q : 
		i, j = q.pop(0)
		grid[i][j] = newCol
		neighbours = ((0,1), (0,-1), (1,0), (-1,0))
		for dx, dy in neighbours:
			x = i + dx
			y = j + dy
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != old:
				continue 
			q.append((x, y))
	printgrid(grid)


def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
printgrid(grid)
#FloodFill(grid, 1, 1, 2)


