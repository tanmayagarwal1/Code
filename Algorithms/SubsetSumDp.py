def SubsetSumDp(arr, target):
	if not arr or not target : return - 1
	dp = [[False for _ in range(target + 1)] for _ in range(len(arr) + 1)]
	for i in range(len(arr) + 1):
		dp[i][0] = True
	for i in range(1, len(arr) + 1):
		for j in range(1, target + 1):
			if arr[i - 1] <= j :
				dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
			else:
				dp[i][j] = dp[i - 1][j]

	return dp[len(arr)][target]


arr = [1, 2 ,3, 4 ,5, 6, 7]
target = 28
print(SubsetSumDp(arr, target))