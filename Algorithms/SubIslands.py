def MatchGrids(grid, gridd):
	if not grid or not gridd : return -1 
	sen, res = set(), 0 
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				dfs(grid, i, j, sen)

	for i in range(len(gridd)):
		for j in range(len(gridd[0])):
			if gridd[i][j] == 1:
				seen = set()
				dfs(gridd, i, j, seen)
				if all(grid[a][b] == -1 for a, b in seen):
					res += 1
	return res 

def dfs(grid, i, j, seen):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in seen or grid[i][j] != 1 :
		return 
	seen.add((i, j))
	grid[i][j] = -1
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
	for dx, dy in neighbours:
		dfs(grid, i + dx, j + dy, seen)
	return 
	 


grid = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
gridd = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(MatchGrids(grid, gridd))


