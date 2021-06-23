def MinOperationsArrayIncrease(arr):
	if len(arr) == 0 : raise ValueError 
	count = 0 
	for i in range(1, len(arr)):
		if arr[i] <= arr[i - 1]:
			diff = arr[i - 1] - arr[i] + 1 # + 1 to account for 0 difference
			count += diff 
			arr[i] = arr[i - 1] + 1
	return count 

arr = [1, 1, 1]
print(MinOperationsArrayIncrease(arr)) 