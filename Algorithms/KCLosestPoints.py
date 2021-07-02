def KclosestPoints(arr, k, x):
	if not arr : raise ValueError 
	l = 0 
	h = len(arr) - k 
	while h > l :
		mid = l + (h - l)//2
		if abs(arr[mid + k] - x) < abs(arr[mid] - x):
			l = mid + 1
		else:
			h = mid 
	return arr[l : l + k]

arr = [1,2,3,4,4,4,4,5,5]
k = 3
x = 3
print(KclosestPoints(arr, k, x))

