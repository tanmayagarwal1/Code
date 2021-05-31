from math import sqrt 
def NumPerfSqaures(n):
	if n == 0:
		return 0 
	if int(sqrt(n))**2 == n:
		return 1 
	for i in range(int(sqrt(n)) + 1):
		if int(sqrt(n - i*i))**2 == n- i*i:
			return 2 
	while n % 4 == 0:
		n >>=2
	if n % 8 == 7:
		return 4 
	return 3 

print(NumPerfSqaures(112))
