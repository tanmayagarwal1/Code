def SumOfSquares(num):
	if not num : raise ValueError 
	l, r = 0, int(num**0.5)
	while l <= r :
		if l * l + r * r == num : return True 
		elif l * l + r * r < num : l += 1
		else : r -= 1
	return False 

num = 1000000
print(SumOfSquares(num))