def Lights(n, lamps, queries):
	if not n or not lamps : return -1 
	grid, res = [[1 for _ in range(n)] for _ in range(n)], []
	neighbours = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (1, -1), (-1, 1), (-1, -1))

	for i in lamps: # Turning the lamps ON
		grid[i[0]][i[1]] = -1
		for dx, dy in neighbours:
			x = i[0] + dx
			y = i[1] + dy
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]): 
				continue 
			directionaldfs(grid, x, y, dx, dy)
			grid[x - dx][y - dy] = 0
	for i, j in queries:
		if not grid[i][j]:
			res.append(1)
		else:
			res.append(0)
		TurnOff(grid, i, j)
	return res

def directionaldfs(grid, i, j, dx, dy):
	grid[i][j] = 0 
	x = i + dx
	y = j + dy
	if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
		return 
	directionaldfs(grid, x, y, dx, dy)
			
def TurnOff(grid, i, j):
	neighbours = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (1, -1), (-1, 1), (-1, -1))
	for dx, dy in neighbours:
		x = i + dx
		y = j + dy
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
			continue
		grid[x][y] = 1 

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()

lamps = [[0,0],[0,1],[0,4]]
queries = [[0,0],[0,1],[0,2]]

print(Lights(5, lamps, queries))
