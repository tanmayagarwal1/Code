'''
This version of the solution is meant only for understanding purposes and it fails certain edge cases. 
For a shorter and more conciece solutions view the QueenKing(short) solution

'''

def KingandQueen(queens, kings):
    max_tuple = max(queens)
    max_len = max(max_tuple[0], max_tuple[1])
    q = []
    dp = [[0 for _ in range(max_len+1)]for _ in range(max_len+1)]
    for i in queens:
        dp[i[0]][i[1]] = 'Q'
    dp[king[0]][king[1]] = 'K'
    for i in range(max_len +1):
        for j in range(max_len + 1):
            if dp[i][j] == "Q":
                if Helper(dp, i, j):
                    q.append([i, j])
    return q 

    printsol(dp) # Only for viewing the board (debugging)

def Helper(dp, i, j):
    if i<0 or i>=len(dp) or j<0 or j>=len(dp[0]) or dp[i][j] != "Q":
        return False 

    flag1 = flag2 = 0 
    for col in range(j-1, -1, -1): #Left 
        if dp[i][col] == "Q":
            flag1 = 1
        if dp[i][col] == "K":
            flag2 = 1 
        if checkWhileMoving(flag1, flag2):  
            return True 
    flag1 = flag2 = 0
    for row, col in zip(range(i-1, -1, -1), range(j-1, -1,-1)): # Left Up diagonal 
        if dp[row][col] == "Q":
            flag1 = 1 
        elif dp[row][col] == "K":
            flag2 = 1
        if checkWhileMoving(flag1, flag2):
            return True 
    flag1 = flag2 = 0
    for row, col in zip(range(i+1, len(dp)), range(j-1, -1, -1)): # Left Down Diagonal 
        if dp[row][col] == "Q":
            flag1 = 1 
        elif dp[row][col] == 'K':
            flag2 = 1
        if checkWhileMoving(flag1, flag2):
            return True
    flag1 = flag2 = 0
    for row in range(i-1, -1, -1): #Full Up 
        if dp[row][j] == "Q":
            flag1 = 1
        elif dp[row][j] == 'K':
            flag2 = 1 
        if checkWhileMoving(flag1, flag2):
            return True
    flag1 = flag2 = 0 
    for row in range(i+1, len(dp)): #Full Down 
        if dp[row][j] == "Q":
            flag1 = 1
        elif dp[row][j] == 'K':
            flag2 = 1 
        if checkWhileMoving(flag1, flag2):
            return True
    flag1 = flag2 = 0
    for col in range(j+1, len(dp[0])):
        if dp[i][col] == 'Q':
            flag1 = 1 
        elif dp[i][col] == 'K':
            flag2 = 1
        if checkWhileMoving(flag1, flag2):
            return True 
    flag1 = flag2 = 0 
    for row, col in zip(range(i-1, -1, -1), range(j+1, len(dp[0]))):
        if dp[row][col] == 'Q':
            flag1 = 1
        elif dp[row][col] == 'K':
            flag2 = 1
        if checkWhileMoving(flag1, flag2):
            return True 
    flag1 = flag2 = 0
    for row, col in zip(range(i+1, len(dp)), range(j+1, len(dp[0]))):
        if dp[row][col] == 'Q':
            flag1 = 1
        elif dp[row][col] == "K":
            flag2 = 1 
        if checkWhileMoving(flag1, flag2):
            return True 
    flag1 = flag2 = 0 
    return False 


def Judge(flag1, flag2):
    if flag1 == 1:
        return False 
    elif flag1 == 1 and flag2 == 1:
        return False
    elif flag1 == 0 and flag2 == 1:
        return True 
    return False

def checkWhileMoving(flag1, flag2):
    if flag1 == 0 and flag2 == 1:
        return True 
    return False 

def printsol(dp): #Only for seeing the board 
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print(dp[i][j], end = " ")
        print()

queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king = [3,4]
print(KingandQueen(queens, king))