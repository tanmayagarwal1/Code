def ContiguousArray(arr):
	if not arr : raise ValueError 
	Sum = 0 
	d = {0 : -1} # We have to start from -1 cause array starts from 0 and the sum can go to -1
	res = float('-inf')
	for idx, num in enumerate(arr):
		if num == 0 : Sum += -1 
		else : Sum += 1
		if Sum in d:
			res = max(res, idx - d[Sum])
		else:
			d[Sum] = idx 
	return res 


arr = [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]
print(ContiguousArray(arr))




