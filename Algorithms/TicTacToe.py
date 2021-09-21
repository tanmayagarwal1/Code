def TicTacToe(Moves):
	if not Moves : raise ValueError 
	A = [0] * 8 
	B = [0] * 8 
	for i in range(len(Moves)):
		r, c = Moves[i]
		player = A if i % 2 == 0 else B 
		player[r] += 1 
		player[c + 3] += 1 
		if r == c : player[6] += 1
		if r == 2 - c : player[7] += 1 
	for i in range(8):
		if A[i] == 3 : return "A"
		if B[i] == 3 : return "B"
	return "Draw" if len(Moves) == 9 else "Pending"


moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
print(TicTacToe(moves))
