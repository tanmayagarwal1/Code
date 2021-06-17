def PeakElement(arr):
	if not arr : return -1 
	l, h = 0, len(arr) - 1
	while h >= l:
		mid = l + (h - l)//2
		if mid != 0 and mid != len(arr) - 1:
			if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
				return arr[mid], mid 
			elif arr[mid] < arr[mid - 1]:
				h = mid - 1
			else:
				l = mid + 1
		else:
			if mid == 0 :
				if arr[mid] > arr[mid + 1]:
					return arr[mid], mid 
				else:
					return arr[mid + 1], 1
			elif mid == len(arr) - 1:
				if arr[mid] > arr[mid] - 1:
					return arr[mid], mid 
				else:
					return arr[mid - 1], len(arr) - 1
	return -1 

arr = [2, 23, 90, 67]
print(PeakElement(arr))
