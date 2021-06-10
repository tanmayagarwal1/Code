def DiagonalTraversal(grid):
	if len(grid) == 0 or len(grid[0]) == 0:
		return - 1
	d, res = dict(), []
	m, n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(len(grid[i])):
			if i + j in d.keys():
				d[i + j].append(grid[i][j])
			else:
				d[i + j] = [grid[i][j]]
	for i in d.keys():
		if i & 1 == 0:
			[res.append(x) for x in d[i][::-1]]
		else:
			[res.append(x) for x in d[i]]
	return res



grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(DiagonalTraversal(grid))
