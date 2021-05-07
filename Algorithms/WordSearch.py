def Exist(board,word):
	m=len(board)
	n=len(board[0])
	if m==0 or n==0:
		return -1 
	word=[i for i in word]
	count=0
	for i in range(m):
		for j in range(n):
			if board[i][j]==word[0] and Helper(board,word,i,j,count):
				return True 
	return False 



def Helper(board, word, i, j, count):
	if count==len(word):
		return True 
	if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[count]:
		return 0 
	x=board[i][j]
	board[i][j]="#"
	neighbours=((0,1),(0,-1),(1,0),(-1,0))
	res= Helper(board,word,i+1,j,count+1) or Helper(board,word,i-1,j,count+1) or \
		 Helper(board,word,i,j+1,count+1) or Helper(board,word,i,j-1,count+1)
	board[i][j]=x
	return res






board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(Exist(board,"ABCCED"))
