
from collections import deque
def minPushBox(grid): # grid is a 2d array 
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "T":
                target = (i,j)
            if grid[i][j] == "B":
                box = (i,j)
            if grid[i][j] == "S":
                person = (i,j)

    def valid(x, y):
        return 0<=x<m and 0<=y<n and grid[x][y]!='#'

    def get_neighbor(i, j):
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = i + dx, j + dy
            if valid(x, y):
                yield x, y

    def get_box_neighbor(i, j):
        for dx,dy in [(-1,0),(0,-1)]:
            x, y = i + dx, j + dy
            px, py = i - dx, j - dy
            if valid(x, y) and valid(px, py):
                yield (x, y), (px, py)
                yield (px, py), (x, y)

    def check(curr, dest, box):
        queue = deque([curr])
        v = set()
        while queue:
            i, j = queue.popleft()
            if (i, j) == dest: 
                return True
            for x, y in get_neighbor(i, j):
                if (x,y) not in v and (x,y) != box:
                    v.add((x,y))
                    queue.append((x,y))
        return False

    q = deque([(box, person)])
    seen = set()
    seen.add(box + person)
    steps = 0
    while q:
        size = len(q)
        for _ in range(size):
            box, person = q.popleft()
            if box == target:
                return steps
            for new_box, new_person in get_box_neighbor(*box):
                if new_box + box not in seen and \
                        check(person, new_person, box):
                    seen.add(new_box + box)
                    q.append((new_box, box))
        steps += 1
    return -1

grid = [["#","#","#","#","#","#"],
       ["#","T",".",".","#","#"],
       ["#",".","#","B",".","#"],
       ["#",".",".",".",".","#"],
       ["#",".",".",".","S","#"],
       ["#","#","#","#","#","#"]]

print(minPushBox(grid))