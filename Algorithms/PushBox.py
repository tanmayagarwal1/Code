def MinMovesToPushBox(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 'B':
				box = (i, j)
			if grid[i][j] == 'S':
				person = (i, j)
			if grid[i][j] == 'T':
				target = (i, j)

	def check(x, y):
		return 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]!='#'

	def isReachable(curr, new, box):
		q = [curr]
		visted = set()
		while q :
			curr = q.pop(0)
			if curr == new : return True 
			new_curr = [(curr[0] - 1, curr[1]), (curr[0], curr[1] + 1), (curr[0], curr[1] - 1), (curr[0] + 1, curr[1])]
			for x, y in new_curr:
				if check(x, y) and (x, y) not in visted and (x, y) != box:
					visted.add((x, y))
					q.append((x, y))
		return False 


	q = [(0, box, person)]
	visited = {box + person}
	while q:
		dist, box, person = q.pop(0)
		if box == target : return dist 
		b_coord = [(box[0]+1,box[1]),(box[0]-1,box[1]),(box[0],box[1]+1),(box[0],box[1]-1)]
		p_coord = [(box[0]-1,box[1]),(box[0]+1,box[1]),(box[0],box[1]-1),(box[0],box[1]+1)]
		for new_box, new_person in zip(b_coord, p_coord):
			if not check(*new_box) or  new_box + box in visited: continue 
			if not check(*new_person) or not isReachable(person, new_person, box): continue 
			visited.add(new_box + box)
			q.append((dist + 1, new_box, box))
	return -1

grid = [["#","#","#","#","#","#"],
        ["#","T","#","#","#","#"],
        ["#",".",".","B",".","#"],
        ["#",".","#","#",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]
print(MinMovesToPushBox(grid))





