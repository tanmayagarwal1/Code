def LongestCommonSubsequence(x, y):
	m, n = len(x), len(y)
	if m == 0 or n == 0:
		return - 1
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] == y[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + 1
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
	return dp[m][n]

def LongestPalindromicSubsequence(sti): # Reverse the string and pass it through Lcs 
	x = sto[::-1]
	return LongestCommonSubsequence(sti, x)

def LongestIncresingSubsequence(arr): # Sort the array, remove the duplicates and pass through Lcs. Use same logic for a string
	arr.sort()
	q, s = [], set()
	for num in arr:
		if num not in s:
			s.add(num)
			q.append(num)
		else:
			continue 
	return LongestCommonSubsequence(arr, q)

def RegularExpression(sti, pattern):
	m, n = len(sti), len(pattern)
	if m == 0 or n == 0:
		return - 1
	dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
	dp[0][0] = True 
	for i in range(1, n + 1):
		if pattern[i - 1] == '*':
			dp[0][i] = dp[0][i - 2]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if pattern[j - 1] == '.' or sti[i - 1] == pattern[j - 1]:
				dp[i][j] = dp[i- 1][j - 1]
			elif pattern[j - 1] == '*':
				dp[i][j] = dp[i][j - 2]
				if pattern[j - 2] == '.' or sti[i - 1] == pattern[j - 2]:
					dp[i][j] = dp[i - 1][j]
	return dp[m][n]

def UniquePaths(m, n):
	if m == 0 or n == 0:
		return - 1
	dp = [[1 for _ in range(n)] for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

	return dp[m - 1][n - 1]

def UniquePaths2(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	dp = [[0 for _ in range(n)] for _ in range(m)]
	if not grid[0][0] : dp[0][0] = 1
	for i in range(1, m):
		if not grid[i][0] : dp[i][0] = 1

	for i in range(1, n):
		if not grid[0][i] : dp[0][i] = 1

	for i in range(1, m):
		for j in range(1, n):
			if grid[i][j]:
				continue
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

	return dp[m - 1][n - 1]

def MainimumCostPath(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[0][0] = grid[0][0]
	for i in range(1, m):
		dp[i][0] = dp[i - 1][0] + grid[i][0]
	for i in range(1, n):
		dp[0][i] = dp[0][i - 1] + grid[0][i]

	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = min(dp[i][j] + dp[i - 1][j], dp[i][j] + dp[i][j - 1]) + grid[i][j]

	return dp[m - 1][n - 1]

def Water_collector(heights):
	a = np.array(heights)
	global_max = np.argmax(heights)
	return np.sum(run_max(a[:global_max]) - a[:global_max], dtype = np.int64) + \
			np.sum(run_max(a[:global_max:-1]) - a[:global_max:-1], dtype = np.int64)

def eggs_max(f, n):
	dp = [[0 for _ in range(n + 1)] for _ in range(f + 1)]
	for i in range(1, f + 1):
		for j in range(1, n + 1):
			dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1
		if dp[i][j] >= f : return i 


def TrainTix(days, cost):
	dp = [-1 for _ in range(366)]
	dp[0] = 0 
	for day in days : 
		dp[day] = 0 
	for i in range(1, 366):
		if dp[i] == -1:
			dp[i] = dp[i - 1]
		else:
			dp[i] = min(dp[i - 1] + cost[0], dp[max(i - 7, 0)] + cost[1], dp[max(i - 30, 0)] + cost[2])
	return dp[365]

def CoinChange(coins, ammount):
	dp = [float('inf') for _ in range(ammount + 1)]
	dp[0] = 0 
	for i in range(1, ammount + 1):
		for coin in coins:
			if dp[i - coin] >= 0 :
				dp[i] = min(dp[i], dp[i - coin] + 1)
	return dp[ammount]

def WordBreak(sti, words):
	if len(sti) == 0 :
		return - 1
	dp = [True] + [False for _ in range(len(sti))]
	for i in range(len(sti) + 1):
		for word in words:
			if sti[:i].endswith(word):
				dp[i] = dp[i] or dp[i - len(word)]
	return dp[len(sti)]

def CanPartitionEqualSum(arr):
	if len(arr) == 0 : return -1 
	target = sum(arr)
	if target & 1 : return False 
	target >>= 1 
	dp = [True] + [False for _ in range(len(target)) + 1]
	for num in arr:
		for i in range(target, num - 1, -1):
			if dp[target] : return True 
			dp[i] = dp[i] or dp[i - num]
	return dp[target]

def dearrangementCounts(arr):
	if len(arr) == 0 : return -1 
	if len(arr) == 1 : return  0
	if len(arr) == 2 : return  1 
	return (n - 1) * [dearrangementCounts(n - 1) + dearrangementCounts(n - 2)]

def StairClimbing(n):
	return fib(n - 1) + fib (n - 2)

def fib(n):
	x, y = 0, 1 
	if n == 0 : return x 
	if n == 1 : return y 
	for i in range(2, n + 1):
		tmp = x + y 
		x = y 
		y = temp 
	return y 

######################### KNAPSACK #################################

def Knapsack(arr, val, max_wt):
	if not arr or not max_wt : return 0 
	return KnapsackRecur(arr, val, max_wt, len(arr))

def KnapsackRecur(arr, val, target, n): # Recursive KnapSack
	if not n or not target : return 0 
	if arr[n - 1] <= target:
		return max(val[n - 1] + KnapsackRecur(arr, val, target - arr[n - 1], n - 1), \
								KnapsackRecur(arr, val, target, n - 1))
	else:
		return KnapsackRecur(arr, val, target, n - 1)
 
def KnapsackDp(arr, val, max_wt):  # Knapsack using table 
	if not arr or not max_wt : return 0 
	dp = [[0 for _ in range(max_wt + 1)] for _ in range(len(arr) + 1)]
	for i in range(1, len(arr) + 1):
		for j in range(1, max_wt + 1):
			if arr[i - 1] <= j :
				dp[i][j] = max(val[i - 1] + dp[i - 1][j - arr[i - 1]], dp[i - 1][j])
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[len(arr)][max_wt]

def Subsetsum(arr, target):
	if not arr or not target : return 0 
	return SubsetsumRecur(arr, target, len(arr))


def SubsetsumRecur(arr, target, n): # Recusive Subset Sum
	if not n and target : return False 
	if n and not target : return True 
	if arr[n - 1] <= target:
		return SubsetsumRecur(arr, target - arr[n - 1], n - 1) or SubsetsumRecur(arr, target, n - 1)
	else:
		return SubsetsumRecur(arr, target, n - 1)

def SubsetsumDp(arr, target): # SubSetSum Using Table
	if not arr or not target : return -1 
	dp = [[False for _ in range(target + 1)] for _ in range(len(arr) + 1)]
	for i in range(len(arr) + 1):
		dp[i][0] = True 
	for i in range(1, len(arr) + 1):
		for j in range(1, target + 1):
			if arr[i - 1] <= j:
				dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[len(arr)][target]


def EqalSubsetSum(arr):
	if len(arr) == 0 : return -1 
	target = sum(arr)
	if target & 1 : return False 
	target >>= 1
	return Subsetsum(arr, target)

def TotSubsetSum(arr, target):
	if not arr or not target : return - 1
	dp = [[0 for _ in range(target +1 )] for _ in range(len(arr) + 1)]
	for i in range(len(arr) + 1):
		dp[i][0] = 1 
	for i in range(len(arr) + 1):
		for j in range(target + 1):
			if arr[i - 1] <= target :
				dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[len(arr)][target]

print(3 % 5)