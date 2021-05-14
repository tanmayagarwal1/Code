def CoinChange(coins, amount):
	dp = [float('inf') for _ in range(amount+1)]
	dp[0] = 0 
	for current_amount in range(1, amount + 1):
		for coin in coins:
			if current_amount - coin >= 0:
				dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
	if dp[-1] == float('inf'):
		return -1 
	return dp[-1] #dp[-1] == the last element  or you can use dp[amount]

print(CoinChange([1,2,3,4],5))
