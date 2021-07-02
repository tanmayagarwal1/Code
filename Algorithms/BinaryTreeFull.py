class node:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None 

def push(root, data):
    if not root:
        return node(data) 
    else:
        if root.data < data:
            root.right = push(root.right, data)
        elif root.data > data:
            root.left = push(root.left, data)
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
    if not root.left and not root.right :
        return 1 
    else:
        return Leaf(root.left) + Leaf(root.right)

def Count(root):
    if not root:
        return 0 
    else:
        return Count(root.left) + Count(root.right) + 1 

def Search(root, data):
    if not root:
        return False 
    if root.data == data:
        return True 
    else:
        return Search(root.left, data) or Search(root.right, data)

def Delete(root, data):
    if root.left :
        root.left = Delete(root.left, data)
    if root.right:
        root.right = Delete(root.right, data)
    else:
        if root.data == data:
            return None 
    return root

def height(root):
    if not root:
        return 0 
    else:
        l = height(root.left)
        r = height(root.right)
        if l < r :
            return r + 1
        else:
            return l + 1

def Levelorder(root):
    if not root:
        return 
    h = height(root)
    for i in range(h):
        LevelorderU(root, i)

def LevelorderU(root, l):
    if not root : return 
    if l == 0 : print(root.data)
    else:
        LevelorderU(root.left, l - 1)
        LevelorderU(root.right, l - 1)

def Subtree(root):
    if not root:
        return - 1
    res = [-9999]
    SubtreeU(root, res)
    return res[0]

def SubtreeU(root, res):
    if not root:
        return 0 
    cur = root.data + SubtreeU(root.left, res) + SubtreeU(root.right, res)
    res[0] = max(res[0], cur)
    return cur 

def kthanc(root, n, k):
    if not root : return 
    if root.data == n or kthanc(root.left, n, k) or kthanc(root.right, n, k):
        if k[0] > 0 :
            k[0] -= 1
        elif k[0] == 0:
            print(root.data)
            return None
        return root 

def IsSymmetric(root):
    return IsMirror(root.left, root.right)

def IsMirror(rootl, rootr):
    q = [(rootl, rootr)]
    while q :
        x, y = q.pop(0)
        if not x and not y :
            continue 
        if not x or not y :
            return False 
        if x.data != y.data:
            return False 
        else:
            q.append((x.left, y.right))
            q.append((x.right, y.left))
        return True 

def IsValid(root):
    return IsBST(root, float('-inf'), float('inf'))

def IsBST(root, lower, upper):
    if not root:
        return True
    else:
        if lower < root.data < upper :
            return IsBST(root.left, lower, root.data) and IsBST(root.right, root.data, upper)
        return False 

def ExistsPath(root, target):
    if not root:
        return False 
    if not root.left and not root.right and root.data == target:
        return True 
    else:
        return ExistsPath(root.left, target - root.data) or ExistsPath(root.right, target - root.data)

def PathSum(root, target):
    if not root : return 
    res = []
    PathSumHelper(root, target, [], res)
    return res 

def PathSumHelper(root, target, path, res):
    if not root : return 
    if not root.left and not root.right and root.data == target:
        path.append(root.data)
        res.append(path)
    else:
        PathSumHelper(root.left, target - root.data, path + [root.data], res)
        PathSumHelper(root.right, target - root.data, path + [root.data], res)

def Paths(root):
    if not root : return ''
    if not root.left and not root.right : return [str(root.data)]
    path = []
    l = Paths(root.left)
    r = Paths(root.right)
    [path.append(str(root.data) + '->' + i) for i in l]
    [path.append(str(root.data) + '->' + i) for i in r]
    return path 

def SumLeftLeaves(root):
    if not root : return 0 
    if root.left and not root.left.left and not root.left.right : return root.data + SumLeftLeaves(root.right)
    else:   return SumLeftLeaves(root.left) + SumLeftLeaves(root.right)

def SumRIghtLEaves(root):
    if not root : return 0
    if root.right and not root.right.left and not root.right.right : return root.data + SumRIghtLEaves(root.left)
    else: return SumRIghtLEaves(root.right) + SumRIghtLEaves(root.left)

class solution():
    def __init__(self):
        self.max_level = 0 

    def LeftView(self, root):
        if not root : return 
        self.dfs(root, 1)
        self.max_level = 0 
        return None

    def dfs(self, root, level):
        if not root :
            return 
        if self.max_level < level:
            print(root.data)
            self.max_level = level
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

    def RightLEaves(self, root):
        if not root : return  
        self.dfsRight(root, 1)
        self.max_level = 0 
        return None 

    def dfsRight(self, root, level):
        if not root : return 
        if self.max_level < level:
            print(root.data)
            self.max_level = level 
        self.dfsRight(root.right, level + 1)
        self.dfsRight(root.left, level + 1)

# Building Trees with different forms : 

def Inorder(root):
    if root : return Inorder(root.left) + [root.data] + Inorder(root.right)
    else: return []

