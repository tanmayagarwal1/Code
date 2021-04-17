global n
n=4 
def nqueen():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]
    if nqueenu(board,0)==False:
        print("NO solution")
    printsol(board)

def nqueenu(board,col):
    if col>=n:
        return True 
    for i in range(n):
        if issafe(board,i,col):
            board[i][col]=1

            if nqueenu(board,col+1)==True:
                return True 
            board[i][col]=0 
    return False 
def issafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False 
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False 
    for i,j in zip(range(row,n),range(col,-1,-1)):
        if board[i][j]==1:
            return False 
    return True 

def printsol(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()

nqueen()