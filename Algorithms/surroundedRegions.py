def IsSurround(grid):
	m=len(grid) 
	n=len(grid[0])

	# first row will be i = 0 and last row will be i = m-1
	# first col will be j = 0 and last col will be j = n-1
	for i in range(m):
		if grid[i][0]=='O':
			checker(grid , i , 0)
	for i in range(m):
		if grid[i][n-1]=='O':
			checker(grid , i, n-1)
	for j in range(n):
		if grid[0][j]=="O":
			checker(grid , 0 , j)
	for j in range(n):
		if grid[m-1][j]=="O":
			checker(grid , m-1 , j)
	for i in range(m):
		for j in range(n):
			if grid[i][j]=="$":
				grid[i][j]="O"
			elif grid[i][j]=="O":
				grid[i][j]="X"
	printsol(grid)

def checker(grid,i,j):
	if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != "O":
		return 
	grid[i][j]="$"
	neighbours=((0,1),(0,-1),(1,0),(-1,0),)
	for dx, dy in neighbours: 
		checker(grid , i+dx , j+dy)
	return 

def printsol(grid):	
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j],end=" ")	
		print()


grid = [ ["X","X","X","X"],
		 ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

IsSurround(grid)