def SortedListToBst(arr): # Returns a fresh root
    if not arr : return 
    return SortedListToBstBuilder(arr, 0, len(arr) - 1)

def SortedListToBstBuilder(arr, l, h):
    if h < l : return
    if h >= l :
        mid = (l + h)//2
        root = node(arr[mid])
        root.left = SortedListToBstBuilder(arr, l, mid - 1)
        root.right = SortedListToBstBuilder(arr, mid + 1, h)
        return root

def LinkedListToBst(head): # Returns a fresh root
    if not head : return 
    if not head.next : return node(head.data)
    slow, fast = head, head.next.next 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    tmp = slow.next 
    slow.next = None
    root = node(tmp.data)
    root.left = LinkedListToBst(head)
    root.right = LinkedListToBst(tmp.next)
    return root 

def NormalTreetoBst(root): # In Place
    if not root : return 
    arr = Inorder(root)
    arr.sort()
    NormalTreetoBstBuilder(root, arr)

def NormalTreetoBstBuilder(root, arr):
    if root : 
        NormalTreetoBstBuilder(root.left, arr)
        root.data = arr[0]
        arr.pop(0)
        NormalTreetoBstBuilder(root.right, arr)
    else:
        return 

def BstToBalancedBst(root): # Returns a root
    if not root : return 
    arr = Inorder(root)
    return BstToBalancedBstBalancer(root, arr, 0, len(arr) - 1)

def BstToBalancedBstBalancer(root, arr, l, h):
    if h < l : return 
    if h >= l :
        mid = (l + h)//2
        root = node(arr[mid])
        root.left = BstToBalancedBstBalancer(root, arr, l, mid - 1)
        root.right = BstToBalancedBstBalancer(root, arr, mid + 1, h)
        return root 

def BstToMaxHeap(root): # InPlace
    if not root : return 
    arr = Inorder(root)
    BstToMaxHeapBuilder(root, arr)

def BstToMaxHeapBuilder(root, arr):
    if root:
        BstToMaxHeapBuilder(root.left, arr)
        BstToMaxHeapBuilder(root.right, arr)
        root.data = arr[0]
        arr.pop(0)
    else:
        return 

def ShowHeap(root):
    if root : 
        return ShowHeap(root.left) + ShowHeap(root.right) + [root.data]
    else:
        return []

def TreeToDoublell(root): # Returns head of DLL
    if not root : return 
    sol = dll()
    return sol.convert(root)

class dll:
    def __init__(self):
        self.head = None
        self.tail = None 

    def convert(self, root):
        if root:
            self.convert(root.left)
            tmp = root 
            if not self.head:
                self.head = tmp 
            else:
                self.tail.right = tmp
                tmp.left = self.tail 
            self.tail = tmp 
            self.convert(root.right)
            return self.head 

def ShowList(head):
    if not head : return 
    while head : 
        print(head.data)
        head = head.right



def MergeTwoTree(t1, t2):
    if not t1 and not t2 : return 
    root = node((t1.data if t1 else 0) + (t2.data if t2 else 0))
    root.left = MergeTwoTree(t1 and t1.left, t2 and t2.left)
    root.right = MergeTwoTree(t1 and t1.right, t2 and t2.right)
    return root 
def Kthlargest(root, k, c):
    if not root or c[0] >= k : return 
    Kthlargest(root.right, k, c)
    c[0] += 1
    if c[0] == k:
        print(root.data)
        return None
    Kthlargest(root.left, k, c)

def IsOddEven(root):
    if not root : return 
    q = [root]
    count = 0 
    while q:    
        tmp = len(q)
        if count == 0 :
            while tmp > 0:
                tmp -= 1
                x = q.pop()
                if x.left : q.append(x.left)
                if x.right : q.append(x.right)

        elif count % 2: # ODD Case 
            temp = float('inf')
            while tmp > 0:
                tmp -= 1
                x = q.pop(0)
                if x.data % 2 == 1 : return False 
                if x.data < temp : temp = x.data 
                else: return False 
                if x.left : q.append(x.left)
                if x.right : q.append(x.right)
        elif count % 2 == 0:
            temp = float('-inf')
            while tmp > 0: # Even Case 
                tmp -= 1
                x = q.pop(0)
                if x.data % 2 == 0: return False 
                if x.data > temp : temp = x.data 
                else : return False 
                if x.left : q.append(x.left)
                if x.right : q.append(x.right)
        count += 1

    return True 

def diameter(root):
    res = 0 
    def Helper(root):
        if not root : return 0 
        l = Helper(root.left)
        r = Helper(root.right)
        res = max(res, l + r + 1)
        if l < r : return r + 1
        return l + 1

    Helper(root)
    return best - 1


root=node(5)
push(root,10)
push(root,15)
push(root,6)
push(root,8)
push(root,1)
Kthlargest(root, 2, [0])
#show(forest)
#print(Paths(forest))
IsBST






