def MinCostClimbingStairs(arr):
	if not arr : raise ValueError 
	dp = [0] * len(arr)
	dp[0] = arr[0]
	if len(arr) >= 2 : dp[1] = arr[1]
	for i in range(2, len(arr)):
		dp[i] = arr[i] + min(dp[i - 1], dp[i - 2])
	return min(dp[-1], dp[-2])

arr = [1,100,1,1,1,100,1,1,100,1]
print(MinCostClimbingStairs(arr))