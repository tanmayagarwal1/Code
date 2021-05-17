import numpy as np 
run_max = np.maximum.accumulate
def lcs(x, y):
    m = len(x)
    n = len(y)
    if m ==0 or n ==0:
        return False 
    dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
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
    if m ==0 or n == 0:
        return False
    dp = [[0 for _ in range(n)]for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, n+1):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = min( dp[i-1][j-1], dp[i-1][j], dp[i][j-1] ) + grid[i][j]
    return dp[x][y]

def UniquePath(m, n):
    if m == 0 or n == 0:
        return -1 
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
def regularexpression(sti, pattern):
    m = len(sti)
    n = len(pattern)
    if m == 0 or n == 0:
        return -1 
    dp = [[False for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        if pattern[i-1] == '*':
            dp[0][i] = dp[0][i-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if pattern[j-1] == '.' or sti[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-2]
            if pattern[j-1] == '.':
                dp[i][j] = dp[i][j-2]
                if pattern[j-2] == '.' or sti[i-1] == pattern[j-2]:
                    dp[i][j] = dp[i-1][j]
    return dp[m][n]

def Egss_max(f, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, f+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
        if dp[i][j] >= f:
            return i 
def water_collector(height):
    a = np.array(height)
    global_max = np.argmax(a)
    return np.sum(run_max(a[:global_max]) - a[:global_max], dtype = np.int64) +\
            np.sum(run_max(a[global_max:-1]) - a[:global_max:-1], dtype = np.int64)

def Traintix(days, costs):
    dp = [-1 for _ in range(366)]
    dp[0] = 0
    for day in days:
        dp[day] = 0 
    for i in range(1, 366):
        if dp[i] == -1:
            dp[i] = dp[i-1]
        else:
            dp[i] = min( dp[i-1]+ costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
    return dp[365]

def CoinChange(coins, ammount):
    dp = [float('inf') for _ in range(ammount+1)]
    dp[0] = 0 
    for i in range(1, ammount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[-1]

def NumIslands(grid):
    m = len(grid)
    n = len(grid[0])
    if m == 0 or n == 0 :
        return - 1
    grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                count += HelperIsland(grid, i, j)
    return count 

def HelperIsland(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
        return 0 
    grid[i][j] = -1
    neighbours = ((0,1),(0,-1),(1,0),(-1,0))
    for dx, dy in neighbours:
        HelperIsland(grid, i+dx, j+dy)
    return 1

def Countisland(grid):
    m = len(grid)
    n = len(grid[0])
    if m == 0 or n == 0:
        return -1 
    grid = [[int(grid[i][j])for j in range(len(grid[0]))]for i in range(len(grid))]
    count, q = 0, []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                x = HelperCount(grid, count, i, j)
                q.append(x)
    return q 

def HelperCount(grid, count, i, j):
    if i < 0 or i >=len(grid) or j< 0 or j>=len(grid[0]) or grid[i][j] != 1:
        return count 
    grid[i][j] = -1 
    phi = HelperCount(grid, count + 1, i+1, j)
    psi = HelperCount(grid, count + 1, i, j+1)
    mu  = HelperCount(grid, count + 1, i-1, j)
    nu  = HelperCount(grid, count + 1, i, j-1)

    return max(phi, psi, mu, nu)

def Surrounded(grid):
    m = len(grid)
    n = len(grid[0])
    if m == 0 or n == 0:
        return - 1
    for i in range(n):
        if grid[0][i] == "O":
            Helpersurround(grid, 0, i)
    for i in range(n):
        if grid[m-1][i] == "O":
            Helpersurround(grid, m-1, i)
    for i in range(m):
        if grid[i][0] == "O":
            Helpersurround(grid, i, 0)
    for i in range(m):
        if grid[i][n-1] == 'O':
            Helpersurround(grid, i, n-1)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == -1:
                grid[i][j] = "O"
            elif grid[i][j] == "O":
                grid[i][j] = "X"
    printgrid(grid)

def HelperSurround(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid) or grid[i][j] != "O":
        return 
    grid[i][j] = - 1
    neighbours = ((0,1),(0,-1),(1,0),(-1,0))
    for dx, dy in neighbours:
        Helpersurround(grid, i+dx, j+dy)
    return 

def Stairclimbing(n):
    i = 0 
    j = 1 
    while n>0:
        temp = i+j 
        i = j 
        j = temp
        n -= 1
    return j 

def Stairs(n):
    if n<=2:
        return n 
    else:
        return Stairclimbing(n-1) + Stairclimbing(n-2) + Stairclimbing(n-3)
print(Stairs(5))

def Subsets(arr):
    return [[arr[i] for i in range(len(arr)) if bit & 1<<i != 0]for bit in range(1<<len(arr))]

def Subsets2(arr):
    if len(arr) == 0:
        return []
    solution = [[]]
    for i in arr:
        solution += [current + [i] for current in solution]
    return solution

def Partition(O, P):
    if P == 1:
        return 1 
    elif P == 0 or O < 0:
        return 0 
    else:
        return Partition(O-P, P) + Partition(O, P-1)

def Permutations(arr):
    if len(arr) == 0:
        return -1 
    res = []
    Permutator(arr, [], res)
    return res 

def Permutator(arr, path, res):
    if not arr:
        res.append(path)
    for i in range(len(arr)):
        Permutator(arr[:i] + arr[i+1 :], path + [arr[i]], res)

def Combinations(arr, target):
    if len(arr) == 0:
        return 
    res = []
    Combinator(arr, target, 0, [], res)
    return res 

def Combinator(arr, target, index, path, res):
    if target < 0 :
        return 
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(arr)):
        Combinator(arr, target - arr[i], i, path + [arr[i]], res)

print(Partition(5, 3))
