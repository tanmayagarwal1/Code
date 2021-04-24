global n
global m 
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
def  mazesolveru(maze,x,y,sol):
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
        for row in range(m):
            if col==n-1:
                right=0 
            else:
                right=gt[row][col+1]
            if col==n-1 or row==n-1:
                right_down=0 
            else:
                right_down=gt[row+1][col+1]
            if col==n-1 or row==1:
                right_up=0 
            else:
                right_up=gt[row-1][col+1]
            gt[row][col]=gold[row][col]+max(right_down,right_up,right)
    res=gt[0][0]
    for i in range(n):
        res=max(res,gt[i][0])
    return res 

def checker(sti):
    v={'(':')','{':'}','[':']'}
    z=set(['(','{','['])
    q=[]
    for i in sti:
        if i in z:
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
def eggs_max(f,n):
    dp=[[0]*(n+1) for i in range(f+1)]
    for i in range(1,f+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1
        if dp[i][j]>=f:
            return i 
def encoding(newmap,sti):
    ogmap='abcdefghijklmnopqrstuvwxyz'
    q=[]
    d=dict(zip(newmap,ogmap))
    for i in sti: 
        q.append(d[i])
    s=''.join(q)
    return s 

sti='{()}'
mymap='qwertyuiopasdfghjklzxcvbnm'
print(encoding(mymap,'tanmay'))
