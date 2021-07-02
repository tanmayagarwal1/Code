def LongestHappyPrefix(sti):
	if not sti : raise ValueError 
	res, l, r, mod = 0, 0, 0, 10**9 + 7 
	for i in range(len(sti) - 1):
		l = (l * 128 + ord(sti[i])) % mod 
		r = (r + pow(128, i, mod) * ord(sti[~i])) % mod
		if l == r : res = i + 1
	return sti[:res]

sti = 'ababab'
print(LongestHappyPrefix(sti))