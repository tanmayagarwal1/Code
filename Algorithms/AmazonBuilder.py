def FullfillmentBuilder(arr):
	if not arr:
		return -1 
	arr.sort()
	dp = [0 for _ in range(len(arr))]
	dp[0] = arr[0]
	for i in range(1, len(arr)):
		dp[i] = dp[i - 1] + arr[i]
	return sum(dp[1:])


print(FullfillmentBuilder([8, 4, 6, 12]))
