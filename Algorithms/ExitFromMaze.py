def MiniminMovesToExitGrid(grid, start):
    # classic bfs. Use rotten oranges template 
    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0 : raise ValueError 
    i, j = start 
    q, moves = [(i, j)], 0
    grid[i][j] = '+'
    while q:
        moves += 1
        for _ in range(len(q)):
            i, j = q.pop(0)
            nieghbours = ((0, 1), (1, 0), (-1, 0), (0, -1))
            for dx, dy in nieghbours:
                x = i + dx 
                y = j + dy 
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '+':
                    continue 
                if x == 0 or y == 0 or x == m - 1 or y == n - 1 : # Either of the borders with empty cell
                    return moves 
                q.append((x, y))
                grid[x][y] = '+'
    return - 1



grid = [["+",".","+","+","+","+","+"],
        ["+",".","+",".",".",".","+"],
        ["+",".","+",".","+",".","+"],
        ["+",".",".",".",".",".","+"],
        ["+","+","+","+",".","+","."]]

start = [0,1]

print(MiniminMovesToExitGrid(grid, start))
