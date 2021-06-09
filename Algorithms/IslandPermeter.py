'''  Always remeber the permiter = 4 * 1 but if connected its 2* number of connected. Here in the program the var area is just
	 a place holder and nothing else. '''
 
def IslandPerimeter(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return - 1
	area, connect = 0 , 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] : 
				area += 1
				if i > 0 and grid[i - 1][j] : connect += 1
				if j > 0 and grid[i][j - 1] : connect += 1

	return (area*4) - (2*connect)

grid = [[0,1,0,0],
		[1,1,1,0],
		[0,1,0,0],
		[1,1,0,0]]
print(IslandPerimeter(grid))