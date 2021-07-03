def KthLargest(arr, k):
	def partition(arr, l, h):
		i = l - 1
		pivot = arr[h]
		for j in range(l, h):
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i + 1], arr[h] = arr[h], arr[i + 1]
		return i + 1 

	def Helper(arr, k):
		if arr: 
			mid = partition(arr, 0, len(arr) - 1)
			if k > mid + 1:
				return Helper(arr[mid + 1 :], k - mid - 1)
			elif k < mid + 1:
				return Helper(arr[:mid], k)
			else:
				return arr[mid]

	if not arr : raise ValueError
	return Helper(arr, len(arr) + 1 - k)

arr = [3,2,1,5,6,4]
k = 2
print(KthLargest(arr, k))
print(sorted(arr))