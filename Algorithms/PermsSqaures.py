
# Perms such that adjacent elements are squares of each other 
def SquarablePermutations(arr):
	def isSquare(x):
		return int(x**0.5)**2 == x 

	def Helper(arr, path, res):
		if not arr:
			res.append(path)
			return 
		for i in range(len(arr)):
			if i > 0 and arr[i - 1] == arr[i]:
				continue 
			elif path and not isSquare(path[-1] +arr[i]):
				continue 
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

	if not arr : raise ValueError 
	res = []
	Helper(sorted(arr), [], res)
	return len( res ), res

arr = [1, 17, 8]
print(SquarablePermutations(arr))