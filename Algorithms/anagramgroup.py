def Bubble(arr):
	n = len(arr)
	for i in range(n):
		for j in range(1+i, n):
			if arr[j] < arr[i]:
				arr[j], arr[i] = arr[i], arr[j] 
	return arr
print(Bubble([1,2,4,2,312,4,2,32]))
