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
			if nqueenu(b,col+1):
				return True 
			b[i][col]=0 
	return False 
def issafe(b,row,col):
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
	gt=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for col in range(n-1,-1,-1):
		for row in range(n):
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

def eggs_max(f,n):
	dp=[[0]*(n+1) for i in range (f+1)]
	for i in range(1,f+1):
		for j in range(1,n+1):
			dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1
		if dp[i][j]>=f:
			return i 
def checker(sti):
	q=[]
	v={'[':']','{':'}','(':')'}
	open_br=set(['{','[','('])
	for i in sti:
		if i in open_br:
			q.append(i)
		else:
			if i==v[q[-1]]:
				q.pop()
			else:
				return False 
	return True 

import numpy as np 
run_max=np.maximum.accumulate 

def water_collector(height):
	a=np.array(height)
	global_max=np.argmax(a)
	return np.sum(run_max(a[:global_max])-a[:global_max],dtype=np.int64)+\
			np.sum(run_max(a[:global_max:-1])-a[:global_max:-1],dtype=np.int64)

def lcs(x,y):
	n=len(x)
	m=len(y)
	lcs=[[0 for i in range(m+1)]for j in range(n+1)]
	for i in range(n+1):
		for j in range(m+1):
			if i==0 and j==0:
				lcs[i][j]=0 
			elif x[i-1]==y[j-1]:
				lcs[i][j]=lcs[i-1][j-1]+1
			else:
				lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
	return lcs[n][m] 


class graph:
	def __init__(self,v):
		self.v=v
		self.graph=[[0 for i in range(self.v)]for j in range(self.v)]
	def shortestPath(self,s):
		dist=[float('inf')]*self.v
		visited=[False]*self.v
		dist[s]=0 
		for i in range(self.v):
			u=self.minvertex(dist,visited)
			visited[u]=True 
			for x in range(self.v):
				if self.graph[u][x]>0 and visited[x]==False and dist[x]>dist[u]+self.graph[u][x]:
					dist[x]=dist[u]+self.graph[u][x]
		self.printsol(dist)
	def minvertex(self,dist,visited):
		min=float('inf')
		for i in range(self.v):
			if dist[i]<min and visited[i]==False:
				min=dist[i]
				min_index=i 
		return min_index 
	def printsol(self,dist):
		for i in range(self.v):
			print(f"{i} : {dist[i]}")


def encoding(newmap,sti):
    ogmap='abcdefghijklmnopqrstuvwxyz'
    q=[]
    d=dict(zip(newmap,ogmap))
    for i in sti: 
        q.append(d[i])
    return ''.join(q) 

def mergesort(arr):
	if len(arr)>1:
		mid=len(arr)//2
		l=arr[:mid]
		r=arr[mid:]
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
			k+=1
		while j<len(r):
			arr[k]=r[j]
			j+=1
			k+=1
