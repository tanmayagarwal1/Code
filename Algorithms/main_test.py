import numpy as np 
run_max = np.maximum.accumulate
from collections import defaultdict
from heapq import heappop, heappush

def Lcs(x, y):
	m, n = len(x), len(y)
	if m == 0 or n == 0: return -1 
	dp = [[0 for _ in range(n +1)] for _ in range(m + 1)]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] == y[j - 1]:
				dp[i][j] = dp[i- 1][j - 1] + 1
			else:
				dp[i][j] = max(dp[i -1][j], dp[i][j - 1])
	return dp[m][n]

def regularexpression(sti, pattern):
	m, n = len(sti), len(pattern)
	if m == 0 or n == 0 : return - 1
	dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
	dp[0][0] = True
	for i in range(1, n + 1):
		if pattern[i - 1] == '*':
			dp[0][i] = dp[0][i - 2]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if sti[i - 1] == pattern[j - 1] or pattern[j - 1] == '.':
				dp[i][j] = dp[i - 1][j - 1]
			elif pattern[j - 1] == '*':
				dp[i][j] = dp[i][j - 2]
				if sti[i - 1]== pattern[j - 2] or pattern[j - 2] == '.':
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
		return - 1
	dp = [[0 for _ in range(n)] for _ in range(m)]
	if not grid[0][0] : dp[0][0] = 1
	for i in range(1, m):
		if not grid[i][0]:
			dp[i][0] = 1
	for i in range(1, n):
		if not grid[0][i]:
			dp[0][i] = 1 
	for i in range(1, m):
		for j in range(1, n):
			if not grid[i][j]:
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
			else:
				continue 
	return dp[m - 1][n - 1]

def MinimumCostPath(grid):
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

def CoinChange(coins, ammount):
	dp = [float('inf') for _ in range(ammount + 1)]
	dp[0] = 0 
	for i in range(1, ammount + 1):
		for coin in coins:
			if i - coin >= 0:
				dp[i] = min(dp[i], dp[i - coin] + 1)
	return dp[ammount]

def egg_max(f, n):
	dp = [[0 for _ in range(n + 1)] for _ in range(f + 1)]
	for i in range(1, f + 1):
		for j in range(1, n + 1):
			dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1
		if dp[i][j] >= f : return i 

def water_collector(arr):
	a = np.array(arr)
	global_max = np.argmax(a)
	return np.sum(run_max(a[:global_max]) - a[:global_max], dtype = np.int64) + \
			np.sum(run_max(a[:global_max:-1]) - a[:global_max:-1], dtype = np.int64)

def TrainTix(days, cost):
	if not days : return 0 
	dp = [-1 for _ in range(366)]
	dp[0] = 0 
	for day in days:
		dp[day] = 0 
	for i in range(1, 366):
		if dp[i] == -1:
			dp[i] = dp[i -1 ]
		else:
			dp[i] = min(dp[i - 1] + cost[0], dp[max(i - 7, 0)] + cost[1], dp[max(i - 30, 0)] + cost[2])

	return dp[365]


def CheapestFlights(Flights, src, dst, stops):
	if not Flights : return -1 
	graph, pq = defaultdict(list), []
	for s, d, w in Flights : graph[s].append((d, w))
	heappush(pq, (0, src, stops + 1))
	while pq :
		price, city, k = heappop(pq)
		if city == dst : return price 
		if k > 0 :
			for new_city, new_price in graph[city]:
				heappush(pq, (price + new_price, new_city, k - 1))
	return - 1


def Knapsack(arr, val, max_wt):
	if not arr or not val : return - 1
	return HelperKnapsack(arr, val, max_wt, len(arr))

def HelperKnapsack(arr, val, max_wt, n):
	if not n or not max_wt : 
		return 0 
	if arr[n - 1] <= max_wt:
		return max(val[n - 1] + HelperKnapsack(arr, val, max_wt - arr[n - 1], n - 1), HelperKnapsack(arr, val, max_wt, n - 1))
	else:
		return HelperKnapsack(arr, val, max_wt, n - 1)

def isSumSubset(arr, target):
	if not arr : return - 1
	return HelperSubset(arr, target, len(arr))

def HelperSubset(arr, target, n):
	if not n and target : return False 
	if not target and n : return True 
	if arr[n - 1] <= target:
		return HelperSubset(arr, target - arr[n - 1], n - 1) or HelperSubset(arr, target, n - 1)
	else:
		return HelperSubset(arr, target, n - 1)

def CountSubsetstoSum(arr, target):
	if not arr or not target : return - 1
	return HelperCountSubset(arr, target, len(arr))

def HelperCountSubset(arr, target, n):
	if not n and target : return 0 
	if not target and n : return 1 
	if arr[n - 1] <= target :
		return HelperCountSubset(arr, target - arr[n - 1], n - 1) + HelperSubset(arr, target, n - 1)
	else:
		return HelperSubset(arr, target, n - 1)

def UnboundedKnapsack(arr, val, max_wt):
	if not arr or not max_wt : return 0 
	return HelperUnbounded(arr, val, max_wt, len(arr))

def HelperUnbounded(arr, val, max_wt, n):
	if not max_wt or not n : return 0 
	if arr[n - 1] <= max_wt:
		return max(val[n - 1] + HelperUnbounded(arr, val, max_wt - arr[n - 1], n), \
								HelperUnbounded(arr, val, max_wt, n - 1))
	else:
		return HelperUnbounded(arr, val, max_wt, n - 1)

def EqalSumSubset(arr):
	target = sum(arr)
	if target & 1 : return False 
	target >>= 1
	return HelperEqual(arr, target, len(arr))

def HelperEqual(arr, target, n):
	if not n and target : return False
	if not target and n : return True
	if arr[n - 1] <= target:
		return HelperEqual(arr, target - arr[n - 1], n - 1) or HelperEqual(arr, target, n - 1)
	else:
		return HelperEqual(arr, target, n - 1)

def wordbreak(sti, dic):
	if not sti : return -1 
	dp = [False for _ in range(len(sti) + 1)]
	dp[0] = True
	for i in range(1, len(sti) + 1):
		for word in dic:
			if sti[:i].endswith(word):
				dp[i] = dp[i] or dp[i - len(word)]
	return dp[len(sti)]

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordbreak(s, wordDict))



