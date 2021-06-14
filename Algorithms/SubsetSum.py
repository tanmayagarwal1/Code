def SubsetSum(arr, target):
	if not arr or not target : return - 1
	return SubsetSumUtil(arr, target, len(arr))

def SubsetSumUtil(arr, target, n):
	if n == 0 and target != 0 : return False 
	if n != 0 and target == 0 : return True 
	if arr[n - 1] <= target:
		return SubsetSumUtil(arr, target - arr[n - 1], n - 1) or SubsetSumUtil(arr, target, n - 1)
	else:
		return SubsetSumUtil(arr, target, n - 1)

arr = [2, 3, 7, 8, 10]
target = 11
print(SubsetSum(arr, target))