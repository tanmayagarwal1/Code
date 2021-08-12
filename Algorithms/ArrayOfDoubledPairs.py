def canReorderDouble(arr):
	if not arr : raise ValueError
	d = {}
	for num in arr:
		d[num] = d.get(num, 0) + 1
	for x in sorted(arr, key = lambda x : abs(x)):
		if d[x] == 0 : continue 
		if 2 * x not in d : return False 
		if d[2 * x] == 0 : return False 
		d[x] -= 1
		d[2 * x] -= 1
	return True 

arr = [4, -2, 2, -4]
print(canReorderDouble(arr))