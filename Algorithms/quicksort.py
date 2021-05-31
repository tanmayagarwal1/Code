def partition(arr, l, h):
	i = l - 1
	pivot = arr[h]
	for j in range(l, h):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[h] = arr[h], arr[i + 1]
	return i + 1

def quicksort(arr, l, h):
	if len(arr) == 1:
		return arr 
	if l < h:
		mid = partition(arr, l, h)
		quicksort(arr, l, mid - 1)
		quicksort(arr, mid + 1, h)

arr= [4,21,3,12,313,2,131]
quicksort(arr, 0, len(arr) - 1)
print(arr)
