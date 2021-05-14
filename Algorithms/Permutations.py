def Permutations(sti):
	n = len(sti)
	if n ==0 :
		return -1 
	res = []
	Permuter(sti, [], res) # [] = empty path 
	return res 
	
def Permuter(arr, path, res):
	if not arr:
		res.append(path)
	for i in range(len(arr)):
		Permuter(arr[:i] + arr[i+1:], path + [arr[i]], res)


print(Permutations([1,2,3]))


