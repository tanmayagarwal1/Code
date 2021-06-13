def KnapSackDp(wt, val, max_wt, n):
	if len(wt) == 0 or len(val) == 0 : return -1 
	dp = [[0 for _ in range(max_wt + 1)] for _ in range(n + 1)]
	for i in range(1, len(wt) + 1):
		for j in range(1, max_wt + 1):
			if i == 0 or j == 0 : dp[i][j] = 0 
			if wt[i - 1] <= j:
				dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[n][max_wt]


val = [350, 400, 450, 20, 70, 8, 5, 5]
wt  = [25, 35, 45, 5, 25 ,3, 2, 2]
w   = 104
print(KnapSackDp(wt, val, w, len(wt)))