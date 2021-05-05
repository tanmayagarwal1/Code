n=4 
def mazesolver(maze):
	sol=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if mazesolveru(maze,0,0,sol)==False:
		return False 
	printsol(sol)
def mazesolveru(maze,x,y,sol):
	if x==n-1 and y==n-1 and maze[x][y]==1:
		sol[x][y]=1 
		return True 
	if issafe(maze,x,y):
		neighbours=((0,1),(0,-1),(1,0),(-1,0))
		for dx,dy in neighbours:
			mazesolveru(maze, x+dx, y+dy, sol)
	return False 
def issafe(maze,x,y):
	if x>=0 and x<n and y>=0 and y<n and maze[x][y]==1:
		return True 
	return False 
def printsol(sol):
	for i in range(n):
		for j in range(n):
			print(sol[i][j],end=" ")
		print()

maze = [  [1, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 1, 0],
          [1, 1, 1, 1] ]
mazesolver(maze)
