def PermutationCOefficient(P, k):
	if k < 0 :
		return - 1
	f = 1
	for i in range(k):
		f *= (P - i)
	return f 

print(PermutationCOefficient(3, 2))


#Time : O(n), space : O(1)