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
from collections import defaultdict
class graph1:
	def __init__(self):
		self.graph=defaultdict(list)
	def append(self,s,d):
		self.graph[s].append(d)
	def bfs(self,s):
		q=[]
		visited=[False]*1000
		visited[s]=True 
		q.append(s)
		while q:
			s=q.pop(0)
			print(s)
			for i in self.graph[s]:
				if visited[i]==False:
					q.append(i)
					visited[i]=True 
	def dfs(self,v):
		s=set()
		self.dfsu(s,v)
	def dfsu(self,s,v):
		s.add(v)
		print(v)
		for i in self.graph[v]:
			if i not in s:
				self.dfsu(s,i)

def NumIslands(grid):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0:
		return -1 
	grid=[[int(grid[i][j])for j in range(n)]for i in range(m)]
	count=0 
	for i in range(m):
		for j in range(n):
			if grid[i][j]==1:
				count+= IsIslandHelper(grid,i,j)
	return count 

def IsIslandHelper(grid, i, j):
	if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
		return  0 
	grid[i][j]=-1 
	neighbours=((0,1),(0,-1),(1,0),(-1,0))
	for dx, dy in neighbours:
		IsIslandHelper(grid, i+dx, j+dy)
	return 1 

def Surrounded(grid):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0:
		return -1 
	for i in range(m):
		if grid[i][0] == "O":
			SurroundedHelper(grid, i, 0)
	for i in range(m):
		if grid[i][n-1] == "O":
			SurroundedHelper(grid, i, n-1)
	for i in range(n):
		if grid[0][i] == "O":
			SurroundedHelper(grid, 0, i)
	for i in range(n):
		if grid[m-1][i] == "O":
			SurroundedHelper(grid, m-1, i)
	for i in range(m):
		for j in range(n):
			if grid[i][j] == -1 :
				grid[i][j]= "O"
			elif grid[i][j] == "O":
				grid[i][j] = "X"
	printgrid(grid)

def SurroundedHelper(grid, i, j):
	if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != "O":
		return 
	grid[i][j] = -1
	neighbours = ((0,1),(0,-1),(1,0),(-1,0))
	for dx, dy in neighbours :
		SurroundedHelper(grid, i+dx, j+dy)
	return 
def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j],end=" ")
		print()
def SpiralMatrix(grid):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0 :
		return -1 
	arr=[]
	Top, Bottom, Left, Right, max_arr = 0, m-1, 0, n-1, m*n
	while len(arr)<max_arr:
		for i in range(Left, Right+1):
			if len(arr)<max_arr:
				arr.append(grid[Top][i])
		Top += 1

		for i in range(Top, Bottom+1):
			if len(arr)<max_arr:
				arr.append(grid[i][Right])
		Right -=1

		for i in range(Right, Left-1, -1):
			if len(arr)<max_arr:
				arr.append(grid[Bottom][i])
		Bottom -= 1

		for i in range(Bottom, Top-1, -1):
			if len(arr)<max_arr:
				arr.append(grid[i][Left])
		Left += 1
	return arr 

def AntiSpiralMatrix(grid):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0:
		return -1 
	Top, Bottom, Left, Right, max_arr, arr = 0, m-1, 0, n-1, m*n, []
	while len(arr)<max_arr:
		for i in range(Right, Left-1, -1):
			if len(arr)<max_arr:
				arr.append(grid[Top][i])
		Top += 1

		for i in range(Top, Bottom+1):
			if len(arr)<max_arr:
				arr.append(grid[i][Left])
		Left+=1

		for i in range(Left, Right+1):
			if len(arr)<max_arr:
				arr.append(grid[Bottom][i])
		Bottom -=1 

		for i in range(Bottom, Top-1, -1):
			if len(arr)<max_arr:
				arr.append(grid[i][Right])
		Right -=1
	return arr


def Exist(grid, word):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0:
		return -1 
	count=0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and ExistHelper(grid, i, j, word, count):
				return True 
	return False

def ExistHelper(grid, i, j, word, count):
	if count == len(word):
		return True 
	if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != word[count]:
		return False 
	temp = grid[i][j]
	grid[i][j] = "#"
	boolean = ExistHelper(grid, i+1, j, word, count+1) or \
			  ExistHelper(grid, i, j+1, word, count+1) or \
			  ExistHelper(grid, i-1, j, word, count+1) or \
			  ExistHelper(grid, i, j-1, word, count+1)
	grid[i][j] = temp 
	return boolean



board = [["A","B","C","E"],
		 ["S","F","C","S"],
		 ["A","D","E","E"]]

#print(Exist(board,"ABCCED"))




class node:
	def __init__(self,data):
		self.data=data
		self.left=self.right=None
def push(root,data):
	if root == None:
		return node(data)
	else:
		if root.data<data:
			root.right=push(root.right,data)
		elif root.data>data:
			root.left=push(root.left,data)
		return root 

def view(root):
	if root:
		view(root.left)
		print(root.data)
		view(root.right)
	else:
		return 
def dele(root,val):
	if root.left:
		root.left=dele(root.left,val)
	if root.right:
		root.right=dele(root.right,val)
	if root.data==val:
		return None 
	return root

def kthancestor(root,val,k):
	if root==None:
		return None
	if (root.data==val or (kthancestor(root.left,val,k)) or (kthancestor(root.right,val,k))):
		if k[0]>0:
			k[0] -=1
		elif k[0]==0:
			print(root.data)
			return None
		return root 
def search(root,val):
	if root==None:
		return False 
	if root.data==val:
		return True 
	else:
		 return search(root.left,val) or search(root.right,val)
def isSymmetric(root):
	return isMirror(root.left,root.right)
def isMirror(root_left, root_right):
	q=[(root_left,root_right)]
	while q:
		x,y = q.pop()
		if not x and not y:
			continue 
		if not x or not y:
			return False 
		if x.data != y.data:
			return False 
		else:
			q.append((x.left, y.right))
			q.append((x.right, y.left))
		return True 




root=node(5)
push(root,1)
push(root,1)
push(root,1)
push(root,1)
push(root,1)
view(root)
print(isSymmetric(root))
#kthancestor(root,10,[1])





          
