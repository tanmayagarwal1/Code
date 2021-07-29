def DungeonGame(grid):
    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0 : raise ValueError 
    dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
    dp[m - 1][n], dp[m][n - 1] = 1, 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - grid[i][j], 1)
    return dp[0][0]

grid = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(DungeonGame(grid))