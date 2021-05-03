'''
This file contains a few Dynamic programming examples in one 

'''

def regularexpression(sti,pattern):
	m=len(sti)
	n=len(pattern)
	dp=[[False for _ in range(n+1)]for _ in range(m+1)]
	dp[0][0]=True 
	for i in range(1,n+1):
		if pattern[i-1]=='*':
			dp[0][i]=dp[0][i-2]
	for i in range(1,m+1):
		for j in range(1,n+1):
			if pattern[j-1]=='.' or (sti[i-1]==pattern[j-1]):
				dp[i][j]=dp[i-1][j-1]
			if pattern[j-1]=='*':
				dp[i][j]=dp[i][j-2] # If * assign the secind previous 
				if pattern[j-2]=='.' or sti[i-1]==pattern[j-2]: # Check for matching with second previous in pattern sring 
					dp[i][j]=dp[i-1][j]
	return dp[m][n]

def lcs(x,y):
	n=len(x)
	m=len(y)
	dp=[[0 for i in range(n+1)]for j in range(m+1)]
	for i in range(1,m+1):
		for j in range(1,n+1):
			if x[j-1]==y[i-1]:
				dp[i][j]=dp[i-1][j-1]+1
			else:
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	return dp[m][n]
def minimumCostPath(cost,x,y):
	m=3
	n=3
	dp=[[0 for _ in range(m)]for _ in range(n)]
	dp[0][0]=cost[0][0]
	for i in range(1,n):
		dp[i][0]=dp[i-1][0]+cost[i][0]
	for i in range(1,m):
		dp[0][i]=dp[0][i-1]+cost[0][i]
	for i in range(1,n):
		for j in range(1,m):
			dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+cost[i][j]
	return dp[x][y]

def eggs_max(f,n):
	dp=[[0 for i in range(n+1)]for j in range(f+1)]
	for i in range(1,f+1):
		for j in range(1,n+1):
			dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1
		if dp[i][j]>=f:
			return i 
def goldmax(gold):
	gt=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	m=n=4
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
			gt[row][col]=gold[row][col]+max(right,right_up,right_down)
	res=gt[0][0]
	for i in range(m):
		res=max(res,gt[i][0])
	return res 

gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]
        
print(goldmax(gold))