def Conjecture(num):
	# This prooves the conjecture of (2x + 1)
	if not num or num < 1 : raise ValueError 
	seen = {4, 2, 1}
	limit = 10000
	count = 0 
	while True:
		count = count + 1
		if num % 2 == 0  : num = num // 2 
		else : num = num * 3 + 1
		if num in seen : 
			break 
		if count > limit : return False 
	return True, count

print(Conjecture(27))

