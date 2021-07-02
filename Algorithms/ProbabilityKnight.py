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

n = 3 # number of rows and cols n x n 
k = 2 # Number of moves 
r = 0 # starts row 
c = 0 # Start col 
print(ProbabilityKnight(n, k, r, c))





