def Reshape(grid, r, c):
	if r * c != len(grid) * len(grid[0]) : return grid 
	val = [num for row in grid for num in row]
	ans = [[None for _ in range(c)] for _ in range(r) ]
	x = 0 
	for i in range(r):
		for j in range(c):
			ans[i][j] = val[x]
			x += 1
	return ans

mat = [[1,2],[3,4]]
r = 1
c = 4
print(Reshape(mat, r, c))