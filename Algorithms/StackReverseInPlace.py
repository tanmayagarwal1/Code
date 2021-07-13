def ReverseStack(arr):
	def Helper(arr, x):
		if not arr:
			arr.append(x)
			return 
		curr = arr.pop()
		Helper(arr, x)
		arr.append(curr)
	if not arr : return 
	x = arr.pop()
	ReverseStack(arr)
	Helper(arr, x)
	return arr 


arr = [1, 2, 3, 4, 5, 6]
print(ReverseStack(arr))