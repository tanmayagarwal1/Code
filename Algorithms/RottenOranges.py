def RottenOranges(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	rotten, fresh_cnt, minutes = [], 0, 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 2:
				rotten.append((i, j))
			elif grid[i][j] == 1:
				fresh_cnt += 1
	while rotten and fresh_cnt != 0:
		minutes += 1
		for _ in range(len(rotten)):
			i, j = rotten.pop(0)
			neighbours = ((0,1), (0,-1), (1,0), (-1,0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 2 or grid[x][y] == 0:
					continue 
				grid[x][y] = 2
				fresh_cnt -= 1
				rotten.append((x, y))
	return minutes if fresh_cnt == 0 else -1 

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(RottenOranges(grid))



