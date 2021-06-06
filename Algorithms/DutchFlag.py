def Sort(arr):
	if len(arr) == 0:
		return -1 
	l, h, mid = 0, len(arr) - 1, 0
	while mid <= h:
		if arr[mid] == 0:
			swap(arr, mid, l)
			l += 1
			mid += 1
		elif arr[mid] == 1:
			mid += 1
		else:
			swap(arr, mid, h)
			h -= 1
def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i] 

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Sort(arr)
print(arr)

