def ZigZagConversion(sti, n):
	if not sti : raise ValueError 
	res = [''] * n
	idx = 1 
	increment_up = True 
	for char in sti:
		res[idx - 1] += char 
		if idx == n :
			increment_up = False 
		elif idx == 1 :
			increment_up = True 
		if increment_up == True :
			idx += 1
		else:
			idx -= 1
	return ''.join(res)

sti = "PAYPALISHIRING"
print(zigZagConversion(sti, 3))