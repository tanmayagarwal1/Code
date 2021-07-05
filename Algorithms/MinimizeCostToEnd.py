def MinimizeCost(arr, x):
	if len(arr) == 0 : raise ValueError 
	n = len(arr)
	dp = [0]*(n + 1)
	dp[0] = arr[0]
	for i in range(1, n):
		if i == 1 : dp[i] = arr[i] + dp[i - 1]
		elif i == 2 : dp[i] = arr[i] + min(dp[i - 1], x + dp[i - 2])
		else:
			dp[i] = arr[i] + min(dp[i - 1], x + dp[i - 2], 2 * x + dp[i - 3])
	return dp[n - 1]

arr = [6, 3, 9, 2, 1, 3, 4]
x  = 4 
print(MinimizeCost(arr, x))

# We need to minimize the sum to reach the end element by skiiping certain elements 
# We cannot skip more than two consecutive elements and we cannot skip the first and the last 
# Wheneve we skip an element : x will be added to the sum 
# We use dp 
# We observe that if any position i is skipped, the cost is increased by arr[i] or X but if the cost 
# is increased by arr[i] then it’s best to choose that position as choosing the position also increases 
# the cost by arr[i]. This implies that the minimum cost to reach position i can be found by taking the 
# minimum among the : 
# minimum cost to reach position (i – 1), X + the minimum cost to reach position (i – 2) and 2X + the minimum cost to reach position (i – 3).