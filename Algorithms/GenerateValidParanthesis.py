def GenerateParanthsis(n):
	def Helper(Open, Close, path, res):
		if not Open and not Close:
			res.append(path)
			return 
		if Open > 0:
			Helper(Open - 1, Close, path + '(', res)
		if Close > Open:
			Helper(Open, Close - 1, path + ')', res)

	if not n : raise ValueError 
	res = []
	Helper(n, n, '', res)
	return res 

n = 3 
print(GenerateParanthsis(n))