def CountDeg(n):
	if n == 0 : return - 1
	if n == 1 : return 0 
	elif n == 2: return 1 
	return (n - 1) * (CountDeg(n - 1) + CountDeg(n - 2))

print(CountDeg(4))

# Program which return in how many ways can an array of gievn length be permuaated such that no element comes back in its 
# Place. 