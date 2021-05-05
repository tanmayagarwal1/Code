def numIsIslands(grid):
	# Grid is a 1 and 0 matrox 
	grid=[[int(grid[j][i]) for i in range(len(grid[0]))]for j in range(len(grid))]
	count=0 
	if len(grid)==0 or len(grid[0])==0:
		return 0 
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j]==1:
				count+= self.checker(grid,i,j)
	return count 

def checker(self,grid,i,j):
	if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
		return 0 
	grid[i][j]=0 
	self.checker(grid,i+1,j)
	self.checker(grid,i,j+1)
	self.checker(grid,i-1,j)
	self.checker(grid,i,j-1)
	return 1 

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIsIslands(grid))
