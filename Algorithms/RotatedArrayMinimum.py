def Minimum(arr):
	if not arr : raise ValueError 
	l, h = 0, len(arr) - 1
	while h >= l :
		if arr[l] <= arr[h]:
			return l 
		mid = l + (h - l)//2
		ne = (mid + 1) % len(arr)
		pre = (mid + len(arr) - 1) % len(arr)
		if arr[mid] <= arr[ne] and arr[mid] <= arr[pre]:
			return mid
			break 
		elif arr[mid] >= arr[l]:
			l = mid + 1
		elif arr[mid] <= arr[h]:
			h = mid - 1
	return -1 

arr = [4, 5, 6, 1, 2, 3]
print(Minimum(arr))