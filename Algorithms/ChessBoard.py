def movesToChessboard(board):
    n=len(board)
    for i in range(n):
        for j in range(n):
            if xor(xor(board[0][0],board[0][j]),xor(board[i][0],board[i][j])):
                return -1 
    rs=cs=cnumber=rnumber=0 
    for i in range(n):
        rs=rs+board[i][0]
        cs=cs+board[i][0]
        rnumber+=board[i][0]==n%2 
        cnumber+=board[0][i]==n%2 
    if rs != n/2 and rs != (n+1)/2:
        return -1 
    if cs != n/2 and cs != (n+1)/2:
        return -1 
    if n%2==1:
        if cnumber%2:
            cnumber=n-cnumber 
        if rnumber%2:
            rnumber=n-rnumber 
    else:
        cnumber=min(cnumber,n-cnumber)
        rnumber=min(rnumber,n-rnumber)
    if rnumber+cnumber==2:
        return 0 
    else:
        return round((rnumber+cnumber)/2)
def xor(x,y):
    return (x and not y) or (not x and y)
arr=[[0,1],[1,0]]
print(movesToChessboard(arr))


