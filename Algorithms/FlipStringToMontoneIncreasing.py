def montoneincreasingstring(sti):
	if not sti : raise ValueError 
	flips = 0 
	ones = 0 
	for char in sti:
		if char == '1':
			ones += 1 
		else:
			flips += 1
		flips = min(ones, flips)
	return flips 

sti = '00011000'
print(montoneincreasingstring(sti))