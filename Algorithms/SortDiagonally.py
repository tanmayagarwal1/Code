def SortMatrixDiagonally(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	d = {}
	for i in range(m):
		for j in range(n):
			if i - j in d:
				d[i - j].append(grid[i][j])
			else:
				d[i - j] = [grid[i][j]]
	for k in d :
		d[k].sort(reverse = True)

	for i in range(m):
		for j in range(n):
			grid[i][j] = d[i - j].pop()
	return grid 

grid = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print(SortMatrixDiagonally(grid))