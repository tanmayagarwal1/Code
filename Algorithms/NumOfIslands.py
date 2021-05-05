def numIsIslands(grid):
	# Grid is a 1 and 0 matrox 
	grid=[[int(grid[j][i]) for i in range(len(grid[0]))]for j in range(len(grid))]
	count=0 
	if len(grid)==0 or len(grid[0])==0:
		return 0 
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j]==1:
				count+= checker(grid,i,j)
	return count 

def checker(grid,i,j):
	if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
		return 0 
	grid[i][j]=0 
	checker(grid,i+1,j)
	checker(grid,i,j+1)
	checker(grid,i-1,j)
	checker(grid,i,j-1)
	return 1 

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIsIslands(grid))


'''
The recursive checks part can also be written as the surrounded regions parts  i.e 

	neighbours=((0,1),(0,-1),(1,0),(-1,0))
	for dx, dy in neighbours :
		check(grid, i+dx , j+dy)
	return 1 


'''