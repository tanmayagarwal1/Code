"""


AUTHOR : Tanmay Agarwal ; 20 April 2021
@Complex Algoithms 
Maintained at a git repo



"""


'''
1
'''
n=m=4

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
'''
2
'''

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
def issafe(maze,x,y):
	if x>=0 and x<n and y>=0 and y<n and maze[x][y]==1:
		return True 
	return False 

'''
3
'''

def goldmax(gold):
	gt=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for col in range(n-1,-1,-1):
		for row in range(m):
			if col==n-1 :
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
			gt[row][col]=gold[row][col]+max(right,right_up,right_down)

	res=gt[0][0]
	for i in range(m):
		res=max(res,gt[i][0])
	return res 

'''
4
'''

def eggs(f,n):
	dp=[[0]*(n+1)for i in range(f+1)]
	for i in range(1,f+1):
		for j in range(1,n+1):
			dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1
		if dp[i][j]>=f:
			return i 

'''
5
'''

def checker(st):
	q=[]
	v={'(':')','{':'}','[':']'}
	open_br=set(['(','[','{'])
	for i in st:
		if i in open_br:
			q.append(i)
		else:
			if i==v[q[-1]]:
				q.pop()
			else:
				return False 
	return True 

'''
12
'''

import numpy as np 
run_max=np.maximum.accumulate 
def water_collector(height):
	if not height:
		return 0 
	a=np.array(height)
	global_max=np.argmax(a)
	return np.sum(run_max(a[:global_max])-a[:global_max],dtype=np.int64)+\
			np.sum(run_max(a[:global_max:-1])-a[:global_max:-1],dtype=np.int64)

