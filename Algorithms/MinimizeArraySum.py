def MinimizeArraySum(arr, k):
	if not arr : raise ValueError 
	n = len(arr)
	if n == 0 : return 0 
	if n == 1 : return 1 
	for i in range(k):
		small = arr[0]
		s_idx = 0 
		large = arr[0]
		l_idx = 0 
		for i in range(1, n):
			if arr[i] > large:
				large = arr[i]
				l_idx = i 
			if arr[i] < small:
				small = arr[i]
				s_idx = i 
		a = large //2 
		b = small * 2 
		if (a + b) < (large + small):
			arr[s_idx] = b 
			arr[l_idx] = a

	return sum(arr)

arr = [5, 1, 10, 2, 3]
k = 1
print(MinimizeArraySum(arr, k))