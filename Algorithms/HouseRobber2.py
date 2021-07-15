def HouseRobber2(arr):
	def Helper(arr):
		if not arr : raise ValueError 
		if len(arr) == 1: return arr[0]
		dp = [0 for _ in range(len(arr))]
		dp[0] = arr[0]
		dp[1] = max(arr[1], arr[0])
		for i in range(2, len(arr)):
			dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
		return dp[len(arr) - 1]

	if not arr : raise ValueError 
	if len(arr) == 1 : return arr[0]
	return max( Helper(arr[1:] + [0]), Helper([0] + arr[:-1]) )

arr = [1,2,3,1]
print(HouseRobber2(arr))

'''

The changes to this verison of thr problem is that the houses are arranged in a cicrle and so the thief cannot rob the first and the last house both together 
Hence we calculate the max he can rob if he robs house 1 and leaves house(n) : Helper(arr[:-1]) 
And also the max he can rob leaving first house and robbing the n'th house. Helper(arr[1:])
I have added extra padding, ie : arr[1:] + [0] and arr[:-1] + [0] so that if the input array size only two, the input to our helper functions is of atleat length two 
If padding is not added, as the input array is split into two, each helper will get an array of size one as the array is split and will throw an index error ar dp[1] = max(..)
To avoide this edge case, I have added padding 

'''