"""


AUTHOR :   Tanmay Agarwal 

DATE :     20 April 2021 ( DATE OF ORGINATION )

FILE :     @InProgress 

ABSTRACT : A culmination of algorithms and strutures that can be used as chunks of code
           for present or future purposes. This code driver will be updated reglarly with 
           systematic optimisations and with new advanced algorithms. If, cloned from 
           the git repo, and in the perspective of contribution, kindly make sure the
           contributions are throroughly tested out on a sub-branch and well optimised 
           algorithms are implemented before a pull request has been issued. 
		   Conversely, each and every algorithm also has its own seprate code file  which can be 
		   looked up at the git repo 


NOTE : 	   It has a similar sibling by the name of @DriverComplex. It is a brute force file, best
	       used for testing out rapid models ( Not so well optimised )

SOURCING : Maintained at a git repo @CODE 



"""
"""

NQUEENS  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
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
		if issafequeen(b,i,col):
			b[i][col]=1
			if nqueenu(b,col+1)==True:
				return True 
			b[i][col]=0 
	return False
def issafequeen(b,row,col):
	for i in range(col):
		if b[row][i]==1:
			return False 
	for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
		if b[i][j]==1:
			return False 
	for i,j in zip(range(row,n),range(col,-1,-1)):
		if b[i][j]==1:
			return False 
	return True 

"""

GOLD MINE  ---------------------------------------------------------------------------------------------------------------------------------------------------------------


"""



def goldmax(gold):
	gt=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
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
			gt[row][col]=gold[row][col]+max(right_down,right_up,right)
	res=gt[0][0]
	for i in range(n):
		res=max(res,gt[i][0])
	return res 

"""

MAZE SOLVER  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

def mazesolver(maze):
	sol=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if mazsolveru(maze,0,0,sol)==False:
		return False 
	printsol(sol)
def mazsolveru(maze,x,y,sol):
	if x==n-1 and y==n-1 and maze[x][y]==1:
		sol[x][y]=1
		return True 
	if issafe(maze,x,y):
		sol[x][y]=1
		if mazsolveru(maze,x+1,y,sol):
			return True
		if mazsolveru(maze,x,y+1,sol):
			return True 
		if mazsolveru(maze,x-1,y,sol):
			return True 
		if mazsolveru(maze,x,y-1,sol):
			return True 
		sol[x][y]=0 
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

"""

EGGS  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

def eggs(f,n):
	dp=[[0]*(n+1)for i in range(f+1)]
	for i in range(1,f+1):
		for j in range(1,n+1):
			dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1
		if dp[i][j]>=f:
			return i 


"""

RAIN WATER COLLECTOR ----------------------------------------------------------------------------------------------------------------------------------------------------

"""
import numpy as np 
run_max=np.maximum.accumulate 
def water_collector(height):
	if not height:
		return 0 
	a=np.array(height)
	global_max=np.argmax(a)
	return np.sum(run_max(a[:global_max])-a[:global_max],dtype=np.int64)+\
			np.sum(run_max(a[:global_max:-1])-a[:global_max:-1],dtype=np.int64)


"""

