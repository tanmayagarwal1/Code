def NumWays(cities, trips):
	return PermutationCOefficient(cities - 1, trips - 1)

def PermutationCOefficient(P, k):
	if k < 0 :
		return - 1
	f = 1
	for i in range(k):
		f *= (P - i)
	return f 

print(NumWays(4, 2))