
# The grid here is broken that is, it doesnt form a perfect square/ rectangular grid 
def Diagonalraversal(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	res = []
	for i, row in enumerate(grid):
		for j, num in enumerate(row):
			if len(res) <= i + j:
				res.append([])
			res[i + j].append(num)
	ans = []
	for arr in res:
		for num in reversed(arr):
			ans.append(num)
	return ans 

grid = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
print(Diagonalraversal(grid))