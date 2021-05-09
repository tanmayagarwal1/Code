# Preorder and Inorder build 
# Inorder and Postorder build 
def Search(grid, word):
    m=len(grid)
    n=len(grid[0])
    if m==0 or n==0:
        return -1
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == word[0] and Helper(grid, word, i, j, count):
                return True 
    return False 
def Helper(grid, word, i, j , count):
    if count == len(word):
        return True 
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != word[count]:
        return False 
    grid[i][j] = -1 
    boolean = Helper(grid, word, i+1, j, count+1) or \
              Helper(grid, word, i, j+1, count+1) or \
              Helper(grid, word, i-1, j, count+1) or \
              Helper(grid, word, i, j-1, count+1) 
    return boolean 

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(Search(board,"ABCCED"))

def NumIslands(grid):
    m=len(grid)
    n=len(grid[0])
    if m==0 or n==0:
        return -1 
    grid= [[int(grid[i][j]) for j in range(n)]for i in range(m)]
    count = 0 
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                count += IslandHelper(grid, i, j)
    return count 

def IslandHelper(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
        return 0 
    grid[i][j] = -1
    neighbours = ((0,1),(0,-1),(1,0),(-1,0))
    for dx, dy in neighbours:
        IslandHelper(grid, i+dx, j+dy)
    return 1

def IsSurround(grid):
    m=len(grid)
    n=len(grid[0])
    if m==0 or n==0:
        return -1
    for i in range(m):
        if grid[i][0] =="O":
            SurroundHelper(grid, i, 0)
    for i in range(m):
        if grid[i][n-1] =="O":
            SurroundHelper(grid, i, n-1)
    for i in range(n):
        if grid[0][i] =="O":
            SurroundHelper(grid,0,i)
    for i in range(n):
        if grid[m-1][i]=="O":
            SurroundHelper(grid, m-1, i)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == -1:
                grid[i][j] = "O"
            elif grid[i][j] == "O":
                grid[i][j] = "X"
    printsol(grid)

def SurroundHelper(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != "O":
        return 
    grid[i][j] = -1
    neighbours= ((0,1),(0,-1),(1,0),(-1,0))
    for dx, dy in neighbours:
        SurroundHelper(grid, i+dx, j+dy)
    return 
def printsol(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end=" ")
        print()


grid = [ ["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
IsSurround(grid)