def SearchInRotated(arr, k):
	if not arr : raise ValueError 
	def Helper(arr):
		l, h = 0, len(arr) - 1
		while h >= l :
			if arr[l] <= arr[h]:
				return l 
			mid = l + (h - l)//2
			ne = (mid + 1) % len(arr)
			prev = (mid + len(arr) - 1) % len(arr)
			if arr[mid] < arr[ne] and arr[mid] < arr[prev]:
				return mid 
			elif arr[l] <= arr[mid]:
				l = mid + 1
			elif arr[mid] <= arr[h]:
				h = mid - 1
		return -1 

	def BinarySearch(arr, l, h):
		if h < l : return - 1
		while h >= l :
			mid = l + (h - l)//2
			if arr[mid] == k : return mid 
			if arr[mid] < k : l = mid + 1
			else : h = mid - 1
		return -1 

	idx = Helper(arr)
	l = BinarySearch(arr, 0, idx - 1)
	r = BinarySearch(arr, idx + 1, len(arr) - 1)
	return l if l != - 1 else r 

def CookChef(arr, p):
	def IsValid(arr, mid, p):
		curr_p = 0 
		curr_time = 0 
		for i in range(len(arr)):
			curr_time = arr[i]
			j = 2 
			while curr_time <= mid:
				curr_time += arr[i]*j 
				j += 1
				curr_p += 1
				if curr_p >= p : return True 
		return False 

	if not arr : raise ValueError 
	l, h = 0, 1e8 
	while h >= l:
		mid = l + (h - l)//2
		if IsValid(arr, mid, p):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

arr = [1, 2, 3, 4]
p = 10
print(CookChef(arr, p))

