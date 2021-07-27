def MinMovesToPushBox(grid):
    def check(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '#':
            return False 
        return True 

    def Helper(p_i, p_j, p_x, p_y, b_i, b_j):
        q = [(p_i, p_j)]
        visited = set()
        while q:
            p_i, p_j = q.pop(0)
            neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
            if (p_i, p_j) == (p_x, p_y) : return True 
            for dx, dy in neighbours:
                new_x = p_i + dx 
                new_y = p_j + dy 
                if not check(new_x, new_y) or (new_x, new_y) == (b_i, b_j) or (new_x, new_y) in visited:
                    continue 
                visited.add((new_x, new_y))
                q.append((new_x, new_y))
        return False 

    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0 : raise ValueError 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'T':
                target = (i, j)
            elif grid[i][j] == 'B':
                box = (i, j)
            elif grid[i][j] == 'S':
                person = (i, j)
    p_i, p_j = person
    b_i, b_j = box 
    q = [(0, b_i, b_j, p_i, p_j)]
    visited = {(b_i, b_j, p_i, p_j)}
    while q:
        dist, b_i, b_j, p_i, p_j = q.pop(0)
        if (b_i, b_j) == target : return dist 
        neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in neighbours:
            b_x = b_i + dx 
            b_y = b_j + dy 
            p_x = b_i - dx 
            p_y = b_j - dy 
            if not check(b_x, b_y) or (b_x, b_y, b_i, b_j) in visited : continue 
            if not check(p_x, p_y) or not Helper(p_i, p_j, p_x, p_y, b_i, b_j) : continue 
            visited.add((b_x, b_y, b_i, b_j))
            q.append((dist + 1, b_x, b_y, b_i, b_j))
    return - 1

grid = [["#","#","#","#","#","#"],
        ["#","T","#","#","#","#"],
        ["#",".",".","B",".","#"],
        ["#",".","#","#",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]
print(MinMovesToPushBox(grid))





