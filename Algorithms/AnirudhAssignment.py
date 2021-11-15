def MinDistance(x, y):
	def InitialiseTable(grid):
		rowMax, colMax = len(x) + 1, len(y) + 1
		while rowMax >= 0:
			for char in x[::-1]:
				dp[rowMax][0] = char 
				rowMax -= 1
			break 

		while colMax >= 0 : 
			for char in y[::-1]:
				dp[0][colMax] = char 
				colMax -= 1
			break 

		tmp = 1
		for i in range(len(x) + 1):
			dp[tmp][1] = i 
			tmp += 1 

		tmp = 1 
		for i in range(len(y) + 1):
			dp[1][tmp] = i 
			tmp += 1 

	def printTable(grid):
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				print(grid[i][j], end = " ")
			print()

	m, n = len(x), len(y)
	if m == 0 or n == 0 : raise ValueError 
	dp = [[" " for _ in range(n + 2)] for _ in range(m + 2)]
	InitialiseTable(dp)
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] != y[j - 1]:
				dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])
			else:
				dp[i + 1][j + 1] = dp[i][j]
	printTable(dp)

MinDistance("sets", "reset")