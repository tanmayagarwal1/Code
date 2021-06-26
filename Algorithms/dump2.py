def SubIslands(grid, matrix):
	def Helper(grid, i, j, seen):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return 
		grid[i][j] = -1 
		seen.add((i, j))
		neighbours = ((0, 1), (1, 0), (-1, 0), (0, -1))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, seen)
		return 

	if not grid or not matrix : raise ValueError 
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				Helper(grid, i, j, set())

	res = 0 
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				seen = set()
				Helper(matrix, i, j, seen)
				if all(grid[dx][dy] == - 1 for dx, dy in seen):
					res += 1
	return res 

try : 
	grid = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
	gridd = 0 
	print(SubIslands(grid, gridd))

except ValueError:
	print("Empty Value Specified")