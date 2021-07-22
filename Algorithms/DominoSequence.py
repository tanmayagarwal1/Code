def PushDominos(sti):
	if not sti : raise ValueError 
	res = ''
	i = 0 
	while i < len(sti):
		if sti[i] == 'L' or sti[i] == 'R':
			res += sti[i]
			i += 1
		else: # We encounter a . 
			if i and sti[i - 1] == 'R':
				j = i 
				while j < len(sti) and sti[j] == '.':
					j += 1
				countdots = (j - i)
				if j == len(sti) or sti[j] == 'R': # After completing all the dots we still have an R then .. 
					res += 'R' * countdots
				else:
					res += 'R' * (countdots//2) + '.' * (countdots - 2 * (countdots//2)) + 'L' * (countdots//2)
				i = j 
			else: # If start of the string is . or previous is left pushed 
				j = i 
				while j < len(sti) and sti[j] == '.':
					j += 1
				countdots = (j - i)
				if j == len(sti) or sti[j] == 'R':
					res += '.' * countdots
				else:
					res += 'L' * countdots 
				i = j 
	return res 

sti = "RR.L"
print(PushDominos(sti))


