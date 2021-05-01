n=m=4
def nqueen():
	b=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if nqueenu(b,0)==False:
		return False 
	printsl(b)
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
	for i in range(n-1,0,-1):
		j=0 
		while j<i:
			if arr[j]==arr[i]:
				print(arr[j])
				j+=1
			else:
				j+=1
def dups2(arr):
	n=len(arr)
	s=set()
	for i in arr:
		if i not in s:
			s.add(i)
		else:
			print(i)
def kadens(arr):
	n=len(arr)
	i=arr[0]
	j=0 
	for k in range(len(arr)):
		j=j+arr[k]
		if i<j:
			i=j 
		if j<0:
			j=0
	return i 

def target(arr,t):
	n=len(arr)
	for i in range(n):
		for j in range(i+1,n):
			if arr[i]+arr[j]==t:
				return i,j 

def unique(sti):
	n=len(sti)
	s=set()
	for i in range(n-1,0,-1):
		j=0 
		while j<i:
			if arr[j]==ar[i]:
				s.add(arr[j])
				j+=1
			else:
				j+=1
	for i in sti:
		if i not in s:
			print(i)

def maxwindow(arr,k):
	q=[]
	for i in range(k):
		q.append(arr[i])
	res=0 
	n=len(arr)
	for i in range((n-k)+1):
		for j in range(k):
			res=max(res,q[j])
		q.pop(0)
		if  i+k<n:
			q.append(arr[i+k])
	return res

def subarraysum(arr,k):
	window_sum=sum(arr[:k])
	n=len(arr)
	res=0
	for i in range(n-k):
		window_sum=window_sum-arr[i]+arr[i+k]
		res=max(res,window_sum)
	return window_sum

def Houses(arr,b):
	n=len(arr)
	q=[]
	for i in range(n-1,-1,-1):
		if arr[i]>b:
			continue 
		initial=arr[i]
		count=1 
		for j in range(n):
			if i==j:
				continue 
			if arr[j]+initial<=b:
				initial=initial+arr[j]
				count+=1
		q.append(count)
	res=q[0]
	for i in range(len(q)):
		res=max(res,q[i])
	return res 

def Blocks(arr,interests):
	q=[]
	for i in arr:
		count=0 
		for j,k in i.items():
			for z in range(len(interests)):
				if j==interests[z] and k==True:
					count+=1
		q.append(count)
	res=q[0]
	for i in range(len(q)):
		res=max(res,q[i])
	return q.index(res)+1

def startingWith(arr,pat):
	q=[]
	for i in arr:
		count=0 
		for j in range(len(pat)):
			if i[j]==pat[j]:
				count+=1
			else:
				break 
			if count==len(pat):
				q.append(i)
	return q 

print(maxwindow([1,2,3,4,5,6,7,8,9,10,11],3))









