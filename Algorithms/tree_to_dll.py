q=[]
class node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

################LIST FUNCTIONS
class dll:
    def __init__(self):
        self.head=None
    def append(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            nn=node(data)
            temp=self.head
            while temp.right != None:
                temp=temp.right
            temp.right=nn
            nn.left=temp
            nn.right=None
    def show(self):
        temp=self.head
        while temp != None:
            print(temp.data)
            temp=temp.right 
################TREE FUNCTIONS    
def push(root,data):
    if root==None:
        return node(data)
    else:
        if root.data<data:
            root.right=push(root.right,data)
        elif root.data>data:
            root.left=push(root.left,data)
        return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    else:
        return 
###############FUNCTIONS TO CONVERT A TREE TO AN ARRAY IN LEVEL ORDER  
def levelextract(root):
    h=height(root)
    for i in range(h):
        levelutil(root,i)
    return q

def levelutil(root,h):
    if root==None:
        return 0 
    else:
        if h==0:
            q.append(root.data)
        else:
            levelutil(root.left,h-1)
            levelutil(root.right,h-1)
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

        
########CREATING TREE AND LIST 
li=dll()
root=node(5)
push(root,7)
push(root,8)
push(root,1)
push(root,3)
#inorder(root)
x=levelextract(root)
for i in x:
    li.append(i)
li.show()


