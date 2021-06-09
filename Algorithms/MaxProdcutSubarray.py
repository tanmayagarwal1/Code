def MaxProductSubarray(arr):
	B = arr[::-1]
	for i in range(1, len(arr)):
		arr[i] *= arr[i - 1] or 1 
		B[i]   *= B[i - 1] or 1
	return max(arr+B)

''' In this problem we knwo that the subarray will either begin from the 0th index or end at len(arr) - 1th index. So we calculate
    prefix prod and suffix prod and the max of those two gives us the result'''


arr = [2,3,-2,4]
print(MaxProductSubarray(arr))