'''
13
'''
def lcs(x,y):
	n=len(x)
	m=len(y)
	lcs=[[0 for i in range(n+1)]for j in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				lcs[i][j]=0 
			elif x[j-1]==y[i-1]:
				lcs[i][j]=lcs[i-1][j-1]+1
			else:
				lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
	return lcs[m][n]

'''

14
'''
def Houses(arr,budget):
	n=len(arr)
	q=[]
	for i in range(n-1,-1,-1):
		if arr[i]>budget:
			continue
		initial= arr[i]
		count=1
		for j in range(n):
			if i==j:
				continue
			if arr[j]+initial<budget:
				initial=initial+arr[j]
				count+=1
		q.append(count)
	if not q:
		return 0 
	res=q[0]
	for i in range(len(q)):
		res=max(res,q[i])
	return res 

'''

15
'''

def unique(arr):
	n=len(arr)
	s=set()
	for i in range(n-1,0,-1):
		j=0 
		while j<i:
			if arr[i]==arr[j]:
				s.add(arr[j])
				j+=1
			j+=1
	for i in range(n):
		if arr[i] not in s:
			print(arr[i])

'''
6
'''
from collections import defaultdict
class graph:
	def __init__(self):
		self.graph=defaultdict(list)


	def append(self,s,d):
		self.graph[s].append(v)
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
					visited[i]==True 
	def dfs(self,v):
		s=set()
		self.dfsu(self,s,v)
	def dfsu(self,s,v):
		s.add(v)
		print(v)
		for i in self.graph[v]:
			if i not in s:
				self.dfsu(s,i)
'''
7
'''
class rnode:
	def __init__(self,data):
		self.data=data
		self.left=self.right=None
def push(root):
	if root==None:
		return rnode(data)
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
def adder(root):
	if root==None:
		return 0 
	else:
		return root.data+adder(root.left)+adder(root.right)
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
	else:
		res=[-99999]
		subtreeu(root,res)
		return res[0]
def subtreeu(root):
	if root==None:
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
def innvert(root):
	if root:
		root.right,root.left=root.left,root.right
		invert(root.left)
		invert(root.right)
	else:
		return 
def maxi(root):
	if root==None:
		return 0
	if root.right==None:
		return root.data
	else:
		max(root.right)
def make(root):
	q=listmaker(root)
	d=dll()
	for i in q:
		d.append(i)
	return d 
def listmaker(root):
	if root==None:
		return 
	else:
		q=[]
		h=height(root)
		for i in range(h):
			listmakeru(root,i,q)
		return q
def listmakeru(root,l,q):
	if root==None:
		return 
	if l==0:
		q.append(root.data)
	else:
		listmakeru(root.left,l-1,q)
		listmakeru(root.right,l-1,q)

'''
8
'''
class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class ll:
	def __init__(self):
		self.head=None
	def append(self,data):
		if self.head==None:
			self.head=node(data)
		else:
			temp=self.head
			n=node(data)
			while temp.next != None:
				temp=temp.next 
			temp.next=n 
			n.next=None
	def view(self):
		temp=self.head 
		while temp != None:
			print(temp.data)
			temp=temp.next 
	def len(self):
		count=0 
		temp=self.head
		while temp!= None:
			count+=1
			temp=temp.next
		return count 
	def remdup(self):
		head=self.head
		while head.next != None:
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
	def deln(self,n):
		count+=0
		l=self.len()
		res=l-n
		temp=self.head
		while temp.next != None and count<res:
			count+=1
			pre=temp
			temp=temp.next 
		pre.next=temp.next 
		temp.next=None 
	def ispal(self):
		slow=fast=second=pre=self.head
		midnode=None
		while self.head != None and self.head.next!=None:
			while fast!=None and fast.next!=None:
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
	def compare(self,head1,head2):
		head1=head1
		head2=head2
		while  head1 and head2:
			if head1.data==head2.data:
				head1=head1.next
				head2=head2.next 
			else:
				return False
		if head1==None and head2==None:
			return True 
	def __add__(self,other):
		x=self.len()
		y=other.len()
		l=ll()
		if x<y:
			temp1=self.head
			temp2=other.head 
		else:
			temp1=other.head 
			temp2=self.head 
		while temp1 and temp2:
			l.append(temp1.data+temp2.data)
			temp1=temp1.next
			temp2=temp.next 
		while temp2!=None:
			l.append(temp2)
		return l 
	def sum(self):
		res=0 
		temp=self.head 
		while temp!=None:
			res=temp.data+res 
			temp=temp.next 
		return res 

'''
9
'''

class dll:
	def __init__(self):
		self.head=None
	def append(self,data):
		if self.head==None:
			self.head=rnode(data)
		else:
			n=rnode(data)
			temp=self.head 
			while temp.right != None:
				temp=temp.right 
			temp.right=n
			n.left=temp
			n.right=None
	def view(self):
		temp=self.head 
		while temp != None:
			print(temp.data)
			temp=temp.right 
'''
10

'''
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

def remdup(arr):
	for i in range(len(arr)-1,0,-1):
		j=0 
		while j<i:
			if arr[j]==arr[i]:
				print(arr[j])
				j+=1
			else:
				j+=1
def remdup2(arr):
	v=set()
	for i in range(len(arr)):
		if arr[i] not in v:
			v.add(arr[i])
		else:
			print(arr[i])
def reve(arr):
	n=len(arr)
	j=0 
	for i in range(n-1,n//2,-1):
		if arr[i].isalpha():
			while j<i:
				if arr[j].isalpha():
					arr[j],arr[i]=arr[i],arr[j]
					j+=1
					break 
				else:
					j+=1
	return arr 
def kaden(arr):
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

def splitnum(num):
	j=[int(i) for i in str(num)]
	return j 

def target(arr,sum):
	for i in range(len(arr)-1,0,-1):
		for j in range(0,i):
			if arr[j]+arr[i]==sum:
				return i,j 
			else:
				continue 

def window_max_sum(arr,k):
	n=len(arr)
	res=0
	window_max=sum(arr[:k])
	for i in range(n-k):
		window_max=window_max-arr[i]+arr[i+k]
		res=max(res,window_max)
	return res 

def windwo_max_element(arr,k):
	n=len(arr)
	q=[]
	res=float('-inf') 
	for i in range(k):
		q.append(arr[i])
	for i in range(n-k+1):
		for j in range(k):
			res=max(res,q[j])
		q.pop(0)
		if i+k<n:
			q.append(arr[i+k])
	return res 



'''

11

'''

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
	while l<n and arr[large]<arr[l]:
		large=l
	while r<n and arr[large]<arr[r]:
		large=r
	if large != i :
		arr[large],arr[i]=arr[i],arr[large]
		Heapify(arr,n,large)
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
			k+=1
		while j<len(r):
			arr[k]=r[j]
			k+=1
			j+=1
arr=[90,20,40,90]
l=ll()
l.append(1)
l.append(1)
l.append(1)
l.append(1)
l.append(1)
l.append(1)

