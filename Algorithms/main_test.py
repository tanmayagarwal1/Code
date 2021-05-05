global m 
global n 
m=n=4
import numpy as np 
from collections import defaultdict 
run_max=np.maximum.accumulate 

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
            gt[row][col]=gold[row][col]+max(right_up,right_down,right)
    res=gt[0][0]
    for i in range(m):
        res=max(res,gt[i][0])
    return res 

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

def water_collector(height):
    a=np.array(height)
    global_max=np.argmax(a)
    return np.sum(run_max(a[:global_max])-a[:global_max],dtype=np.int64)+\
            np.sum(run_max(a[:global_max:-1])-a[:global_max:-1],dtype= np.int64)

def egg_max(f,n):
    dp=[[0 for _ in range(n+1)]for _ in range(f+1)]
    for i in range(1,f+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+1 # Eggs break= florr down and egg no break, still floor down 
        if dp[i][j]>=f:
            return i 
def lcs(x,y):
    m=len(x)
    n=len(y)
    dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[j-1]==y[i-1]:
                dp[i][j]=dp[i-1][j-1]+1 # If equal, diagonal of upper left+!
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1]) # Maximum of top and left 
    return dp[n][m]

def MinimumCost(cost,x,y):
    m=3 
    n=3 
    dp=[[0 for _ in range(m)]for _ in range(n)]
    dp[0][0]=cost[0][0]
    for dx in range(1,n):
        dp[dx][0]=dp[dx-1][0]+cost[dx][0]
    for dy in range(1,m):
        dp[0][dy]=dp[0][dy-1]+cost[0][dy]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+cost[i][j]
    return dp[x][y]

def regularexpression(sti,pattern):
    m=len(sti)
    n=len(pattern)
    dp=[[False for _ in range(n+1)]for _ in range(m+1)]
    dp[0][0]=True 
    for dx in range(1,n+1):
        if pattern[dx-1]=='*':
            dp[0][dx]=dp[0][dx-2]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if pattern[j-1]=='.' or sti[i-1]==pattern[j-1]:
                dp[i][j]=dp[i-1][j-1] #Diagonal 
            if pattern[j-1]=='*':
                dp[i][j]=dp[i][j-2] #previous element 
                if pattern[j-2]=='.' or sti[i-1]==pattern[j-1]:
                    dp[i][j]=dp[i-1][j] # Top 
    return dp[m][n]


def Houses(arr,b):
    n=len(arr)
    q=[]
    for i in range(n):
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
    res=0 
    for i in range(len(q)):
        res=max(res,q[i])
    return res 

def Blocks(arr,interests):
    q=[]
    for i in arr:
        count=0 
        for j,k in i.items():
            for dx in range(len(interests)):
                if j==interests[dx] and k==True:
                    count+=1 
        q.append(count)
    res=0 
    for i in range(len(q)):
        res=max(res,q[i])
    return q.index(res)+1

def subarraysum(arr,k):
    window_sum=sum(arr[:k])
    res=0 
    n=len(arr)
    for i in range(n-k):
        window_sum=window_sum-arr[i]+arr[i+k]
        res=max(res,window_sum)
    return res 

def maxelement(arr,k):
    n=len(arr)
    q=[]
    for dx in range(k):
        q.append(arr[dx])
    res=0 
    for i in range(n-k+1):
        for j in range(k):
            res=max(res,q[j])
        q.pop(0)
        if i+k<n:
            q.append(arr[i+k])
    return res 
def checker(sti):
    dic={'{':'}','(':')','[':']'}
    s=set(['{','(','['])
    q=[]
    for i in sti:
        if i in s:
            q.append(i)
        else:
            if i==dic[q[-1]]:
                q.pop()
            else:
                return False
    return True 
def encoding(mymap,sti):
    ogmap='abcdefghijklmnopqrstuvwxyz'
    q=[]
    dic=dict(zip(ogmap,mymap))
    for i in sti:
        q.append(dic[i])
    return ''.join(q)

def startigWith(arr,pattern):
    q=[]
    for i in arr:
        count=0 
        for j in range(len(pattern )):
            if i[j]==pattern[j]:
                count+=1
            else:
                break 
            if count==len(pattern):
                q.append(i)
    return q 

