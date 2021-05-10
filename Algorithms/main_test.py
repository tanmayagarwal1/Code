class node:
    def __init__(self,data):
        self.data=data
        self.left = self.right = None
def push(root,data):
    if root == None:
        return node(data)
    else:
        if root.data < data:
            root.right = push(root.right,data)
        elif root.data > data:
            root.left = push(root.left,data)
        return root 
def show(root):
    if root:
        show(root.left)
        print(root.data)
        show(root.right)
    else:
        return 
def Adder(root):
    if not root:
        return 0 
    else:
        return root.data + Adder(root.left) + Adder(root.right)
def Leaf(root):
    if not root:
        return 0 
    if root.left == None and root.right == None:
        return 1 
    else:
        return Leaf(root.left) + Leaf(root.right)
def subtree(root):
    if not root:
        return 0 
    res=[-99999]
    subtreeu(root, res)
    return res[0]
def subtreeu(root, res):
    if root == None:
        return 0 
    curr = root.data + subtreeu(root.left, res) + subtreeu(root.right, res)
    res[0] = max(res[0],curr)
    return curr
def Height(root):
    if root==None:
        return 0 
    else:
        l = Height(root.left)
        r = Height(root.right)
        if l < r:
            return r + 1
        else :
            return l + 1
def LevelOrder(root):
    if not root:
        return 
    else:
        h = Hieght(root)
        for i in range(h):
            LevelOrderu(root, i )

def LevelOrderu(root, l):
    if not root:
        return 
    if l == 0:
        print(root.data)
    else:
        LevelOrderu(root.left, l-1)
        LevelOrderu(root.right, l-1)
def Invert(root):
    if root:
        root.left, root.right = root.right, root.left
        Invert(root.left)
        Invert(root.right)
    else:
        return 
def Maximum(root):
    if not root:
        return 
    if not root.right:
        print(root.data)
    else:
        Maximum(root.right)
def Kthanc(root, n, k):
    if not root:
        return 0 
    if root.data == n or Kthanc(root.left, n, k) or Kthanc(root.right, n, k):
        if k[0] > 0 :
            k[0] -= 1
        elif k[0] == 0:
            print(root.data)
            return None
        return root 

def IsSymmetric(root):
    return IsMirror(root.left, root.right)

def IsMirror( left_root, right_root):
    q=[(left_root, right_root)]
    while q :
        x, y = left_root, right_root
        if not x and not y:
            continue 
        if not x or not y:
            return False 
        if x.data != y.data :
            return False 
        else:
            q.append((x.left, y.right))
            q.append((x.right, y.left))
        return True  

def Isvalid(root):
    return IsCorrect (root, float('-inf'), float('inf'))

def IsCorrect(root, lower, upper):
    if not root:
        return True 
    if lower < root.data < upper :
        return IsCorrect(root.left, lower, root.data) and IsCorrect(root.right, root.data, upper)
    return False 

def Delete(root, n):
    if root.right:
        root.right = Delete(root.right, n)
    if root.left :
         root.left = Delete(root.left, n)
    if root.data == n:
        return None
    return root 

def Search(root, n):
    if not root :
        return False
    if root.data == n:
        return True 
    else:
        return Search(root.left, n) or Search(root.right, n)
def BuildTree(Preorder, Inorder):
    dic = dict(zip(Inorder, range(len(Inorder))))
    len_pre = len(Preorder)
    return Build(Preorder, Inorder, len_pre, 0, 0, 0)

def Build(Preorder, Inorder, pre_len, pre_index, i, j):
    if pre_index >= pre_len or i >= j:
        return 
    x =  Preorder[pre_index]
    In_index = dic[x]
    pre_left = pre_index + 1
    pre_right = pre_index + max(0, In_index - 1) + 1
    n= node(x)
    n.left = build(Preorder,Inorder, pre_len, pre_left, i, In_index - 1)
    n.right = build(Preorder, Inorder, pre_len, In_index +1, j)
    return n 



preorder = [3,9,20,15,7] 
inorder = [9,3,15,20,7]
x= BuildTree(preorder, inorder)
print(x.data)


