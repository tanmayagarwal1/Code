def MaximumNonNegativeProduct(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	dp_min = [[1 for _ in range(n)] for i in range(m)]
	dp_max = [[1 for _ in range(n)] for i in range(m)]
	dp_min[0][0] = grid[0][0]
	dp_max[0][0] = grid[0][0]
	for i in range(1, m):
		dp_min[i][0] = dp_min[i - 1][0] * grid[i][0]
		dp_max[i][0] = dp_max[i - 1][0] * grid[i][0]
	for i in range(1, n):
		dp_min[0][i] = dp_min[0][i - 1] * grid[0][i]
		dp_max[0][i] = dp_max[0][i - 1] * grid[0][i]
	for i in range(1, m):
		for j in range(1, n):
			if grid[i][j] > 0:
				dp_max[i][j] = max(dp_max[i - 1][j], dp_max[i][j - 1]) * grid[i][j]
				dp_min[i][j] = min(dp_min[i - 1][j], dp_min[i][j - 1]) * grid[i][j]
			else:
				dp_max[i][j] = min(dp_min[i - 1][j], dp_min[i][j - 1]) * grid[i][j]
				dp_min[i][j] = max(dp_max[i - 1][j], dp_max[i][j - 1]) * grid[i][j]
	return dp_max[m - 1][n - 1] %(10**9 + 7) if dp_max[m - 1][n - 1] >= 0 else -1

grid = [[1,-2,1],
       [1,-2,1],
       [3,-4,1]]

print(MaximumNonNegativeProduct(grid))

# Maintain two dp arrays that is max and min as there are positive and negative numbers in the matrix 
# If the cell is positive the dp_max = max(dp_max(up), dp_max(left)) * current grid and for dp_min its gonna be min 
# But if it is negative then it is reversed dp_max = min(dp_min(up), dp_min(left)) and so for dp_min 
# In the end the result is stroed at last cell of dp_max 