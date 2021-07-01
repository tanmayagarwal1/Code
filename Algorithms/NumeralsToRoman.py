def NumeralsToInts(x):
	values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
	numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
	res = ''
	for v, n in zip(values, numerals):
		res += (x//v)* n
		x %= v
	return res 

print(NumeralsToInts(38))