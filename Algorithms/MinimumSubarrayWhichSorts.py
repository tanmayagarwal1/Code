def SortSubarray(arr):
	if len(arr) == 0 : return -1 
	i, j = 0, len(arr) - 1
	while i < len(arr) and arr[i] < arr[i + 1]:
		i += 1
	while j > -1 and arr[j] > arr[j - 1]:
		j -= 1
	global_max, gloabl_min = max(arr[i:j + 1]), min(arr[i :j + 1])
	for tmp in range(0, i):
		if arr[tmp] > gloabl_min:
			i = tmp 
	for tmp in range(j, len(arr)):
		if global_max > arr[tmp]:
			j = tmp 
	return i, j 


arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
print(SortSubarray(arr))