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

def mazesolver(maze):
	sol=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if mazsolveru(maze,0,0,sol)==False:
		return False 
	printsol(sol)
def mazsolveru(maze,x,y,sol):
	if x==n-1 and y==n-1 and maze[x][y]==1:
		sol[x][y]==1
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

def eggs(f,n):
	dp=[[0]*(n+1)for i in range(f+1)]
	for i in range(1,f+1):
		for j in range(1,n+1):
			dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1
		if dp[i][j]>=f:
			return i 

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

					
######Sorts Not Woking ##########################
	def mergesort(self):
		if len(self.a)>1:
			mid=len(self.a)//2
			l=self.a[:mid]
			r=self.a[mid:]
			self.mergesort(l)
			self.mergesort(r)
			i=j=k=0
			while i<len(l) and j<len(r):
				if l[i]<r[j]:
					self.a[k]=l[i]
					i+=1
				else:
					self.a[k]=r[j]
					j+=1
				k+=1
			while i<len(l):
				self.a[k]=l[i]
				i+=1
				k+=1
			while j<len(r):
				self.a[k]=r[j]
				j+=1
				k+=1
			return self.a
	def heapsort(self):
		n=len(self.a)
		for i in range(n//2-1,-1,-1):
			Heapify(self.a,n,i)
		for i in range(n-1,0,-1):
			self.a[0],self,a[i]=self.a[i],self.a[0]
			Heapify(self.a,i,0)
	def Heapify(self,arr,n,i):
		large=i 
		l=2*i+1
		r=2*i+2
		if l<n and arr[large]<arr[l]:
			large=l 
		if r<n and arr[larhe]<arr[r]:
			large=r 
		if large != i:
			arr[large],arr[i]=arr[i],arr[large]
			Heapify(arr,n,large)

##########################################################

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




l=ll()
l.append(1)
l.append(1)
l.append(1)
l.append(1)
l.append(1)

#l.view()
print(l.ispal())










#arr=[1,2,3,4,213,123,453]
#a=A(arr)
#x=a.mergesort()







