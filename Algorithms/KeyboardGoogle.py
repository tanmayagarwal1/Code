def TimetoType(keyboard, sti):
	if len(keyboard) == 0 or len(sti) == 0 : return - 1
	d, res = dict(), 0 
	for i, j in enumerate(keyboard) : d[j] = i 
	res = d[sti[0]]
	for i in range(1, len(sti)):
		tmp = abs (d[sti[i]] - d[sti[i - 1]])
		res = res + tmp
	return res


keyboard = "abcdefghijklmnopqrstuvwxy"
text = "cba" 
print(TimetoType(keyboard, text))