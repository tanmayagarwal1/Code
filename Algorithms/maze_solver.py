n=4
def printSolution( sol ):
    for i in range(n):
        for j in range(n):
            print(sol[i][j],end=" ")
        print()
def mazesolver(maze):
    sol=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if mazesolveutil(maze,0,0,sol)==False:
        return False 
    printSolution(sol) 
def issafe(maze,x,y):
    if x >= 0 and x<n and y >= 0 and y<n and maze[x][y]==1:
        return True 
    return False 
def mazesolveutil(maze,x,y,sol):
    if x==n-1 and y==n-1 and maze[x][y]==1:
        sol[x][y]=1
        return True
    if issafe(maze,x,y)==True:
        if sol[x][y]==1:        	
            return False 
        sol[x][y]=1        
        if mazesolveutil(maze,x+1,y,sol)==True:
            return True
        if mazesolveutil(maze,x,y+1,sol)==True:
            return True 
        if mazesolveutil(maze,x-1,y,sol)==True:
            return True 
        if mazesolveutil(maze,x,y-1,sol)==True:
            return True
        sol[x][y]=0
    return False

maze = [  [1, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 1, 0],
          [1, 1, 1, 1] ]
mazesolver(maze)



              