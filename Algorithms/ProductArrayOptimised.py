def ProductArray(arr):
	if len(arr) == 0 : return -1 
	n = len(arr)
	res = [1]*len(arr)
	for i in range(1, len(arr)):
		res[i] = res[i - 1]*arr[i - 1]
	prod = 1 
	for i in range(n - 1, -1 , -1):
		res[i] = res[i]*prod
		prod = prod*arr[i]
	return res 

arr = [1, 2, 3, 4, 5]
print(ProductArray(arr))
