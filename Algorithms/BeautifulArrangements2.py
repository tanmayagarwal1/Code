def Arrangement2(n, k):
	arr = [i for i in range(1, n + 1)]
	for i in range(1, k):
		arr[i:] = arr[:i - 1:-1]
	return arr 

print(Arrangement2(3, 2))
