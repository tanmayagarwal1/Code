m=n=4
def nqueen():
    b=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if nqueenu(b,0)==False:
        return False 
    printsol(b)
def nqueenu(b,col):
    if col>=n:
        return True 
    for i in range(n):
        if issafe(b,i,col):
            b[i][col] = 1
            if nqueenu(b, col+1):
                return True
            b[i][col]=0
    return False 
def issafe(b,row,col):
    for i in range(col):
        if b[row][i] == 1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if b[i][j]==1:
            return False 
    for i,j in zip(range(row,n),range(col,-1,-1)):
        if b[i][j]==1:
            return False 
    return True 

def mazesolver(maze):
    sol=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if mazesolveru(maze,0,0,sol)==False:
        return False 
    printsol(sol)
def mazesolveru(maze,x,y,sol):
    if x==n-1 and y==n-1 and maze[x][y]==1:
        sol[x][y]=1
        return True 
    if issafemaze(maze,x,y):
        if sol[x][y]==1:
            return True 
        sol[x][y]=1
        if mazesolveru(maze,x+1,y,sol):
            return True 
        if mazesolveru(maze,x,y+1,sol):
            return True 
        if mazesolveru(maze,x-1,y,sol):
            return True 
        if mazesolveru(maze,x,y-1,sol):
            return True 
        sol[x][y]=0 
    return False 

def issafemaze(maze,x,y):
    if x>=0 and x<n and y>=0 and y<n and maze[x][y]==1:
        return True 
    return False 
def goldmax(gold):
    gt=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m=len(gold)
    n=len(gold[0])
    for col in range(n):
        for row in range(m):
            if col==0:
                left = 0 
            else:
                left = gt[row][col-1]
            if col==0 or row==0:
                left_up = 0
            else:
                left_up = gt[row-1][col-1]
            if col==0 or row==m-1:
                left_down = 0 
            else:
                left_down = gt[row+1][col-1]
            gt[row][col]=gold[row][col] + max(left,left_down,left_up)
    res=gt[0][m-1]
    for i in range(m):
        res = max(res, gt[i][m-1])
    return res 

