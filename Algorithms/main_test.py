m=n=4
def nqueen():
	b=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if nqueenu(b,0)==False:
		return False 
	printsol(b)
def nqueenu(b,col):
	if col>=n:
		return True 
	for i in range(n):
		if issafe(b,i,col):
			b[i][col]=1
			if nqueenu(b,col+1)==True:
				return True 
			b[i][col]=0 
	return False 
def issafe(b,row,col):
	for i in range(col):
		if b[row][i]==1:
			return False 
	for i,j in zip(range(row,-1,-1),range(col,-1,-1,)):
		if b[i][j]==1:
			return False 
	for i, j in zip(range(row,n),range(col,-1,-1)):
		if b[i][j]==1:
			return False 
	return True 
def printsol(b):
	for i in range(n):
		for j in range(n):
			print(b[i][j],end=" ")
		print()
def mazesolver(maze):
	sol=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if mazesolveru(maze,0,0,sol)==False:
		return False 
	printsol(sol)
def mazesolveru(maze,x,y,sol):
	if x==n-1 and y==n-1 and maze[x][y]==1:
		sol[x][y]=1
		return True
	if issafemaze(maze,x,y):
		if sol[x][y]==1:
			return False 
		sol[x][y]=1
		if mazesolveru(maze,x+1,y,sol):
			return True  
		if mazesolveru(maze,x,y+1,sol):
			return True  
		if mazesolveru(maze,x-1,y,sol):
			return True  
		if mazesolveru(maze,x,y-1,sol):
			return True  
		sol[x][y]=0 
	return False 

def issafemaze(maze,x,y):
	if x>=0 and x<n and y>=0 and y<n and maze[x][y]==1:
		return True 
	return False  



def goldmax(gold):
	m=len(gold)
	n=len(gold[0])
	gt=[[0 for _ in range(n)]for _ in range(m)]
	for col in range(n-1,-1,-1):
		for row in range(m):
			if col==n-1:
				right=0 
			else:
				right=gt[row][col+1]
			if col==n-1 or row==n-1:
				right_down=0 
			else:
				right_down=gt[row+1][col+1]
			if col==n-1 or row==0:
				right_up=0 
			else:
				right_up=gt[row-1][col+1]
			gt[row][col]=gold[row][col]+max(right_up,right_down,right)
	res=gt[0][0]
	for i in range(m):
		res=max(res,gt[i][0])
	return res

def lcs(x,y):
	m=len(x)
	n=len(y)
	dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
	for i in range(1,m+1):
		for j in range(1,n+1):
			if x[i-1]==y[j-1]:
				dp[i][j]=dp[i-1][j-1]+1
			else:
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	return dp[m][n]

def egg_max(f,n):
	dp=[[0 for _ in range(n+1)]for _ in range(f+1)]
	for i in range(1,f+1):
		for j in range(1,n+1):
			dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1
		if dp[i][j]>=f:
			return i 

def regularexpression(sti,pattern):
	m=len(sti)
	n=len(pattern)
	dp=[[False for _ in range(n+1)]for _ in range(m+1)]
	dp[0][0]=True 
	for i in range(1,n+1):
		if pattern[i-1]=="*":
			dp[0][i]=dp[0][i-2]
	for i in range(1,m+1):
		for j in range(1,n+1):
			if pattern[j-1]=='.' or sti[i-1]==pattern[j-1]:
				dp[i][j]=dp[i-1][j-1]
			if pattern[j-1]=="*":
				dp[i][j]=dp[i][j-2]
				if pattern[j-2]=="." or sti[i-1]==pattern[j-2]:
					dp[i][j]=dp[i-1][j]
	return dp[m][n]
def mincost(grid,x,y):
	m=len(grid)
	n=len(grid[0])
	dp=[[0 for _ in range(n)]for _ in range(m)]
	dp[0][0]=grid[0][0]
	for i in range(1,n):
		dp[0][i]=dp[0][i-1]+grid[0][i]
	for i in range(1,m):
		dp[i][0]=dp[i-1][0]+grid[i][0]
	for i in range(1,m):
		for j in range(1,n):
			dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+grid[i][j]
	return dp[x][y]
##MINIMUM COST 
cost= [[1, 2, 3],
       [4, 8, 2],
       [1, 5, 3]]

print(mincost(cost, 2, 2))

class graph:
	def __init__(self,v):
		self.v=v
		self.graph=[[0 for _ in range(self.v)]for _ in range(self.v)]
	def shortestPath(self,s):
		dist=[float('inf')]*self.v
		visited=[False]*self.v
		dist[s]=0 
		for _ in range(self.v):
			u=self.minVertex(dist,visited)
			visited[u]=True
			for x in range(self.v):
				if self.graph[u][x]>0 and visited[x]==False and dist[x]>dist[u]+self.graph[u][x]:
					dist[x]=dist[u]+self.graph[u][x]
		self.printsol(dist)
	def minVertex(self,dist,visited):
		min=float('inf')
		for i in range(self.v):
			if dist[i]<min and visited[i]==False:
				min=dist[i]
				min_index=i 
		return min_index
	def printsol(self,dist):
		for i in range(self.v):
			print(f"{i} : {dist[i]}")
g = graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]
g.shortestPath(0)