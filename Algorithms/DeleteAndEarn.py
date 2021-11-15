def DeleteAndEarn(arr):
	def Helper(arr):
		prev, curr = 0, 0 
		for num in arr:
			prev, curr = curr, max(num + prev, curr)
		return curr
	if not arr : raise ValueError 
	dp = [0] * 10001 
	for num in arr:
		dp[num] += num 
	return Helper(dp)

arr = [2,2,3,3,3,4]
print(DeleteAndEarn(arr))