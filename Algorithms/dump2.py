def Lcs(arrs):
	if not arrs : raise ValueError 
	d = {}
	for arr in arrs:
		for num in arr:
			d[num] = d.get(num, 0) + 1
	res = []
	for num, val in d.items():
		if val == len(arrs):
			res.append(num)
	return res 

x = [[2,3,6,8],
     [1,2,3,5,6,7,10],
     [2,3,4,6,9]]
print(Lcs(x))