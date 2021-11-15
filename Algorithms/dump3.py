import sys
 

def MinDistance(sti1, sti2):
	def printTable(grid):
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				print("{}{}".format(grid[i][j], "|"), end = " ")
			print(" ")
	m, n = len(sti1), len(sti2)
	if m == 0 or n == 0 : raise ValueError 
	dp = [[0 for _ in range(n + 2)] for _ in range(m + 2)]
	tmp = n + 1
	while tmp >= 0:
		for char in sti2[::-1]:
			dp[0][tmp] = char 
			tmp -= 1 
		break 
	tmp = m + 1 
	while tmp >= 0 : 
		for char in sti1[::-1]:
			dp[tmp][0] = char 
			tmp -= 1 
		break  
	tmp = 1
	for i in range(m + 1):
		dp[tmp][1] = i 
		tmp += 1

	tmp = 1
	for i in range(n + 1):
		dp[1][tmp] = i 
		tmp += 1
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if sti1[i - 1] != sti2[j - 1]:
				dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])
			else:
				dp[i + 1][j + 1] = dp[i][j]
	printTable(dp)



#MinDistance("sets", "reset")


def MinDistance2(x, y):
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
	dp = [[0 for _ in range(n + 2)] for _ in range(m + 2)]
	InitialiseTable(dp)
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] != y[j - 1]:
				dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])
			else:
				dp[i + 1][j + 1] = dp[i][j]
	printTable(dp)

MinDistance2("sets", "reset")