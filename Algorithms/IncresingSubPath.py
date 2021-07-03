def IncreasingSubPath(grid):
    def Helper(grid, i, j, dp):
        if not dp[i][j]:
            val = grid[i][j]
            if i and val < grid[i - 1][j]:
                Up = Helper(grid, i - 1, j, dp)
            else:
                Up = 0 

            if i < len(grid) - 1 and val < grid[i + 1][j]:
                Down = Helper(grid, i + 1, j, dp)
            else:
                Down = 0 

            if j and val < grid[i][j - 1]:
                Left = Helper(grid, i, j - 1, dp)
            else:
                Left = 0 

            if j < len(grid[0]) - 1 and val < grid[i][j + 1]:
                Right = Helper(grid, i, j + 1, dp)
            else:
                Right = 0 

            dp[i][j] = 1 + max(Up, Down, Left, Right)
        return dp[i][j]

    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0: raise ValueError 
    dp, res = [[0 for _ in range(n)] for _ in range(n)], 0 
    for i in range(m):
        for j in range(n):
            res = max(res, Helper(grid, i, j, dp))
    return res 

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(IncreasingSubPath(matrix))