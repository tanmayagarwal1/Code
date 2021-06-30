def UniquePermutations(arr):
	def Helper(arr, path, res):
		if not arr:
			res.append(path)
			return 
		for i in range(len(arr)):
			if i > 0 and arr[i - 1] == arr[i]:
				continue 
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

	if not arr : raise ValueError 
	res = []
	arr.sort()
	Helper(arr, [], res)
	return res

arr = [1, 1, 2]
print(UniquePermutations(arr))