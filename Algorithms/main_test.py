def eggmax(n,k):
	dp=[[0]*(k+1) for i in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,k+1):
			dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1
		if dp[i][j]>=n: return i
print(eggmax(120,2))