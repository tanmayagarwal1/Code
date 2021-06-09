def Binary(x): # Decimal to Binary
	if x > 1:
		Binary(x//2)
	print(x % 2, end = '')

def decimal(x): # Binary to decimal
	if x == 0:
		return 0 
	res, i = 0, 0
	while x != 0:
		temp = x % 10 
		res += temp * (2**i)
		x = x//10
		i += 1
	return res

Binary(10)
print()
print(decimal(101010))