def MultiplyString(str1, str2):
	if not str1 or not str2 : raise ValueError 
	carry1 = 1
	for i in str1:
		carry1 = carry1 * 10 + (ord(i) - 48)
	carry2 = 1
	for i in str2:
		carry2 *= carry2 * 10 + (ord(i) - 48)
	return str(carry1 * carry2)
print(MultiplyString('2345678', '3'))