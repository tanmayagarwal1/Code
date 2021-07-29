import heapq
def SwimInRisingWater(grid):
    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0 : raise ValueError 
    pq = [(grid[0][0], 0, 0)]
    grid[0][0] =  - 1
    res = 0 
    while True:
        T, i, j = heapq.heappop(pq)
        res = max(res, T)
        if i == m - 1 and j == n - 1 : return res 
        neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in neighbours:
            x = i + dx 
            y = j + dy 
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] < 0 :
                continue 
            heapq.heappush(pq, (grid[x][y], x, y))
            grid[x][y] = - 1
    return False 


grid = [[0, 1, 2, 3, 4],
        [24,23,22,21, 5],
        [12,13,14,15,16],
        [11,17,18,19,20],
        [10, 9, 8, 7, 6]]

print(SwimInRisingWater(grid))