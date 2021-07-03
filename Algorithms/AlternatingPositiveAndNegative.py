def Alternating(arr):
	if not arr : raise ValueError 
	def Helper(arr):
		i = - 1
		for j in range(len(arr)):
			if arr[j] < 0:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		return arr, i + 1 # i will point to the last negative element ( all -ves are on left ), hence i + 1 will point to first postive element

	arr, i = Helper(arr)
	k = 0 
	while i < len(arr):
		arr[k], arr[i] = arr[i], arr[k]
		k += 2
		i += 1
	return arr 


arr = [1, 2, 3, -4, -1, -4, -8, 7]
print(Alternating(arr))
