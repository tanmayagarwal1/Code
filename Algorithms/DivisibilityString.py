def Divisibility(sti, divisor):
	if len(sti) == 0 or len(divisor) == 0:
		return - 1
	i, j, count, res = 0, 0, 0, 0
	while i < len(sti):
		if sti[i] == divisor[j]:
				count += 1 
				i += 1
				j += 1
				if count == len(divisor):
					res += 1 
					count = 0 
					j = 0
		else:
			count = 0 
			i += 1
			j = 0

	return res == len(sti)/len(divisor) 

sti = "abcdabcdabcdxabcd"
divisor = "abcdabcd"
print(Divisibility(sti, divisor))

