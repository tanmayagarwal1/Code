n=8
def nqueen():
	b=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
		
	if nqueenu(b,0)==False:
		return False 
	printsol(b)
def nqueenu(b,col):
	if col>=n:
		return True 
	for i in range(n):
		if issafe(b,i,col):
			b[i][col]=1
			if nqueenu(b,col+1)==True:
				return True 
			b[i][col]=0
	return False
def issafe(b,row,col):
	for i in range(col):
		if b[row][i]==1:
			return False
	for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
		if b[i][j]==1:
			return False 
	for i,j in zip(range(row,n),range(col,-1,-1)):
		if b[i][j]==1:
			return False 
	return True 
def printsol(b):
	for i in range(n):
		for j in range(n):
			print(b[i][j],end=" ")
		print()
nqueen()