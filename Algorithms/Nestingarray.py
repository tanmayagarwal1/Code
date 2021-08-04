def NestingArray(arr):
	if not arr : raise ValueError 
	seen = [0] * len(arr)
	res = 0 
	for num in arr:
		count = 0 
		while not seen[num]:
			seen[num] = 1
			count += 1 
			num = arr[num]
		res = max(res, count)
	return res 

arr = [5,4,0,3,1,6,2]
print(NestingArray(arr))