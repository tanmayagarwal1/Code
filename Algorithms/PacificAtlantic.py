def PacficAtlantic(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return -1
	pacific_visited = [[False for _ in range(n)]for _ in range(m)] 
	atlantic_visited = [[False for _ in range(n)] for _ in range(m)]
	res = []
	for i in range(m):
		HelperOcean(grid, i, 0, pacific_visited)
		HelperOcean(grid, i, n-1, atlantic_visited)
	for i in range(n):
		HelperOcean(grid, 0, i, pacific_visited)
		HelperOcean(grid, m-1, i, atlantic_visited)
	for i in range(m):
		for j in range(n):
			if pacific_visited[i][j] and atlantic_visited[i][j]:
				res.append([i, j])
	return res 

def HelperOcean(grid, i, j, visited):
	visited[i][j] = True 
	neighbours = ((0,1),(0,-1),(1,0),(-1,0))
	for dx, dy in neighbours:
		x, y = i + dx, j + dy
		if x < 0 or x>=len(grid) or y< 0 or y>=len(grid[0]) or visited[x][y] or grid[x][y] < grid[i][j]:
			continue 
		HelperOcean(grid, x, y, visited)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(PacficAtlantic(heights))