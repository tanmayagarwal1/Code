def MaxCutsegments(n, x, y, z):
	if not n:
		return -1
	dp = [-1 for _ in range(n + 1)]
	dp[0] = 0 
	for i in range(n + 1):
		if i - x >= 0:
			dp[i] = max(dp[i - x], dp[i])
		if i - y >= 0:
			dp[i] = max(dp[i - y], dp[i])
		if i - z >= 0:
			dp[i] = max(dp[i - z], dp[i])
		if dp[i] != - 1:
			dp[i] += 1
	return dp

print(MaxCutsegments(5, 5, 3, 2))