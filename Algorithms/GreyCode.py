def greycode(n):
	if not n : raise ValueError 
	res= [0]
	for i in range(1, 2**n):
		res.append(res[-1] ^ (i & ~i + 1))
	return res 
n = 3
print(greycode(n))
