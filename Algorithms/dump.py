def Alternate(arr):
	if len(arr) == 0 : return - 1
	arr.sort()
	res = [0]*len(arr)
	i, j ,k = 0, len(arr) - 1, 0
	while k <= len(arr) - 1:
		if i == j :
			res[k] = arr[i]
			break 
		res[k] = arr[j]
		res[k + 1] = arr[i]
		i += 1
		j -= 1
		k += 2 
	return res

arr = [70, 80, 90,60, 12, 32, 45, 76, 54]
print(Alternate(arr))