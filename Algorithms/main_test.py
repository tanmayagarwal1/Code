def Pemrs(arr):
	if not arr : raise ValueError 
	def Helper(arr, path, res):
		if not arr:
			res.append(path)
			return 
		for i in range(len(arr)):
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

	res = []
	Helper(arr, [], res)
	return res 

arr = [1, 2, 3]
print(Pemrs(arr))