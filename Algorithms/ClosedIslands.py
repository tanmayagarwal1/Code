def ClosedIslands(grid):
	n=len(grid)
	m=len(grid[0])
	if n==0 or m==0:
		return 0 
	count=0 
	for i in range(1,n):
		for j in range(1,m):
			if grid[i][j]==0:
				if self.IsClosedIsland(grid,i,j):
					count+=1
	return count

def IsClosedIsland(self,grid,i,j):
	if grid[i][j]!=0:
		return True 
	if self.Onperimeter(grid,i,j):
		return False 
	grid[i][j]=-1
	left=self.IsClosedIsland(grid,i+1,j)
	right=self.IsClosedIsland(grid,i-1,j)
	up=self.IsClosedIsland(grid,i,j+1)
	down=self.IsClosedIsland(grid,i,j-1)
	return right and left and up and down 
def Onperimeter(self,grid,i,j):
	if i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1:
		return True  
	return False



grid=[[1,1,1,1,1,1,1,0],
      [1,0,0,0,0,1,1,0],
      [1,0,1,0,1,1,1,0],
      [1,0,0,0,0,1,0,1],
      [1,1,1,1,1,1,1,0]]

print(ClosedIslands(grid))