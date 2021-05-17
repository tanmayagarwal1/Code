def KingandQueen(queens, kings):
    max_len, q = maxlength(queens, kings), [] # The function maxlength() returns the maximum number among the given list of queens and kings
    dp = FormBoard(queens, kings, max_len)    # FormBoard() function retuns the board of size max_len * max_len
    for i in range(max_len +1):
        for j in range(max_len + 1):
            if dp[i][j] == "Q" and Solver(dp, i, j): # Whenever we encounter a queen on the board we call the Solver
                q.append([i, j])    # If the co-ordinates of the queen match all the criterias, they are appended in the queue 
    return q # Return the Queue 

def Solver(dp, i, j):
    if i<0 or i>=len(dp) or j<0 or j>=len(dp[0]) or dp[i][j] != "Q":
        return False 

    ''' Now we check all the 8 directions. I have defined two funcitons for doing this task. The first function, CheckDirection, 
        checks the four directions of Left, Right, Up and Down and the second function, CheckDiagonal, checks the four diagonals,
        Left_up(LU), Left_down(LD), Right_up(RU), and Right_down(RD). If any of the directions return a True, that means the paticular
        queen can attack the king and hence all the fuction calls are logically OR'ed'''

    if CheckDirection('Left', i, j, dp) or CheckDirection('Right', i, j, dp)   or \
       CheckDirection('Up', i, j, dp)   or CheckDirection('Down', i, j, dp)    or \
       CheckDiagonal('LU', i, j, dp)    or CheckDiagonal('LD', i, j, dp)       or \
       CheckDiagonal('RD', i, j, dp)    or CheckDiagonal('RU', i, j, dp) :
        return True
    # If all the directions return a False, the king cannot be attacked by the paticular queen and hence return False
    return False 

