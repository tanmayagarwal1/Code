def MaximumCommonSubarray(x, y):
	m, n = len(x), len(y)
	if not m or not y : return 
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	res = 0 
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] == y[j - 1]: dp[i][j] = dp[i - 1][j - 1] + 1
			res = max(res, dp[i][j])
	return res 

arr1 = [1,2,3,2,1]
arr2 = [3,2,1,4,7]
print(MaximumCommonSubarray(arr1, arr2))