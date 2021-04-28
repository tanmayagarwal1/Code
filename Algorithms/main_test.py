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
		sol[x][y]=0 
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
		for row in range(m):
			if col==n-1:
				right=0 
			else:
				right=gt[row][col+1]
			if col==n-1 or row==n-1:
				right_down=0 
			else:
				right_down=gt[row+1][col+1]
			if row==0 or col==n-1:
				right_up=0 
			else:
				right_up=gt[row-1][col+1]
			gt[row][col]=gold[row][col]+max(right,right_down,right_up)
	res=gt[0][0]
	for i in range(n):
		res=max(res,gt[i][0])
	return res 

def eggs_max(f,n):
	x=[[0 for i in range(n+1)]for j in range(f+1) ]
	for i in range(1,f+1):
		for j in range(1,n+1):
			x[i][j]=x[i-1][j-1]+x[i-1][j]+1
		if x[i][j]>=f:
			return i 
import numpy as np 
run_max=np.maximum.accumulate 
def water_collector(height):
	x=np.array(height)
	global_max=np.argmax(x)
	return np.sum(run_max(x[:global_max])-x[:global_max],dtype=np.int64)+\
			np.sum(run_max(x[:global_max:-1])-x[:global_max:-1],dtype=np.int64)

def Houses(arr,budget):
	q=[]
	n=len(arr)
	for i in range(n-1,-1,-1):
		if arr[i]>budget:
			continue 
		initial=arr[i]
		count=1 
		for j in range(n):
			if i==j:
				continue
			if arr[j]+initial<=budget:
				initial=initial+arr[j]
				count+=1
		q.append(count)
	if not q:
		return 0 
	res=q[0]
	for i in range(len(q)):
		res=max(res,q[i])

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
	for i in range(len(arr)):
		j=0 
		while j<i:
			if arr[j]==arr[i]:
				print(arr[j])
				j+=1
			else:
				j+=1
def dups2(arr):
	s=set()
	for i in range(len(arr)):
		if arr[i] not in s:
			s.add(arr[i])
		else:
			print(arr[i])
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

def unique(sti):
	n=len(sti)
	s=set()
	for i in range(n-1,-1,-1):
	 	j=0 
	 	while j<i:
	 		if sti[j]==sti[i]:
	 			s.add(sti[j])
	 			j+=1
	 		else:
	 			j+=1
	for i in range(n):
	 	if sti[i] not in s:
	 		print(sti[i])

def sliding(arr,k):
	n=len(arr)
	q=[]
	res=arr[0]
	for i in range(k):
		q.append(arr[i])
	for i in range(n-k+1):
		for j in range(k):
			res=max(res,q[j])
		q.pop(0)
		if i+k<n:
			q.append(arr[i+k])
	return res 
def window(arr,k):
	n=len(arr)
	res=0 
	window_sum=sum(arr[:k])
	for i in range(n-k):
		window_sum=window_sum-arr[i]+arr[i+k]
		res=max(res,window_sum)
	return res
print(sliding([1,2,3,4,5,6,2,1,124,3],2))



