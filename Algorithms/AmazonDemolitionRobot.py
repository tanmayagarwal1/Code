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

grid = [[1, 1, 1, 0], [1, 1, 9, 0], [1, 1, 1, 1], [1, 1, 1, 1]] # 3
grid1 = [[1,0,0], [1,0,0], [1,9,1]] # 3
grid2 = [[1,0,0], [1,9,1], [1,0,0]] # 2
grid3 = [[1,1,0], [9,1,0], [1,0,1]] # 1
grid4 = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1], [1, 9, 1, 1]] # 4
grid5 = [[1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 9, 1]] # 5
grid6 = [[1, 1, 1, 0], [0, 9, 1, 1]] # 2
print(DemolitionRobot(grid))
print(DemolitionRobot(grid1))
print(DemolitionRobot(grid2))
print(DemolitionRobot(grid3))
print(DemolitionRobot(grid4))
print(DemolitionRobot(grid5))
print(DemolitionRobot(grid6))