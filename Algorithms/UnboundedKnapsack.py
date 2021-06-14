def UnboundKnapsack(arr, val, max_wt):
	if not arr or not val : return - 1
	return UnboundKnapsackUtil(arr, val, max_wt, len(arr))

def UnboundKnapsackUtil(arr, val, max_wt, n):
	if not n or not max_wt:
		return 0 
	if arr[n - 1] <= max_wt:
		return max(val[n - 1] + UnboundKnapsackUtil(arr, val, max_wt - arr[n - 1], n), UnboundKnapsackUtil(arr, val, max_wt, n - 1))
	else:
		return UnboundKnapsackUtil(arr, val, max_wt, n - 1)

arr = [1, 5, 8, 9, 10, 17, 17, 20]
length = [1, 2, 3, 4, 5, 6, 7, 8]
n = 8 
print(UnboundKnapsack(length, arr, n))