def heapsort(arr):
	n=len(arr)
	for i in range(n//2-1,-1,-1):
		Heapify(arr,n,i)
	for i in range(n-1,0,-1):
		arr[i],arr[0]=arr[0],arr[i]
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
def trips(arr):
	n=len(arr)
	for i in range(n):
		arr[i]=arr[i]**2 
	arr.sort()
	for i in range(n-1,1,-1):
		j=0 
		k=i-1
		while j<k:
			if arr[j]+arr[k]==arr[i]:
				return True 
			else:
				if arr[j]+arr[k]<arr[i]:
					j+=1
				else:
					k-=1
	return False 
def dups(arr):
	n=len(arr)
	v=set()
	for i in range(n):
		if arr[i] not in v:
			v.add(arr[i])
		else:
			print(arr[i])
def kadens(arr):
	n=len(arr)
	i=arr[0]
	j=0
	for k in range(n):
		j=j+arr[k]
		if i<j:
			i=j 
		if j<0:
			j=0 
	return i 
def special_reve(arr):
	n=len(arr)
	j=0 
	for i in range(n-1,n//2,-1):
		if arr[i].isalpha():
			while j<i:
				if arr[j].isalpha():
					arr[i],arr[j]=arr[j],arr[i]
					j+=1
					break 
				else:
					j+=1
from collections import defaultdict
class graph1:
	def __init__(self):
		self.graph=defaultdict(list )
	def append(self,s,d):
		self.graph[s].append(d)
	def bfs(self,s):
		visited=[False]*1000 
		q=[]
		visited[s]=True 
		q.append(s)
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
def dups2(arr):
	n=len(arr)
	for i in range(n-1,0,-1):
		j=0 
		while j<i:
			if arr[j]==arr[i]:
				print(arr[j])
				j+=1
			else:
				j+=1

class node:
	def __init__(self,data):
		self.data=data
		self.left=self.right=None
def push(root,data):
	if root==None:
		return node(data)
	else:
		if root.data<data:
			root.right=push(root.right,data)
		elif root.data>data:
			root.left=push(root.left,data)
		return root 
def show(root):
	if root:
		show(root.left)
		print(root.data)
		show(root.right)
	else:
		return 
def add(root):
	if root==None:
		return 0 
	else:
		return root.data+add(root.left)+add(root.right)
def leaf(root):
	if root==None:
		return 0 
	if root.left==None and root.right==None:
		return 1 
	else:
		return leaf(root.left)+leaf(root.right)
def invert(root):
	if root:
		root.left,root.right=root.right,root.left
		invert(root.left)
		invert(root.right)
	else:
		return 
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
def subtree(root):
	if root==None:
		return 0 
	else:
		res=[-99999]
		subtreeu(root,res)
		return res[0]
def subtreeu(root,res):
	if root==None:
		return 0 
	else:
		cur=root.data+subtreeu(root.left,res)+subtreeu(root.right,res)
		res[0]=max(res[0],cur)
		return cur 
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
def maximum(root):
	if root==None:
		return 0 
	if root.right==None:
		print(root.data)
	else:
		maximum(root.right)

class lnode:
	def __init__(self,data):
		self.data=data
		self.next=None
class ll:
	def __init__(self):
		self.head=None
	def append(self,data):
		if self.head==None:
			self.head=lnode(data)
		else:
			n=lnode(data)
			temp=self.head 
			while temp.next != None:
				temp=temp.next 
			temp.next=n
			n.next=None
	def view(self):
		temp=self.head 
		while temp !=None:
			print(temp.data)
			temp=temp.next 
	def rempdup(self ):
		head=self.head 
		while head.next != None and head != None:
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
	def oddeve(self):
		head=self.head 
		temp=head.next 
		pre=temp 
		n=self.len()
		while temp.next != None:
			head.next=temp.next 
			head=temp 
			temp=temp.next 
		if n%2==0:
			head.next=pre 
			temp.next=None
		else:
			temp.next=pre 
			head.next=None
	def len(self):
		count=0 
		temp=self.head 
		while temp != None:
			count+=1
			temp=temp.next 
		return count 
	def ispal(self):
		second=fast=slow=pre=self.head 
		midnode=None
		while self.head != None and self.head.next != None:
			while fast != None and fast.next!=None:
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
			if midnode!=None:
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
	def compare(self,head1,head2):
		while head1 and head2:
			if head1.data==head2.data:
				head1=head1.next 
				head2=head2.next 
			else:
				return False
		if head1 ==None and head2==None:
			return True 
	def lastdel(self,num):
		n=self.len()
		res=n-l
		count =0 
		temp=self.head
		while temp != None and count<res:
			count+=1
			pre=temp
			temp=temp.next 
		pre.next=temp.next 
		temp.next=None
	def __add__(self,other):
		l=ll()
		x=self.len()
		y=other.len()
		if x<y:
			temp1=self.head
			temp2=other.head 
		else:
			temp1=other.head 
			temp2=self.head 
			while temp1 != None:
				l.append(temp1.data+temp2.data)
				temp1=temp1.next 
				temp2=temp2.next 
			while temp2!=None:
				l.append(temp2.data)
		return l 
l=ll()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)

l1=ll()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)

l3=l+l1


print(lcs('tanmay','agarwal'))

