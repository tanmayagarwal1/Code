def ClosedIslands(grid):
	n=len(grid)
	m=len(grid[0])
	if n==0 or m==0:
		return 0 
	count=0 
	for i in range(1,n):
		for j in range(1,m):
			if grid[i][j]==1:
				if IsClosedIsland(grid,i,j):
					count+=1
	return count

def IsClosedIsland(grid,i,j):
	if grid[i][j]!=1:
		return True 
	if Onperimeter(grid,i,j):
		return False 
	grid[i][j]=-1	
	left  = IsClosedIsland(grid,i+1,j)
	right = IsClosedIsland(grid,i-1,j)
	up    = IsClosedIsland(grid,i,j+1)
	down  = IsClosedIsland(grid,i,j-1)
	return right and left and up and down 

def Onperimeter(grid,i,j):
	if i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1:
		return True  
	return False



grid=[[0,0,0,0,0,0,0,1],
      [0,1,1,1,1,0,0,1],
      [0,1,0,1,0,0,0,1],
      [0,1,1,1,1,0,1,0],
      [0,0,0,0,0,0,0,1]]

print(ClosedIslands(grid))