def printsol(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()

def NumIslands(grid):
    m=len(grid)
    n=len(grid[0])
    if m==0 or n==0:
        return -1 
    count = 0 
    grid=[[int(grid[i][j])for j in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                count += NumIsHelper(grid, i, j)
    return count 

def NumIsHelper(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
        return 0 
    grid[i][j] = -1
    neighbours = ((0,1),(0,-1),(1,0),(-1,0))
    for dx, dy in neighbours:
        NumIsHelper(grid, i+dx, j+dy)
    return 1

def AntiSpiralMatrix(grid):
    m=len(grid)
    n=len(grid[0])
    if m==0 or n==0:
        return -1 
    Top, Left, Right, Bottom, arr, max_arr = 0, 0, n-1, m-1, [], m*n
    while len(arr)< max_arr:
        for i in range(Right, Left-1, -1):
            if len(arr)<max_arr:
                arr.append(grid[Top][i])
        Top += 1

        for i in range(Top, Bottom+1):
            if len(arr)<max_arr:
                arr.append(grid[i][Left])
        Left +=1

        for i in range(Left, Right+1):
            if len(arr)<max_arr:
                arr.append(grid[Bottom][i])
        Bottom -= 1

        for i in range(Bottom, Top-1, -1):
            if len(arr)<max_arr:
                arr.append(grid[i][Right])
        Right -=1

    return arr 

def Surrounded(grid):
    m=len(grid)
    n=len(grid[0])
    if m==0 or n==0:
        return -1 
    for i in range(m):
        if grid[i][0] == "O":
            Helper(grid, i, 0)
    for i in range(m):
        if grid[i][n-1] == "O":
            Helper(grid, i, n-1)
    for i in range(n):
        if grid[0][i] == "O":
            Helper(grid, 0, i)
    for i in range(n):
        if grid[m-1][i] == "O":
            Helper(grid, m-1, i)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == -1:
                grid[i][j] = "O"
            elif grid[i][j] == "O":
                grid[i][j] = "X"
    printgrid(grid)

def Helper(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != "O":
        return 
    grid[i][j] = -1 
    neighbours=((0,1),(0,-1),(1,0),(-1,0))
    for dx, dy in neighbours:
        Helper(grid, i+dx, j+dy)
    return 
def printgrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[1])):
            print(grid[i][j],end=" ")
        print()

def WordSearch( grid, word):
    m=len(grid)
    n=len(grid[0])
    if m==0 or n==0 :
        return -1 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == word[0] and WordHelper(grid, word, i, j, 0):
                return True 
    return False

def WordHelper(grid, word, i, j, count):
    if count == len(word):
        return True 
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != word[count]:
        return False 
    grid[i][j] = -1
    Boolean = WordHelper(grid, word, i+1, j, count+1) or \
              WordHelper(grid, word, i, j+1, count+1) or \
              WordHelper(grid, word, i-1, j, count+1) or \
              WordHelper(grid, word, i, j-1, count+1) 
    return Boolean 

def lcs(x,y):
    m=len(x)
    n=len(y)
    dp=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1 ):
            if x[i-1] == y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

def egg_max(f, n):
    dp=[[0 for i in range(n+1)]for j in range(f+1)]
    for i in range(1,f+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j] + 1
        if dp[i][j] >=f:
            return i 

def regularexpression(sti, pattern):
    m=len(sti)
    n=len(pattern)
    if m==0 or n==0:
        return -1 
    dp=[[False for i in range(n+1)]for j in range(m+1)]
    dp[0][0]= True 
    for i in range(1, n+1):
        if pattern[i-1] == "*":
            dp[0][i] = dp[0][i-2]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if pattern[j-1] == "." or sti[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1]
            if pattern[j-1] == "*":
                dp[i][j] = dp[i][j-2]
                if pattern[j-2] =="." or sti[i-1] ==pattern[j-2]:
                    dp[i][j]=dp[i-1][j]
    return dp[m][n]

def UniquePaths(m, n):
    if m==0 or n==0:
        return -1 
    dp = [[0 for i in range(n)]for j in range(m)]
    for i in range(n):
        dp[0][i] = 1
    for j in range(m):
        dp[j][0] = 1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[m-1][n-1]

def Minimumcost(grid, x, y):
    m=len(grid)
    n=len(grid[0])
    if m==0 or n==0:
        return -1 
    dp = [[0 for i in range(n)]for j in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j]= min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+grid[i][j]
    return dp[x][y]


def NextClosestTime(time):
    h, m = time.split(":")
    m = m[0:2]
    minutes = int(h)*60 + int(m)
    for i in range(minutes+1, minutes+1441):
        NewTime = i % 1440 
        h, m = NewTime//60, NewTime % 60 
        NewTime = "{:02d}:{:02d}".format(h, m)
        if set(NewTime) <= set(time):
            if int(NewTime[0:2]) < 12:
                return NewTime+" AM"
            else:
                return NewTime+" PM"


def dups(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] ==arr[j]:
                print(arr[j])
def dups2(arr):
    n=len(arr)
    s=set()
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
        else:
            print(arr[i])

def Blocks(arr, interets):
    q=[]
    for i in arr:
        count = 0
        for j,k in i.items():
            for z in range(len(interets)):
                if j==interets[z] and k==True:
                    count +=1
        q.append(count)
    res=q[0]
    for i in range(len(q)):
        res=max(res,q[i])
    return q.index(res)+1

def Houses(arr, b):
    q=[]
    for i in range(n):
        if arr[i]>b:
            continue 
        initial = arr[i]
        count = 1 
        for j in range(n):
            if i==j:
                continue 
            if arr[j] + initial <= b:
                initial = initial + arr[j]
                count +=1
        q.append(count)
    res =q[0]
    for i in range(len(q)):
        res=max(res, q[i])
    return res 
def subarraysum(arr, k):
    n=len(arr)
    window_sum = sum(arr[:k])
    res=0 
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        res = max(res, window_sum)
    return res 

def maxelement(arr, k):
    q=[]
    n=len(arr)
    for i in range(k):
        q.append(arr[i])
    res= 0
    for i in range(n-k+1):
        for j in range(k):
            res=max(res, q[j])
        q.pop(0)
        if i+k<n:
            q.append(arr[i+k])
    return res 

def unique(sti):
    s=set()
    for i in range(len(sti)):
        for j in range(i+1, len(sti)):
            if sti[i] == sti[j]:
                s.add(sti[j])
    for i in sti:
        if i not in s:
            print(i)


def rev(sti):
    j=0 
    n=len(sti)
    if n==0:
        return ''
    sti = [i for i in sti]
    for i in range(n-1,n//2,-1):
        if sti[i].isalpha():
            while j<i:
                if sti[j].isalpha():
                    sti[i],sti[j] = sti[j],sti[i]
                    j+=1
                    break 
                else:
                    j+=1
    return ''.join(sti)

def startingWith(sti, pattern):
    n=len(sti)
    q=[]
    for i in sti:
        count=0 
        for j in range(len(pattern)):
            if i[j] == pattern[j]:
                count +=1
            else:
                break 
            if count == len(pattern):
                q.append(i)
    return q

def trips(arr):
    n=len(arr)
    for i in range(n):
        arr[i] = arr[i]**2
    arr.sort()
    for i in range(n):
        j=0 
        k=i-1
        while j<k:
            if arr[k] + arr[j] == arr[i]:
                return True 
            else:
                if arr[j]+arr[k] < arr[i]:
                    j+=1
                else:
                    k-=1
    return False

print(rev("a-bC-dEf-ghIj"))


