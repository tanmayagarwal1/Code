def DemolitionRobot(grid):
    start = grid[0][0]
    z = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                z.append([i, j])
            if grid[i][j] == 9:
                end_x, end_y = i, j
    res = [[0, 0]]
    for i in z:
        if [i[0]+1, i[1]] in z and i[0]+1 <= end_x and i[1] <= end_y:
            res.append([i[0]+1,i[1]])
        elif [i[0],i[1]+1] in z and i[0] <= end_x and i[1]+1 <= end_y:
            res.append([i[0],i[1]+1])
    return len(res)

def printgrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = ' ')
        print()

grid = [[1, 0, 1], [1, 1, 1], [1, 1, 9]]
print(printgrid(grid))
