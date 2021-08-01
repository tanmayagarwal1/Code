# i - k <= r <= i + k,
# j - k <= c <= j + k
# Hence row, col = min(i + k, m - 1) and col = min(j + k, n - 1)
# if i - k > 0 and j - k > 0 : conditions 

def BlockSum(grid, k):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	prefix = [[0 for _ in range(n)] for _ in range(m)]
	prefix[0][0] = grid[0][0]
	for i in range(1, m):
		prefix[i][0] += prefix[i - 1][0] + grid[i][0] 
	for i in range(1, n):
		prefix[0][i] += prefix[0][i - 1] + grid[0][i]
	for i in range(1, m):
		for j in range(1, n):
			prefix[i][j] += prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + grid[i][j]

	res = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(m):
		for j in range(n):
			row = min(i + k, m - 1)
			col = min(j + k, n - 1)
			res[i][j] = prefix[row][col]
			if i - k > 0 : res[i][j] -= prefix[i - k - 1][col]
			if j - k > 0 : res[i][j] -= prefix[row][j - k - 1]
			if i - k > 0 and j - k > 0 : res[i][j] += prefix[i - k - 1][j - k - 1]
	return res 

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(BlockSum(grid, k))
	