def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        Heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        Heapify(arr,i,0)
def Heapify(arr,n,i):
    large=i 
    r=2*i+1
    l=2*i+2
    if l<n and arr[large]<arr[l]:
        large=l 
    if r<n and arr[large]<arr[r]:
        large=r 
    if large!=i:
        arr[large],arr[i]=arr[i],arr[large]
        Heapify(arr,n,large)

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0 
        while i<len(l) and j< len(r):
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
class graph: 
    def __init__(self):
        self.graph=defaultdict(list)
    def append(self,s,d):
        self.graph[s].append(d)
    def bfs(self,s):
        visited=[False]*1000
        q=[]
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
class graph1:
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
                if self.graph[u][x]>1 and visited[x]==False and dist[x]>dist[u]+self.graph[u][x]:
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
'''
------------------------------------------------------------------------------------------------------------

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

def dups(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]==arr[i]:
                print(arr[j])
def dups2(arr):
    n=len(arr)
    s=set()
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
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

def target(arr,target):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j]+arr[i]==target:
                return i,j 
    return False 

def unique(sti):
    n=len(sti)
    s=set()
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if sti[i]==sti[j]:
                s.add(sti[j])
    for i in sti:
        if i not in s:
            print(i)



'''
------------------------------------------------------------------------------------------------------------

'''

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
def subtreeu(root,res):
    if root==None:
        return 0 
    else:
        cur=root.data+subtreeu(root.left,res)+subtreeu(root.right,res)
        res[0]=max(res[0],cur)
        return cur 

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
def invert(root):
    if root:
        root.left,root.right=root.right,root.left
        invert(root.left)
        invert(root.right)
    else:
        return 

def maximum(root):
    if root==None:
        return 0
    if root.right==None:
        print(root.data)
    else:
        maximum(root.right)

'''
------------------------------------------------------------------------------------------------------------

'''

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
        while temp!= None:
            print(temp.data)
            temp=temp.next 
    def ispal(self):
        slow=second=fast=pre=self.head 
        midnode=None
        if self.head != None and self.head.next != None:
            while fast != None and fast.next != None:
                fast=fast.next.next 
                pre=slow 
                slow=slow.next 
            if fast != None:
                midnode=slow 
                slow=slow.next 
        second=slow 
        pre.next=None
        second=self.rev(second)
        res=self.compare(self.head,second)
        second=self.rev(second)
        if midnode!=None:
            midnode.next=second
            pre.next=midnode
        else:
            pre.next=second
        return res 

    def rev(self,second):
        temp=second
        pre=ne=None
        while temp != None:
            ne=temp.next
            temp.next =pre
            pre=temp 
            temp=ne 
        second=pre 
        return second
    def compare(self,head1,head2):
        while head1 and head2:
            if head1.data==head2.data :
                head1=head1.next 
                head2=head2.next 
            else:
                return False 
        if head1==None and head2==None:
            return True 
    def len(self):
        count=0 
        temp=self.head
        while temp != None:
            count+=1
            temp=temp.next 
        return count 

    def delnth(self,k):
        n=self.len()
        res=n-k 
        count=0 
        pre=temp=self.head 
        while temp!=None and count<res:
            count+=1
            pre=temp
            temp=temp.next 
        pre.next=temp.next 
        temp.next=None
    def oddeven(self):
        head=self.head 
        temp=head.next 
        n=self.len()
        pre=temp 
        while temp.next !=None:
            head.next=temp.next 
            head=temp
            temp=temp.next 
        if n%2==0:
            head.next=pre
            temp.next=None
        else:
            temp.next=pre 
            head.next=None
    def dups(self):
        head=self.head 
        while head!=None and head.next != None:
            temp=head.next 
            pre=head 
            while temp!=None:
                if temp.data==head.data:
                    pre.next=temp.next 
                    temp=temp.next 
                    pre=temp 
                else:
                    pre=temp
                    temp=temp.next 
            head=head.next 

    def rotate(self,n):
        temp=self.head 
        while temp.next!=None:
            temp=temp.next 
        temp.next=self.head 
        nthnode=self.head
        count=0 
        while count<n:
            count +=1
            nthnode=nthnode.next 
        self.head=nthnode.next 
        nthnode.next=None

li=ll()
li.append(1)
li.append(0)
li.append(0)
li.append(1)
print(li.ispal())

