m = n = 4
def Nqueen():
    b = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if Nqueenu(b, 0) == False:
        return False 
    printsol(b)
def Nqueenu(b,col):
    if col >= n:
        return True 
    for i in range(n):
        if issafe(b, i, col):
            b[i][col] = 1 
            if Nqueenu(b, col+1):
                return True 
            b[i][col] = 0 
    return False 

def issafe(b, row, col):
    for i in range(col):
        if b[row][i] == 1:
            return False
    for i, j in zip(range(row,-1,-1),range(col,-1,-1)):
        if b[i][j] == 1:
            return False 
    for i, j in zip(range(row, n), range(col,-1,-1)):
        if b[i][j] == 1:
            return False 
    return True 

def printsol(b):
    for i in range(n):
        for j in range(n):
            print(b[i][j], end= " ") 
        print()

def mazesolver(maze):
    sol = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if mazesolveru(maze, 0, 0, sol) == False:
        return False 
    printsol(sol)
def mazesolveru(maze, x, y, sol):
    if x == n-1 and y == n-1 and maze[x][y] ==1:
        sol[x][y] = 1
        return True 
    if issafemaze(maze, x, y):
        if sol[x][y] ==1:
            return False 
        sol[x][y] = 1
        if mazesolveru(maze, x+1, y, sol):
            return True 
        if mazesolveru(maze, x, y+1, sol):
            return True 
        if mazesolveru(maze, x, y-1, sol):
            return True 
        if mazesolveru(maze, x-1, y, sol):
            return True 
        sol[x][y] = 0 
    return False 
def issafemaze(maze, i, j):
    if i>=0 and i<m and j>=0 and j<n and maze[i][j] == 1:
        return True 
    return False 

def goldmax(gold):
    gt = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m = len(gold)
    n = len(gold[0])
    for col in range(n):
        for row in range(m):
            if col == 0:
                left = 0 
            else:
                left = gt[row][col-1]
            if col ==0 or row == 0:
                left_up =0 
            else:
                left_up = gt[row-1][col-1]
            if col ==0 or row == m-1:
                left_down = 0 
            else:
                left_down = gt[row+1][col-1]
            gt[row][col] = gold[row][col] + max(left, left_down, left_up)
    res = gt[0][n-1]
    for i in range(m):
        res = max(res, gt[n-1][i])
    return res

def Lcs(x, y):
    m = len(x)
    n = len(y)
    if m == 0 or n ==0:
        return -1 
    dp =[[0 for _ in range(n+1)]for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def MinimumCostPath(grid, x, y):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)]for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]

