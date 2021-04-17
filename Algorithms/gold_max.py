m=n=4
def goldmax(gold):
    goldtable=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for col in range(n-1,-1,-1):
        for row in range(m):
            if col==n-1:
                right=0 
            else:
                right=goldtable[row][col+1]
            if col==n-1 or row==0:
                right_up=0
            else:
                right_up=goldtable[row-1][col+1]
            if col==n-1 or row==n-1:
                right_down=0
            else:
                right_down=goldtable[row+1][col+1]
            goldtable[row][col]=gold[row][col]+max(right,right_down,right_up)
    res=goldtable[0][0]
    for i in range(m):
        res=max(res,goldtable[i][0])
    return res 

gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]
        
print(goldmax(gold))