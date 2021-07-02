def Lcs(x):
	if not x : raise ValueError 
	d = dict()
	for arr in x:
		for num in arr:
			d[num] = d.get(num, 0) + 1
	res = []
	for num, freq in d.items():
		if freq == len(x):
			res.append(num)
	return res 

x = [[2,3,6,8],
   	 [1,2,3,5,6,7,10],
     [2,3,4,6,9]]

print(Lcs(x))