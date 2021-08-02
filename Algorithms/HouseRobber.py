def HouseRobber(arr):
	if not arr : raise ValueError 
	if len(arr) == 1: return arr[0]
	dp = [0 for _ in range(len(arr))]
	dp[0] = arr[0]
	dp[1] = max(dp[1], dp[0])
	for i in range(2, len(arr)):
		dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
	return dp[len(arr) - 1]

arr = [2,7,9,3,1]
print(HouseRobber(arr))


'''
A robber has 2 options: a) rob current house i; b) don't rob current house.
If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.

'''