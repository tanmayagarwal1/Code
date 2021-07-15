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

def SearchInSorted(arr, target):
	def Helper(arr, l, h):
		while h >= l:
			mid = l + (h - l)//2
			if arr[mid] == target:
				return mid 
			elif arr[mid] < target:
				l = mid + 1
			else:
				h = mid - 1
		return -1 
	if not arr : raise ValueError
	idx = Minimum(arr)
	return idx
	left = Helper(arr, 0, idx - 1)
	right = Helper(arr, idx, len(arr) - 1)
	return left if left != -1 else right


arr = [4,5,6,7,0,1,2]
print(SearchInSorted(arr, 2))


