def ProbabilityKnight(n, k, r, c):
	def Helper(i, j, moves):
		if i < 0 or i >= n or j < 0 or j >= n : return 0 
		elif moves == 0 : return 1 
		return (Helper(i + 1, j + 2, moves - 1) + 
				Helper(i + 1, j - 2, moves - 1) + 
				Helper(i - 1, j + 2, moves - 1) + 
				Helper(i - 1, j - 2, moves - 1) + 
				Helper(i + 2, j + 1, moves - 1) + 
				Helper(i + 2, j - 1, moves - 1) + 
				Helper(i - 2, j + 1, moves - 1) + 
				Helper(i - 2, j - 1, moves - 1))/ 8 
	return Helper(r, c, k)

n = 3
k = 2
r = 0 
c = 0 
print(ProbabilityKnight(n, k, r, c))





