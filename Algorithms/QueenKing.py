def KingandQueen(queens, kings):
    max_len, q = maxlength(queens, kings), []
    dp = FormBoard(queens, kings, max_len)
    for i in range(max_len +1):
        for j in range(max_len + 1):
            if dp[i][j] == "Q" and Solver(dp, i, j):
                q.append([i, j])
    return q 

def Solver(dp, i, j):
    if i<0 or i>=len(dp) or j<0 or j>=len(dp[0]) or dp[i][j] != "Q":
        return False 
    if CheckDirection('Left', i, j, dp) or CheckDirection('Right', i, j, dp)   or \
       CheckDirection('Up', i, j, dp)   or CheckDirection('Down', i, j, dp)    or \
       CheckDiagonal('LU', i, j, dp)    or CheckDiagonal('LD', i, j, dp)       or \
       CheckDiagonal('RD', i, j, dp)    or CheckDiagonal('RU', i, j, dp) :
        return True
    return False 

def CheckDirection(direction, row, col, dp):
    direction_mapper = {'Left' : 0, 'Right' : 1, 'Up' : 2, 'Down' : 3}
    q = [(col-1, -1, -1, row), (col+1, len(dp[0]), 1, row), (row-1,-1, -1, col), (row+1, len(dp), 1, col)]
    start, end, step, static = q.pop( direction_mapper[ direction ])
    flag_queen, flag_king = 0, 0
    if row == col:
        if direction == 'Up' or direction == 'Down':
            for i in range(start, end, step):
                if dp[i][col] == "Q":
                    flag_queen = 1
                elif dp[i][col] == "K":
                    flag_king = 1
                if CheckFlag(flag_queen, flag_king):
                    return True 
        elif direction == 'Left' or direction =='Right':
            for i in range(start, end, step):
                if dp[row][i] == "Q":
                    flag_queen = 1
                elif dp[row][i] == "K":
                    flag_king = 1
                if CheckFlag(flag_queen, flag_king):
                    return True 
    elif static == row: 
        for i in range(start, end, step):
            if dp[row][i] == "Q":
                flag_queen = 1
            elif dp[row][i] == "K":
                flag_king = 1
            if CheckFlag(flag_queen, flag_king):
                return True 
    elif static == col:
        for i in range(start, end, step):
            if dp[i][col] == "Q":
                flag_queen = 1
            elif dp[i][col] == "K":
                flag_king = 1
            if CheckFlag(flag_queen, flag_king):
                return True 
    return False 

def CheckDiagonal(direction, row, col, dp):
    direction_mapper = {'LU' : 0, 'LD' : 1, 'RU' : 2, 'RD' : 3}
    q = [(row-1, -1, -1, col-1, -1, -1), (row+1, len(dp), 1, col-1, -1, -1), \
         (row-1, -1, -1, col+1, len(dp[0]), 1), (row+1, len(dp), 1, col+1, len(dp[0]), 1)]
    start, end, step, start1, end1, step1 = q.pop( direction_mapper[direction] )
    flag_queen, flag_king = 0, 0
    for i, j in zip(range(start, end, step), range(start1, end1, step1)):
        if dp[i][j] == "Q":
            flag_queen = 1
        elif dp[i][j] == "K":
            flag_king = 1
        if CheckFlag(flag_queen, flag_king):
            return True
    return False

def CheckFlag(flag_queen, flag_king):
    if flag_queen == 0 and flag_king == 1:
        return True 
    return False 

def maxlength(queens, kings):
    length = 0 
    for queen in queens:
        length = max(length, queen[0], queen[1], kings[0], kings[1])
    return length 

def FormBoard(queens, kings, max_len):
    dp = [[0 for _ in range(max_len+1)]for _ in range(max_len+1)]
    for queen in queens:
        dp[ queen[0] ][ queen[1] ] = 'Q'
    dp[ kings[0] ][ kings[1] ] = 'K'
    return dp 


queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
king = [3,3]
print(KingandQueen(queens, king))