def UniquePath(m, n):
    if m ==0 or n==0:
        return -1 
    dp = [[1 for _ in range(n)]for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

def RegularExpression(sti, pattern):
    m = len(sti)
    n = len(pattern)
    if m ==0 or n ==0 :
        return -1 
    dp = [[False for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = True 
    for i in range(1, n+1):
        if pattern[i-1] == "*":
            dp[0][i] = dp[0][i-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if pattern[j-1] == "." or sti[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1]
            if pattern[j-1] == "*":
                dp[i][j] = dp[i][j-2]
                if pattern[j-2] == '*' or sti[i-1] == pattern[j-2]:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]

def eggs_max(f, n):
    dp = [[0 for _ in range(n+1)]for _ in range(f+1)]
    for i in range(1, f+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
        if dp[i][j] >= f:
            return i 
import numpy as np 
run_max = np.maximum.accumulate 
def Water_collector(height):
    a = np.array(height)
    global_max = np.argmax(a)
    return np.sum(run_max(a[:global_max])- a[:global_max], dtype = np.int64) +\
            np.sum(run_max(a[:global_max:-1])- a[:global_max:-1], dtype = np.int64)

def TrainTixMin(days, costs):
    dp = [-1 for _ in range(366)]
    dp[0] = 0 
    for day in days:
        dp[day] = 0 
    for i in range(1, 366):
        if dp[i] == -1:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[i-1]+costs[0], 
                        dp[max(i-7, 0)] + costs[1], 
                        dp[max(i-30, 0)] + costs[2])
    return dp[365]

def CoinChange(coins, amount):
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0 
    for currrent_amount in range(1, amount+1):
        for coin in coins :
            if currrent_amount - coin >= 0:
                dp[currrent_amount] = min(dp[currrent_amount], dp[currrent_amount - coin] + 1)
    if dp[-1] == float('inf'):
        return - 1
    return dp

def NumIslands(grid):
    m = len(grid)
    n = len(grid[0])
    if m==0 or n==0:
        return -1 
    grid = [[int(grid[i][j]) for j in range(n)]for i in range(m)]
    count = 0 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                count += HelperIsland(grid, i, j)
    return count 
def HelperIsland(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] != 1:
        return 0 
    grid[i][j] = -1
    neighbours = ((0,1),(1,0),(-1,0),(0,-1))
    for dx, dy in neighbours:
        HelperIsland(grid, i+dx, j+dy)
    return 1 

def CountIslands(grid):
    m = len(grid)
    n = len(grid[0])
    if m ==0 or n ==0 :
        return -1 
    grid = [[int(grid[i][j]) for j in range(n)]for i in range(m)]
    count, q= 0, []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                res = HelperCount(grid, i, j, count)
                q.append(res)
    final = q[0]
    for i in range(len(q)):
        final = max(final, q[i])
    return final 

def HelperCount(grid, i, j, count):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
        return count 
    grid[i][j] = -1 
    phi = HelperCount(grid, i+1, j, count+1)
    psi = HelperCount(grid, i, j+1, count+1)
    mu = HelperCount(grid, i-1, j, count+1)
    nu = HelperCount(grid, i, j-1, count+1)
    return max(phi, psi, mu, nu)

def WordSearch(grid, word):
    m = len(grid)
    n = len(grid[0])
    if m ==0 or n ==0:
        return -1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == word[0] and HelperWord(grid, word, i, j, 0):
                return True 
    return False 

def HelperWord(grid, word, i, j, count):
    if count == len(word):
        return True 
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != word[count]:
        return 
    grid[i][j] = -1 
    boolean = HelperWord(grid, word, i+1, j, count+1) or \
              HelperWord(grid, word, i-1, j, count+1) or \
              HelperWord(grid, word, i, j+1, count+1) or \
              HelperWord(grid, word, i, j-1, count+1) 
    return boolean 

def Surrounding(grid):
    m = len(grid)
    n = len(grid[0])
    if m ==0 or n ==0:
        return -1 
    for i in range(m):
        if grid[i][0] == "O":
            HelperSurround(grid, i, 0)
    for i in range(m):
        if grid[i][n-1] == "O":
            HelperSurround(grid, i, n-1)
    for i in range(n):
        if grid[0][i] == "O":
            HelperSurround(grid, 0, i)
    for i in range(n):
        if grid[n-1][i] == "O":
            HelperSurround(grid, n-1, i)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == -1:
                grid[i][j] = "O"
            elif grid[i][j] == "O":
                grid[i][j] = "X"
    printgrid(grid)

def HelperSurround(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 'O':
        return 
    grid[i][j] = -1 
    neighbours = ((0,1),(0,-1),(1,0),(-1,0))
    for dx, dy in neighbours:
        HelperSurround(grid, i+dx, j+dy)
    return 

def Subsets(arr):
    return [[arr[i] for i in range(len(arr)) if bits & 1<<i != 0]for bits in range(1<<len(arr))]

def Subsets2(arr):
    n = len(arr)
    solution = [[]]
    for i in arr:
        solution += [current + [i] for current in solution]
    return solution

def Partitions(O, P):
    if P == 1:
        return 1 
    elif P ==0 or O < 0:
        return 0 
    else:
        return Partitions(O-P, P) + Partitions(O, P-1)
def Maxlength(arr):
    solution = ['']
    res= 0 
    for  i in arr:
        for string in solution:
            temp = string + i 
            if isvalid(temp):
                solution.append(temp)
                res = max(res, len(temp))
    return res

def isvalid(sti):
    return len(sti) == len(set(sti))

def printgrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end= " ")
        print()

def SpiralMatrix(grid):
    m = len(grid)
    n = len(grid[0])
    if m ==0 or n ==0:
        return -1 
    Top, Bottom, Left, Right, arr, arr_max = 0, m-1, 0 , n-1, [], m*n
    while len(arr) < arr_max:
        for i in range(Left, Right+1):
            if len(arr) < arr_max:
                arr.append(grid[Top][i])
        Top += 1

        for i in range(Top, Bottom+1):
            if len(arr) < arr_max:
                arr.append(grid[i][Right])
        Right  -= 1

        for i in range(Right, Left-1, -1):
            if len(arr) < arr_max:
                arr.append(grid[Bottom][i])
        Bottom -=1 

        for i in range(Bottom, Top-1, -1):
            if len(arr) < arr_max:
                arr.append(grid[i][Left])
        Left += 1

    return arr 

def AntiSpiralMatrix(grid):
    m = len(grid)
    n = len(grid[0])
    if m ==0 or n ==0:
        return -1 
    Top, Bottom, Left, Right, arr, arr_max = 0, m-1, 0, n-1, [], m*n
    while len(arr) < arr_max:
        for i in range(Right, Left -1 , -1):
            if len(arr) < arr_max:
                arr.append(grid[Top][i])
        Top += 1

        for i in range(Top, Bottom+1):
            if len(arr) < arr_max:
                arr.append(grid[i][Left])
        Left += 1

        for i in range(Left, Right+1):
            if len(arr) < arr_max:
                arr.append(grid[Bottom][i])
        Bottom -= 1

        for i in range(Bottom, Top-1, -1):
            if len(arr) < arr_max:
                arr.append(grid[i][Right])
        Right -= 1
    return arr 

def Permutations(arr):
    n = len(arr)
    if n ==0:
        return -1 
    res = []
    Helper(arr, [], res)
    return res 

def Helper(arr, path, res):
    if not arr:
        res.append(path)
    for i in range(len(arr)):
        Helper(arr[:i] + arr[i+1:], path + [arr[i]], res)
def StairClimbing(n):
    if n<=2:
        return n 
    else:
        return StairClimber(n-1) + StairClimber(n-2) + StairClimber(n-3)
def StairClimber(n):
    previous = 0 
    final = 1
    while n>0:
        temp = previous + final
        previous = final 
        final = temp 
        n -= 1
    return final 

def Frequencysort(sti):
    n = len(sti)
    if n == 0:
        return ''
    my_dict, q, solution = dict(), [], ''
    for i in sti:
        if i in my_dict.keys():
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for i in my_dict.values():
        q.append(i)
    q.sort()
    q = q[::-1]
    for i in q:
        for j,k in my_dict.items():
            if k == i:
                solution += j*k
                break 
        del my_dict[j]
    return solution

def NextClosestTime(time):
    h, m = time.split(':')
    m = m[0:2]
    minutes = int(h) * 60 + int(m)
    for i in range(minutes+1, minutes+1441):
        temp = i%1440
        h, m = temp//60, temp % 60
        answer = '{:02d}:{:02d}'.format(h, m)
        if set(answer) <= set(time):
            if int(answer[0:2]) < 12:
                return answer + ' AM'
            else:
                return answer + ' PM'
matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8],
          [9,10,11,12]]
          
print(AntiSpiralMatrix(matrix))


                

