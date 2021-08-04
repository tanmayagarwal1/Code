def CoinChange2(arr, ammount):
	def Helper(arr, ammount, n):
		if n == 0 : return 0 
		if ammount == 0 : return 1 
		if arr[n - 1] <= ammount:
			return Helper(arr, ammount - arr[n - 1], n) + Helper(arr, ammount, n - 1)
		return Helper(arr, ammount, n - 1)
	if not arr : raise ValueError 
	n = len(arr)
	return Helper(arr, ammount, len(arr))

arr = [1, 2, 5]
ammount = 5 
print(CoinChange2(arr, ammount))