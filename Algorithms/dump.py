def Lcs(x,y):
	m = len(x)
	n = len(y)
	if m ==0 or n ==0:
		return -1 
	dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
	for i in range(1, m+1):
		for j in range(1, n+1):
			if x[i-1] == y[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[m][n]

def MinimumCost(grid, x, y):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return -1 
	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[0][0] = grid[0][0]
	for i in range(1, n):
		dp[0][i] = dp[0][i-1] + grid[0][i]
	for i in range(1, m):
		dp[i][0] = dp[i-1][0] + grid[i][0]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + grid[i][j]
	return dp[x][y]

def UniquePath(grid):
	m = len(grid)
	n = len(grid[0])
	if m ==0 or n == 0 :
		return -1 
	dp = [[1 for _ in range(n)]for _ in range(m)]
	for i in range(1, m):
		for j in range(1,n):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
	return dp[m-1][n-1]

def regularexpression(sti, pattern):
	m = len(sti)
	n = len(pattern)
	if m ==0 or n == 0:
		return -1 
	dp = [[False for _ in range(n+1)]for _ in range(m+1)]
	dp[0][0] = True 
	for i in range(1, n+1):
		if pattern[i-1] == '*':
			dp[0][i] = dp[0][i-2]
	for i in range(1, m+1):
		for j in range(1, n+1):
			if pattern[j-1] == "." or sti[i-1] == pattern[j-1]:
				dp[i][j] = dp[i-1][j-1]
			if pattern[j-1] == "*":
				dp[i][j] = dp[i][j-2]
				if pattern[j-2] == "." or sti[i-1] == pattern[j-2]:
					dp[i][j] = dp[i-1][j]
	return dp[m][n]

def TrainTickets(days, prices):
	dp = [-1 for _ in range(366)]
	for day in days:
		dp[day] = 0
	dp[0] = 0 
	for i in range(1, 366):
		if dp[i] == -1:
			dp[i] = dp[i-1]
		else:
			dp[i] = min( dp[i-1]+prices[0], 
						 dp[max(i-7, 0)] + prices[1],
						 dp[max(i-30, 0)] + prices[2])
	return dp[365]

def CoinChange(coins, amount):
	dp = [float('inf') for _ in range(amount+1)]
	dp[0] = 0
	for i in range(1, amount+1):
		for coin in coins:
			if i - coin >= 0:
				dp[i] = min(dp[i], dp[i-coin] + 1)
	return dp[-1]

def Permutations(arr):
	if len(arr) == 0:
		return []
	res = []
	Permutator(arr, [], res)
	return res 

def Permutator(arr, path, res):
	if not arr:
		res.append(path)
	for i in range(len(arr)):
		Permutator(arr[:i] + arr[i+1 :], path + [arr[i]], res)
def Combinations(arr, target):
	if len(arr) == 0:
		return -1 
	res = []
	Combinator(arr, target, 0, [], res)
	return res 
def Combinator(arr, target, index, path, res):
	if target < 0:
		return 
	if target == 0:
		res.append(path)
	for i in range(index, len(arr)):
		Combinator(arr, target - arr[i], i, path + [arr[i]], res)

def Subsets(arr):
	if len(arr) == 0:
		return 
	solutions = [[]]
	for i in arr:
		solutions += [current + [i] for current in solutions]
	return solutions 

def Subsets2(arr):
	return [[arr[i] for i in range(len(arr)) if bit & 1<<i != 0]for bit in range(1<<len(arr))]
def NextClosestTime(time):
	h, m = time.split(':')
	m = m[0:2]
	minutes = int(h)* 60 + int(m)
	for i in range(minutes+1, minutes + 1441):
		temp = i % 1440
		h, m = temp//60 , temp%60
		NextTime = "{:02d}:{:02d}".format(h, m)
		if set(NextTime) <= set(time):
			if int(NextTime[0:2]) < 12:
				return NextTime + " AM"
			else:
				return NextTime + " PM"


print(CoinChange([1,2,3,4], 10))      