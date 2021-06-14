def totSubsets(arr, target):
	if len(arr) == 0 or target == 0:
		return - 1
	return totSubsetsUtil(arr, target, len(arr))
def totSubsetsUtil(arr, target, n):
	if n == 0 and target != 0 : return 0 
	if n != 0 and target == 0 : return 1 
	if arr[n - 1] <= target :
		return totSubsetsUtil(arr, target - arr[n - 1], n - 1) + totSubsetsUtil(arr, target, n - 1)
	else:
		return totSubsetsUtil(arr, target, n - 1)

arr = [1, 2, 3, 3]
target = 6 
print(totSubsets(arr, target))