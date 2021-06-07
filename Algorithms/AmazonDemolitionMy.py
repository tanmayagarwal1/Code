def DemolitionRobot(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return -1 
	if grid[0][0] == 9 : return 0
	end_x, end_y = findTarget(grid)
	for i in range(1, m):
		if grid[i][0] == 1:
			grid[i][0] = grid[i -1][0] + grid[i][0]
		else:
			grid[i][0] = float('inf')
	for i in range(1, n):
		if grid[0][i] == 1:
			grid[0][i] = grid[0][i - 1] + grid[0][i]
		else:
			grid[0][i] = float('inf')

	for i in range(1, m):
		for j in range(1, n):
			if not grid[i][j] : grid[i][j] = float('inf')
			elif grid[i][j]:
				if IsLeftPerimeter(grid, i, j) and IsRightPerimeter(grid, i, j):
					grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
				elif IsLeftPerimeter(grid, i, j) and not IsRightPerimeter(grid, i, j):
					grid[i][j] = grid[i][j - 1] + grid[i][j]
				elif IsRightPerimeter(grid, i, j) and not IsLeftPerimeter(grid, i, j):
					grid[i][j] = grid[i - 1][j] + grid[i][j]
				if not IsLeftPerimeter(grid, i, j) and not IsRightPerimeter(grid, i, j):
					grid[i][j] = float('inf')
	printgrid(grid)
	return MinDistTarget(grid, end_x, end_y)

def IsLeftPerimeter(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == float('inf'):
		return False
	if j == 0 and grid[i][j] != float('inf'):
		return True 
	return IsLeftPerimeter(grid, i, j - 1)

def IsRightPerimeter(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] == float('inf'):
		return False
	if i == 0 and grid[i][j] != float('inf'):
		return True 
	return IsRightPerimeter(grid, i - 1, j)

def findTarget(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 9:
				grid[i][j] = float('inf')
				return i, j
	return i, j

def MinDistTarget(grid, i, j):
	neighbours, res = ((0,1), (0,-1), (1,0), (-1,0)), float('inf')
	for dx, dy in neighbours:
		x, y = i + dx, j + dy 
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
			continue 
		else:
			res = min(res, grid[x][y])
	return res

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == float('inf'):
				print('X', end = ' ')
			else:
				print(grid[i][j] , end = ' ')
		print()

grid = [[1, 1, 1, 0], [1, 1, 9, 0], [1, 1, 1, 1], [1, 1, 1, 1]] # 3
grid1 = [[1,0,0], [1,0,0], [1,9,1]] # 3
grid2 = [[1,0,0], [1,9,1], [1,0,0]] # 2
grid3 = [[1,1,0], [9,1,0], [1,0,1]] # 1
grid4 = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1], [1, 9, 1, 1]] # 4
grid5 = [[1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 9, 1]] # 5
print(DemolitionRobot(grid5))

