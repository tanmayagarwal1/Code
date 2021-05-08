def ObstacleAvoider(grid):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0 or grid[0][0]==1:
		return 0
	dp = [[0 for _ in range(n)]for _ in range(m)]
	for i in range(n):
		if not grid[0][i] :
			dp[0][i] = 1
	for i in range(m):
		if  not grid[i][0]:
			dp[i][0]=1 
	for i in range(1,m):
		for j in range(1,n):
			if grid[i][j] : continue 
			dp[i][j] = dp[i-1][j]+dp[i][j-1]
	return dp[m-1][n-1]




obstacleGrid = [[0],[1]]



print(ObstacleAvoider(obstacleGrid))