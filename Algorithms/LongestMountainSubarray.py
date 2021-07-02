def LongestMountainSubarray(arr):
	if not arr : raise ValueError 
	if len(arr) < 3 : return False 
	res = 0 
	for i in range(1, len(arr) - 1):
		if arr[i + 1] < arr[i] > arr[i - 1]:
			l = r = i 
			while l and arr[l] > arr[l - 1] : l -= 1
			while r + 1  < len(arr) and arr[r] > arr[r + 1] : r += 1
			if r - l + 1 > res : res = r - l + 1
	return res 

arr = [2,1,4,7,3,2,5]
print(LongestMountainSubarray(arr))
