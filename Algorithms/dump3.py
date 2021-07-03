def CanPartition(arr):
	def Helper(arr, target, n):
		if not target and n : return True 
		if not n and target : return False 
		if arr[n - 1] <= target:
			return Helper(arr, target - arr[n - 1], n - 1) or Helper(arr, target, n - 1)
		else:
			return Helper(arr, target, n - 1)

	if not arr : raise ValueError 
	target = sum(arr) 
	if target & 1 : return False 
	target >>= 1
	return Helper(arr, target, len(arr))

arr = [1, 2, 3, 4]
print(CanPartition(arr))