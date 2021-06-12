def IncresingSubPath(grid):
    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0:
        return -1 
    res, dp = [], [[0 for _ in range(n)]for _ in range(m)]
    for i in range(m):
        for j in range(n):
            res.append(dfs(grid, dp, i, j))
    return max(res)

def dfs(grid, dp, i, j):
    if not dp[i][j]:
        val = grid[i][j]

        if i and val > grid[i - 1][j] : 
            Up = dfs(grid, dp, i - 1, j)
        else:
            Up = 0

        if i < len(grid) - 1 and val > grid[i + 1][j]:
            Down = dfs(grid, dp, i + 1, j)
        else:
            Down = 0

        if j and val > grid[i][j - 1]:
            Left = dfs(grid, dp, i, j - 1)
        else:
            Left = 0

        if j < len(grid[0]) - 1 and val > grid[i][j + 1]:
            Right = dfs(grid, dp, i, j + 1)
        else:
            Right = 0 

        dp[i][j] = 1 + max(Up, Down, Left, Right)
    return dp[i][j]

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(MaximumPath(matrix))