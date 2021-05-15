def Combinations(arr, target):
	if len(arr) == 0:
		return -1
	res = []
	Combinator(arr, target, 0, [], res)
	return res 

def Combinator(arr, target, index, path, res):
	if target< 0:
		return 
	if target == 0:
		res.append(path)
	for i in range(index, len(arr)):
		Combinator(arr, target - arr[i], i, path + [arr[i]], res)

print(Combinations([2,3,6,7], 7))
