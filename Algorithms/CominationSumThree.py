def CombinationSum2(n, k):
	def Helper(arr, target, k, path, res):
		if target < 0 or k < 0 : return 
		if target == 0 and k == 0: 
			res.append(path)
			return 
		for i in range(len(arr)):
			Helper(arr[i + 1:], target - arr[i], k - 1, path + [arr[i]], res)
	# Find all possible k numbers that sum upto n 
	# Use only numbers between 1 through 9 
	res = []
	Helper(list(range(1, 10)), n, k, [], res)
	return res 

k = 3 
n = 7 
print(CombinationSum2(n, k))