def Swap(arr):
	if len(arr) == 0 : return - 1
	i, j = 0 ,len(arr) - 1
	while i < j:
		while arr[j] < 0 :
			j -= 1
		while arr[i] >= 0 : 
			i += 1
		arr[i], arr[j] = arr[j], arr[i]
		i += 1
		j -= 1
	return arr, i 

def ZigZag(arr):
	if len(arr) == 0 : return - 1
	arr, i = Swap(arr)
	k = 1
	while k < len(arr) and i < len(arr):
		arr[k], arr[i] = arr[i], arr[k]
		k += 2
		i += 1
	return arr


arr = [1, 2, 3, -4, -1, 4]
print(ZigZag(arr))
