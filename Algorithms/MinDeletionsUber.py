def MinDeletions(arr, p, q, r):
	arr.sort() # Use mergeSort Here
	x = (p) + (2 * q) + (3 * r)
	return sum(arr[x:])

arr = [3, 1, 0, 5, 1, 6, 5, -1, -100]
print(MinDeletions(arr, 1, 1, 1))
