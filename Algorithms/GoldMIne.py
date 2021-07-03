# In this problem it is essential to restore the original grid after changing values to - 1 as we travel multiple paths 
# So that is why we declare the tmp variable and then after the recursion change the grid value back to tmp 
# The last lines (24 - 29) can be compressed in one line ( res = max(res, Helper(...)) ) but for understanding, it has'nt
def GoldMine(grid):
	def Helper(grid, i, j, gold):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] <= 0:
			return gold 
		gold += grid[i][j]
		res, tmp = 0, grid[i][j]
		grid[i][j] = -1 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			res = max(res, Helper(grid, i + dx, j + dy, gold))
		grid[i][j] = tmp 
		return res 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 :
		raise ValueError 
	res = []
	for i in range(m):
		for j in range(n):
			if grid[i][j]:
				res.append(Helper(grid, i, j, 0))
	ans = 0 
	for i in range(len(res)):
		ans = max(ans, res[i])
	return ans 

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print(GoldMine(grid))