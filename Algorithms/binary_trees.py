#IF WE ARE USING TREES AND WANT TO CREATE ANY FUNCTION WHICH COUNTS OR ADDS ANYTHING THE BASE CASE MUST RETURN 0
class stack: 
    def __init__(self,size):
        self.count=0
        self.size=size
        self.a=[0]*self.size
        self.top=self.a[self.count]
    def push(self,data):
        if self.count < self.size : 
            self.a[self.count]=data
            self.count=self.count+1
            #print("pushed {}".format(data))
        else:
            print("overflow")    
    def pop(self):
        if self.count != 0:
            self.count=self.count-1
            print(f"{self.a[self.count]}" )
            self.a[self.count]=0
        else: 
            print("underflow")    
    def show(self):
        for i in self.a:
            print(i)    
        

class queue:
    def __init__(self, size):
        self.size=size
        self.a=[None]*self.size 
        self.front=0 
        self.rear=0 
        
    def push(self,data):
        if self.rear<self.size:
            self.a[self.rear]=data 
            self.rear=self.rear+1 
        else:
            print("overflow")
    def pop(self):
        print(self.a[self.front])
        self.front=self.front+1
        
    def show(self):
        for i in self.a:
            print(i)

class node: 
    def __init__(self,data):
        self.data=data
        self.left=self.right=None 
def push(root, data):
    if root == None: 
        return node(data)
    else: 
        if root.data > data:
            root.left=push(root.left,data)
        elif root.data < data:
            root.right=push(root.right,data)
        return root 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    else:
        return 

def findkey(root,key):
    if root==None: 
        print("no root")
    else:
        if root.data==key:
            print("key found at {} node".format(root.data))
        elif root.data>key:
            findkey(root.left,key)
        elif root.data<key:
            findkey(root.right,key)  
        else:
            print("key not found")    

def invert(root):
    if root: 
        root.left,root.right=root.right,root.left 
    else: 
        return root    
    invert(root.left)
    invert(root.right)    

def stackorder(root,key):
    if not root:
        root=node(key)
        return 
    q=[]
    q.append(root)
    while(len(q)):
        temp=q[0]
        q.pop(0)
        if not temp.left:
            temp.left= node(key)
        else : 
            q.append(temp.left) 
        if not temp.right:
            temp.right=node(key)
        else:
            q.append(temp.right)
def add(root):
    if root ==None: 
        return 0 
    else : 
        return(root.data + add(root.left)+ add(root.right))

###maximum subtree
def subtree(root,ans):
    if root == None: 
        return 0     
    curr=(root.data+subtree(root.left,ans)+subtree(root.right,ans))
    ans[0]=max(ans[0],curr)
    return curr 
def mainsubtree(root):
    if root == None: 
        return 0 
    ans = [-999999999999]
    subtree(root,ans)
    print(ans[0])

def leaf(root):
    if root==None:
        return 0 
    if root.left==None and root.right==None:
        return 1
    else: 
        return leaf(root.left)+leaf(root.right)  

def height(root):
    if root==None:
        return 0 
    else:
        l=height(root.left)
        r=height(root.right)
        if l>r:
            return l+1
        else: 
            return r+1
def kthanc(root,v,k):
    if root == None:
        return None
    if(root.data == v or (kthanc(root.left,v,k)) or (kthanc(root.right,v,k))):
        if k[0]>0:
            k[0]-=1
        elif k[0]==0:
            print(root.data)
            return None 
        return root 
def isValid(root):
    return IsValidHelper(root, float('-inf'),float('inf'))

def IsValidHelper(root, lower, upper):
    if root==None:
        return True 
    if lower < root < upper :
        return IsValidHelper(root.left, lower, root.data) and \
               IsValidHelper(root.right, root.data, upper)
    else:
        return False 

def IsSymmetric(root):
    return IsSymmetricHelper(root.left, root.right)

def IsSymmetricHelper(left_root, right_root):
    q=[(left_root, right_root)]
    while q:
        x, y =q.pop(0)
        if not x and not y :
            continue 
        if not x or y:
            return False
        if x.data != y.data:
            return False
        else:
            q.append((x.left, y.right))
            q.append((x.right, y.left))
        return True 

def delete(root, n):
    if root.left:
        root.left= delete(root.left, n)
    if root.right: 
        root.right = delete(root.right, n)
    if root.data == n:
        return None
    return root 





root=node(5)
push(root,10)
push(root,15)
push(root,6)
push(root,8)
push(root,1)

inorder(root)
#print("The sum is {}".format(add(root)))
#s=stack(5)
#for i in range(1,6):
    #s.push(i)
print(leaf(root))    







            


