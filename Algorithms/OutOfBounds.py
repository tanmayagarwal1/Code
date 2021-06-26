def OutOfBounds(m, n, sr, sc, max_moves):
	dp = [[[-1]*(max_moves + 1) for _ in range(n + 1)] for _ in range(m + 1)]

	def Helper(i, j, moves):
		if moves < 0 : return 0 
		if i < 0 or i >= m or j < 0 or j >= n : return 1 
		if dp[i][j][moves] != - 1: return dp[i][j][moves]
		Phi = Helper(i + 1, j, moves - 1)
		Psi = Helper(i, j + 1, moves - 1)
		Mu  = Helper(i, j - 1, moves - 1)
		Nu  = Helper(i - 1, j, moves - 1)
		dp[i][j][moves] = Phi + Psi + Mu + Nu 
		return dp[i][j][moves]

	if not max_moves : raise ValuseError 
	return Helper(sr, sc, max_moves)

m = 8
n = 50
maxMove = 23
startRow = 5
startColumn = 26
print(OutOfBounds(m, n, startRow, startColumn, maxMove))