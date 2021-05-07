def numIsIslands(grid):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0:
		return -1 
	grid=[[int(grid[i][j])for j in range(n)]for i in range(m)]
	count=0 
	for i in range(m):
		for j in range(n):
			if grid[i][j]==1:
				count += Helper(grid,i,j)
	return count 

def Helper(grid, i, j):
	if i<0 or i>=len(grid) or j<0 or j>=len(grid) or grid[i][j] != 1:
		return 0 
	grid[i][j]=-1
	neighbours=((0,1),(0,-1),(-1,0),(1,0))
	for dx, dy in neighbours:
		Helper(grid, i+dx, j+dy)
	return 1 



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIsIslands(grid))

          