def canPartition(arr):
	if len(arr) == 0 : return -1 
	target = sum(arr)
	if target & 1 : return False
	target >>= 1 
	return SubsetSum(arr, target, len(arr))

def SubsetSum(arr, target, n):
	if n == 0 and target != 0 : return False 
	if n != 0 and target == 0 : return True 
	if arr[n - 1] <= target : 
		return SubsetSum(arr, target - arr[n - 1], n - 1) or SubsetSum(arr, target, n - 1)
	else:
		return SubsetSum(arr, target, n - 1)

arr = [1, 5, 11, 5]
print(canPartition(arr))