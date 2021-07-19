def PAcificAtlantic(grid):
    def Helper(grid, i, j, visited):
        visited[i][j] = True 
        neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in neighbours:
            x = i + dx 
            y = j + dy 
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[i][j] > grid[x][y]:
                continue 
            Helper(grid, x, y, visited)

    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0 : raise ValueError 
    PacificVisited = [[False for _ in range(n)] for _ in range(m)]
    AtlanticVisited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        Helper(grid, i, 0, PacificVisited)
        Helper(grid, i, n - 1, AtlanticVisited)
    for i in range(n):
        Helper(grid, 0, i, PacificVisited)
        Helper(grid, m - 1, i, AtlanticVisited)
    res = []
    for i in range(m):
        for j in range(n):
            if PacificVisited[i][j] and AtlanticVisited[i][j]:
                res.append([i, j])
    return res 

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(PAcificAtlantic(heights))