def CheckDirection(direction, row, col, dp):

    ''' This function is used to check the four mainstream directions. The four directions are indexd into the dictionary
        'direction_mapper'. Next a queue is defined which holds the start, end, step and static variables of the for loop, for each 
        paticular direction. What I mean by static here is the fact that, if our direction is Up or Down, we move through
        only the rows and hence the column remain static. Similarly, While moving Right or Left, we move along the columns 
        and the row remains static. So, for each direction I have also added a static variable to signify which part(row or column)
        remains static while moving in a paticluar direction '''

    direction_mapper = {'Left' : 0, 'Right' : 1, 'Up' : 2, 'Down' : 3}

    ''' The bounds are as follows 
        1. Left : we start one column before the current column(at which the current queen is placed) and go till the first column. Hence, 
                  start = col -1, end = -1 (As end is -1, the for loop stops at 0), step = -1 (We are moving backwards), 
                  static = row (as we move through the columns)
        2. Right : we start from the next column, of the current column and stop only if we reach the last column. Hence :
                   start = col+1, end = len(dp[0]) (The last column), step = 1 ( We are moving forwards), static = row (column wise movement)
        3. Up    : we start from the previous row of the current row and move till the last row. Hence, 
                   start = row - 1, end = -1, step = -1 ( Moving backwards ), static = col (As we move through the rows)
        4. Down  : we start from the next row of the current row, and move till we reach the last row. hence 
                   start = row + 1, end = len(dp) (Which gives the last row), step = 1 (forward movement), static = col'''


    q = [(col-1, -1, -1, row), (col+1, len(dp[0]), 1, row), (row-1,-1, -1, col), (row+1, len(dp), 1, col)]
    start, end, step, static = q.pop( direction_mapper[ direction ])

    ''' Now we reach the part where I have declared two flags : flag_queen and flag_king. At each iteration, if a queen is in our path, flag_queen is set to 1
        and if a king in in our path, flag_king is set to 1. NOTE : for a queen to successfully attack a king, it should encounter a king in its path, 
        before it encounters any other queen. We keep this fact in our mind and at every point of the iteration, we check: IF flag_king is one( Which 
        means we have encountered a king) AND flag_queen is zero ( which means we have not encountered a queen yet), the function returns True, or else False.
        This check of flags is performed by the CheckFlag() function'''


    flag_queen, flag_king = 0, 0
    if row == col:

        ''' One non trivial thing which happens is when the row number = column number in the co-ordinates of the queen. During this time
            I had to explicitly define the loops to ensure that the static column or the row is choosen. This loop works the following way :
            if row number == column number, it checks the direction. If the direction is Up or Down, The column is set static. Else-If the 
            direction is Left or Right, the row is set static'''

        if direction == 'Up' or direction == 'Down':
            for i in range(start, end, step):
                if dp[i][col] == "Q":                  
                    flag_queen = 1  # If encountered Queen, flag_queen is set to 1
                elif dp[i][col] == "K":
                    flag_king = 1  # If encountered King, flag_king is set to 2
                if CheckFlag(flag_queen, flag_king): # Function to check both the flags at every point 
                    return True 
        elif direction == 'Left' or direction =='Right':
            for i in range(start, end, step):
                if dp[row][i] == "Q":
                    flag_queen = 1
                elif dp[row][i] == "K":
                    flag_king = 1
                if CheckFlag(flag_queen, flag_king):
                    return True 

    # This part is for when row number != Column Number

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

    ''' Here we define the directions : Left_up (LU), Left_Down(LD), Right_Up(RU) and Right_Down(RD).
        Here we have 6 variables in each tuple of our queue. First off, there are total of 4 tuples in 
        the queue referring to the four directions. Now each tuple contains : start, end, step, start1, end1, step1.
        The start, end, step is for the row and start1, end1, step1 is for the column. In a diagonal movement, neither the 
        row nor the column remains static at any point hence we specify the ranges for both row and col'''

    direction_mapper = {'LU' : 0, 'LD' : 1, 'RU' : 2, 'RD' : 3}

    '''The bounds are :

    1. Left Up    : The row starts from the previous row and ends at the first row with a negative one step 
                    and the column starts from the previous column, going till the first column with a negative step
    2. Left Down  : The row start from the next row and iterates till it reaches the final row which is (len(dp)) 
                    and the column starts from the previous column all the way to the first column with a negative step 
    3. Right Up   : The row starts from the previous row and iterates all the way to the first, and the column starts from 
                    the next column all the way to the last 
    4. Right Down : The row starts from the next row, and the column too from the next column and they both end at the last
                    row and column respectively  '''



    q = [(row-1, -1, -1, col-1, -1, -1), (row+1, len(dp), 1, col-1, -1, -1), \
         (row-1, -1, -1, col+1, len(dp[0]), 1), (row+1, len(dp), 1, col+1, len(dp[0]), 1)]
    start, end, step, start1, end1, step1 = q.pop( direction_mapper[direction] )
    flag_queen, flag_king = 0, 0 # Same idea as previous function 
    
    for i, j in zip(range(start, end, step), range(start1, end1, step1)): #zip is used to iterate through both the specified counds of rows and cols Together
        if dp[i][j] == "Q":
            flag_queen = 1
        elif dp[i][j] == "K":
            flag_king = 1
        if CheckFlag(flag_queen, flag_king):
            return True
    return False

def CheckFlag(flag_queen, flag_king): # Trivial defination
    if flag_queen == 0 and flag_king == 1:
        return True 
    return False 

def maxlength(queens, kings): # This function returns the max number in the given lists 
    length = 0 
    for queen in queens:
        length = max(length, queen[0], queen[1], kings[0], kings[1])
    return length 

def FormBoard(queens, kings, max_len): # This returns a board of size max_len * max_len 
    dp = [[0 for _ in range(max_len+1)]for _ in range(max_len+1)]
    for queen in queens:
        dp[ queen[0] ][ queen[1] ] = 'Q'
    dp[ kings[0] ][ kings[1] ] = 'K'
    return dp 


queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
king = [3,3]
print(KingandQueen(queens, king))