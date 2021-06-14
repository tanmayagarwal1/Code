def totSubsets(arr, target):
	if len(arr) == 0 or target == 0:
		return - 1
	return totSubsetsUtil(arr, target, len(arr))
def totSubsetsUtil(arr, target, n):
	dp = [[0 for _ in range(target + 1)] for _ in range(len(arr) + 1)]
	for i in range(len(arr) + 1):
		dp[i][0] = 1
	for i in range(1, len(arr) + 1):
		for j in range(1, target + 1):
			if arr[i - 1] <= j :
				dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
			else:
				dp[i][j] = dp[i - 1][j]

	return dp[len(arr)][target]

arr = [1, 2, 3, 3]
target = 6 
print(totSubsets(arr, target))