SINGLE SOURCE SHORTEST PATH ( DIJKSTRA'S ) ALGORITHM 

"""

class graph1:
	def __init__(self,v):
		self.v=v
		self.graph=[[0 for i in range(self.v)]for j in range(self.v)]
	def shortestPath(self,source):
		dist=[float("inf")]*self.v
		dist[source]=0 
		visited=[False]*self.v
		for i in range(self.v):
			u=self.smalldistance(dist,visited)
			visited[u]=True 
			for x in range(self.v):
				if self.graph[u][x]>0 and visited[x]==False and dist[x]>dist[u]+self.graph[u][x]:
					dist[x]=dist[u]+self.graph[u][x]
		self.printsol(dist)
	def smalldistance(self,dist,visited):
		min=float("inf")
		for i in range(self.v):
			if dist[i]<min and visited[i]==False:
				min=dist[i]
				min_index=i 
		return min_index
	def printsol(self,dist):
		for i in range(self.v):
			print(f"{i} : {dist[i]}")

"""

PARANTHESIS CHECKER ----------------------------------------------------------------------------------------------------------------------------------------------------

"""

def checker(st):
	q=[]
	v={'{':'}','(':')','[':']'}
	open_br=set(['{','[','('])
	for i in st:
		if i in open_br:
			q.append(i)
		else:
			if i==v[q[-1]]:
				q.pop()
			else:
				return "Unbalanced\n"
	return "Balanced\n"

"""

ENCODING ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

def encoding(newmap,sti):
    ogmap='abcdefghijklmnopqrstuvwxyz'
    q=[]
    d=dict(zip(newmap,ogmap))
    for i in sti: 
        q.append(d[i])
    s=''.join(q)
    return s 


"""

ARRAYS ALGO  ---------------------------------------------------------------------------------------------------------------------------------------------------------------


"""

class A:
	def __init__(self,a):
		self.a=a 
	def trips(self):
		n=len(self.a)
		for i in range(len(self.a)):
			self.a[i]=self.a[i]**2
		self.a.sort()
		for i in range(len(self.a)):
			j=0 
			k=i-1 
			while j<k:
				if self.a[k]+self.a[j]==self.a[i]:
					return True
				else:
					if self.a[j]+self.a[k]<self.a[i]:
						j+=1
					else:
						k-=1
		return False

	def remdup(self):
		v=set() 
		for i in range(len(self.a)):
			if self.a[i] not in v:
				v.add(self.a[i])
			else:
				print(f"{self.a[i]} is duplicate")
	def remdup2(self):
		n=len(self.a)
		for i in range(n):
			j=i+1
			while j<n:
				if self.a[i]==self.a[j]:
					print(f"{self.a[i]} is a dup")
					j+=1			
				else:
					j+=1
	def reve(self):
		n=len(self.a)
		j=0 
		for i in range(n-1,-1,-1):
			if self.a[i].isalpha():
				while j<i:
					if self.a[j].isalpha():
						self.a[i],self.a[j]=self.a[j],self.a[i]
						j+=1
						break
					else:
						j+=1
		return self.a
	def kaden(self):
		n=len(self.a)
		i=self.a[0]
		j=0 
		for k in range(n):
			j=j+self.a[k]
			if i<j:
				i=j 
			if j<0:
				j=0 
		return i 
	def target(self, num):
		n=len(self.a)
		for i in range(n):
			for j in range(i+1,n):
				if arr[j]+arr[i]==num :
					return i,j 
				else:
					continue 


"""
SORTS   ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""					

def mergesort(arr):
	if len(arr)>1:
		mid=len(arr)//2
		l=arr[:mid]
		r=arr[mid :]
		mergesort(l)
		mergesort(r)
		i=j=k=0 
		while i<len(l) and j<len(r):
			if l[i]<r[j]:
				arr[k]=l[i]
				i+=1
			else:
				arr[k]=r[j]
				j+=1
			k+=1
		while i<len(l):
			arr[k]=l[i]
			i+=1
			j+=1
		while j<len(r):
			arr[k]=r[j]
			j+=1
			k+=1
def heapsort(arr):
	n=len(arr)
	for i in range(n//2-1,-1,-1):
		Heapify(arr,n,i)
	for i in range(n-1,0,-1):
		arr[0],arr[i]=arr[i],arr[0]
		Heapify(arr,i,0)
def Heapify(arr,n,i):
	large=i 
	l=2*i+1
	r=2*i+2
	if l<n and arr[large]<arr[l]:
		large=l 
	if r<n and arr[large]<arr[r]:
		large=r 
	if large != i:
		arr[large],arr[i]=arr[i],arr[large]
		Heapify(arr,n,large)



""" 

TREES  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

def st(self,data):
	self.data=data 
	self.left=self.right=None
rnode=type('rnode',(),{'__init__':st})

def push(root,data):
	if root==None:
		return rnode(data)
	else:
		if root.data<data:
			root.right=push(root.right,data)
		elif root.data>data:
			root.left=push(root.left,data)
		return root 
def invert(root):
	if root:
		root.left,root.right=root.right,root.left
		invert(root.left)
		invert(root.right)
	else:
		return root 
def adder(root):
	if root==None:
		return 0 
	else:
		return root.data + adder(root.left)+adder(root.right)
def leaf(root):
	if root==None:
		return 0 
	if root.left==None and root.right==None:
		return 1 
	else:
		return leaf(root.left)+leaf(root.right)
def subtree(root):
	if root==None:
		return 0 
	res=[-9999999]
	subtreeu(root,res)
	return res[0]
def subtreeu(root,res):
	if root ==None:
		return 0 
	else:
		curr=root.data+subtreeu(root.left,res)+subtreeu(root.right,res)
		res[0]=max(res[0],curr)
		return curr 
def height(root):
	if root==None:
		return 0 
	else:
		l=height(root.left)
		r=height(root.right)
		if l<r:
			return r+1
		else:
			return l+1 
def levelorder(root):
	if root==None:
		return 
	else:
		h=height(root)
		for i in range(h):
			levelorderu(root,i)
def levelorderu(root,l):
	if root==None:
		return 
	if l==0:
		print(root.data)
	else:
		levelorderu(root.left,l-1)
		levelorderu(root.right,l-1)
def show(root):
	if root:
		show(root.left)
		print(root.data)
		show(root.right)
	else:
		return 


"""

GRAPHS ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
from collections import defaultdict

def tan(self):
	self.graph=defaultdict(list)
def append(self,s,d):
	self.graph[s].append(d)
def bfs(self,v):
	q=[]
	visited=[False]*100
	visited[v]=True
	q.append(v)
	while q:
		s=q.pop()
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

graph=type('graph',(),{'__init__':tan,'append':append,'bfs':bfs,'dfs':dfs,'dfsu':dfsu})




""" 

LISTS  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

def sti(self,data):
	self.data=data
	self.next=None
node=type('node',(),{'__init__':sti})

def constu(self):
	self.head=None
def append(self,data):
	if self.head==None:
		self.head=node(data)
	else:
		n=node(data)
		temp=self.head 
		while temp.next!=None:
			temp=temp.next 
		temp.next=n
		n.next=None
def view(self):
	temp=self.head 
	while temp != None:
		print(temp.data)
		temp=temp.next 
def lent(self):
	temp=self.head 
	count=0 
	while temp != None:
		count+=1
		temp=temp.next 
	return count 
def remdup(self):
	head=self.head 
	while head != None and head.next != None:
		temp=head.next 
		pre=head 
		while temp != None:
			if temp.data==head.data:
				pre.next=temp.next 
				temp=temp.next
				pre=temp
			else:
				pre=temp
				temp=temp.next 
		head=head.next 

def oddeven(self):
	head=self.head 
	temp=head.next 
	pre=temp 
	c=self.len()
	while temp.next!= None:
		head.next=temp.next 
		head=temp 
		temp=temp.next 
	if c%2==0:
		head.next=pre 
		temp.next=None
	else:
		head.next=None
		temp.next=pre 
def ispal(self):
	slow=fast=pre=second=self.head
	midnode=None
	while self.head != None and self.head.next != None:
		while fast != None and fast.next != None:
			fast=fast.next.next 
			pre=slow 
			slow=slow.next 
		if fast != None:
			midnode=slow 
			slow=slow.next 
		pre.next=None
		second=slow 
		second=self.reve(second)
		res=self.compare(self.head,second)
		second=self.reve(second)
		if midnode != None:
			midnode.next=second
			pre.next=midnode
		else:
			pre.next=second
		return res 
def reve(self,second):
	temp=second
	pre=ne=None
	while temp != None:
		ne=temp.next
		temp.next=pre 
		pre=temp
		temp=ne 
	second=pre 
	return second
def compare(self,head,second):
	head1=head
	head2=second
	while head1 and head2:
		if head1.data==head2.data:
			head1=head1.next
			head2=head2.next 
		else:
			return False 
	if head1==None and head2==None:
		return True 

def delast(self,n):
	k=self.len()
	res=k-n 
	temp=self.head
	count=0
	while temp.next != None and count<res:
		count +=1
		pre=temp
		temp=temp.next 
	pre.next= temp.next 
	temp.next=None
ll=type('ll',(),{'__init__':constu,'view':view,'append':append,'len':lent,'remdup':remdup,'oddeven':oddeven,'ispal':ispal,'reve':reve,'compare':compare,'delast':delast})


"""

DRIVER CODE ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""


l=ll()
l.append(1)
l.append(1)
l.append(1)
l.append(1)
l.append(1)

root=rnode(10)
push(root,20)
push(root,21)
push(root,19)
push(root,18)
push(root,5)


g=graph()
g.append(0,1)
g.append(1,2)
g.append(1,3)
g.append(3,4)
g.append(1,5)


g = graph1(9)
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






