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
    return res - 1

def VerticalPrint(root):
    def Helper(root, d, idx):
        if root : 
            if idx in d:
                d[idx].append(root.data)
            else:
                d[idx] = [root.data]
            Helper(root.left, d, idx - 1)
            Helper(root.right, d, idx + 1)
        else:
            return 

    if not root : return 
    d = dict()
    idx = 0 
    Helper(root, d, idx)
    for i in sorted(d.keys()):
        res = []
        for num in d[i]:
            res.append(num)
        print(res)

def GreaterSumBst(root):
    class sol:
        def __init__(self):
            self.val = 0 
        def Helper(self, root):
            if root:
                self.Helper(root.right)
                root.data = self.val = self.val + root.data
                self.Helper(root.left)
                return root 
            else:
                return 0
    s = sol()
    s.Helper(root)
    return 

def LowestCommonAncestor(root, p, q):
    if root in (None, p, q) : return root 
    lef_res, right_res = 0, 0 
    if root.left:
        lef_res = LowestCommonAncestor(root.left, p, q)
    if root.right:
        right_res = LowestCommonAncestor(root.right, p, q)
    if lef_res and right_res:
        return root 
    return left_res or right_res

def PermsToGetSameBinaryTree(arr):
    if not arr : raise ValueError 
    def Fact(fac,  n):
        fac[0] = 1 
        for i in range(1, n):
            fac[i] = fac[i - 1] * i 

    def NcR(fac, n, r):
        if r > n : return 0 
        res = fac[n] // fac[r]
        res //= fac[n - r]
        return res 

    def Helper(arr, fac):
        n = len(arr)
        if n <= 2 : return 1 
        left_tree, right_tree = [], []
        root = arr[0]
        for i in range(1, n):
            if arr[i] > root:
                right_tree.append(arr[i])
            elif arr[i] < root:
                left_tree.append(arr[i])
        n1 = len(left_tree)
        n2 = len(right_tree)
        left_count = Helper(left_tree, fac)
        right_count = Helper(right_tree, fac)
        return (NcR(fac, n - 1, n1) * left_count * right_count)

    n = len(arr)
    fac = [0]*len(arr)
    Fact(fac, n)
    return Helper(arr, fac)

def Median(root, p, q):
    def Helper(root, sol):
        if root:
            Helper(root.left, sol)
            if root.data >= p and root.data <= q:
                sol.append(root.data)
            Helper(root.right, sol)
        else:
            return 
    def MedianHelper(arr):
        n = len(arr)
        idx = (n - 1)//2
        if n & 1 : return arr[idx]
        else: return (arr[idx] + arr[idx + 1])//2

    if not root : return 
    sol = []
    Helper(root, sol)
    return MedianHelper(sol)

# From this problem we define the iterators : Forwards and backwards iterators 
# Forwards iterators iterate to left initially and bakcwards to right 
# in the main while loop to move the iterator, forward iterator goes to right of the last element and recurses to the left 
# Backwards iterator goes to left of last node and recurses to the right again
# Problem that can be solved using this : Number of pairs equal target, Is pair equal target, Is pair in two trees equal target, triplets equal to target
# minimum absolute differnece between nodes of two trees 
def NumberOfNodesEqualSum(root, target):
    if not root : return 
    q  = [] # Forward iterator
    pq = [] # Backward iterator
    tmp = root 
    while tmp:  # Forward iterator goes left 
        q.append(tmp)
        tmp = tmp.left
    tmp = root 
    while tmp: # Backwards iterator goes right
        pq.append(tmp)
        tmp = tmp.right 
    count = 0 
    while q[-1] != pq[-1]: # condition to terminate 
        v1 = q[-1].data
        v2 = pq[-1].data 
        if v1 + v2 == target :
            count += 1
        if v1 + v2 <= target :
            tmp = q[-1].right # Increment forward iterator : first go right on the last node and the recurse left 
            q.pop()
            while tmp:
                q.append(tmp)
                tmp = tmp.left
        else:
            tmp = pq[-1].left # Increment the backwards iterator : Go left on the last node and then go right 
            pq.pop()
            while tmp:
                pq.append(tmp)
                tmp = tmp.right 
    return count 

def BoundaryTraversalClockwise(root):
    if not root : return 

    def Leafs(root):
        if root:
            Leafs(root.right)
            if not root.left and not root.right:
                print(root.data)
            Leafs(root.left)
        else:
            return None 

    def Down(root):
        if root:
            if root.right:
                print(root.data)
                Down(root.right)
            elif root.left:
                print(root.data)
                Down(root.left)
        else:
            return None 

    def Up(root):
        if root:
            if root.left:
                Up(root.left)
                print(root.data)
            elif root.right:
                Up(root.right)
                print(root.data)
        else:
            return None 

    print(root.data)
    Down(root.right)
    Leafs(root.right)
    Leafs(root.left)
    Up(root.left)
    return None 

def AntiBoundary(root): # This one with auxillary space 
    if not root : return None 
    res = []

    def Leafs(root, res):
        if root:
            Leafs(root.left, res)
            if not root.left and not root.right:
                res.append(root.data)
            Leafs(root.right, res)
        else:
            return None 

    def Down(root, res):
        if root:
            if root.left:
                res.append(root.data)
                Down(root.left, res)
            elif root.right:
                res.append(root.data)
                Down(root.right, res)
        else:
            return 

    def Up(root, res):
        if root:
            if root.right:
                Up(root.right, res)
                res.append(root.data)
            elif root.left:
                Up(root.left, res)
                res.append(root.data)
        else:
            return 

    res.append(root.data)
    Down(root.left, res)
    Leafs(root.left, res)
    Leafs(root.right, res)
    Up(root.right, res )
    return res 

def AdvancedZigZag(root):
    if not root : return 
    q, pq = [root], [root]
    res1, res2 = [], []
    while q and pq:
        tmp1, tmp2 = [], []
        le1, le2 = len(q), len(pq)
        while le1 and le2:
            le1 -= 1
            le2 -= 1
            x, y = q.pop(0), pq.pop()
            tmp1.append(x.data)
            tmp2.append(y.data)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
            if y.right:
                pq.insert(0, y.right)
            if y.left:
                pq.insert(0, y.left)
        res1.append(tmp1)
        res2.append(tmp2)

    #return res1, res2
    i = 0 
    j = len(res1) - 1
    while i < j:
        print(res1[i])
        print(res2[j])
        i += 1
        j -= 1
    return None 

def LeafSum(root):
    if not root : return 0 
    if not root.left and not root.right : return root.data 
    return LeafSum(root.left) + LeafSum(root.right)

def IsBalanced(root):
    if not root : return 0 
    if not root.left and not root.right : return 1 
    l = IsBalanced(root.left)
    if l == - 1: return -1 
    r = IsBalanced(root.right)
    if r == -1 : return - 1
    if (abs(l - r) > 1):
        return -1 
    return max(l, r) + 1

def ShowAllAncestors(root, target):
    res = []
    if not root : return None 
    def Helper(root, res, target):
        if not root : return False 
        if root.data == target :
            return True
        if(Helper(root.left, res, target) or Helper(root.right, res, target)):
            res.append(root.data)
            return True 
        return False 
    Helper(root, res, target)
    return res  

def GetParent(root, target):
    if not root : return False 
    if root.left and root.left.data == target or root.right and root.right.data == target:
        return root.data 
    return GetParent(root.left, target) or GetParent(root.right, target)

def GetSibling(root, target):
    def Helper(root, target):
        if not root : return False 
        if root.left and root.left.data == target:
            return root.right.data if root.right else False 
        elif root.right and root.right.data == target:
            return root.left.data if root.left else False 
        return Helper(root.left, target) or Helper(root.right, target)

    if not root : raise ValueError  
    if root.data == target : return None 
    return Helper(root, target)

def isSiblings(root, p, q):
    if not root : return False 
    if root.left and root.right:
        if root.left.data == p and root.right.data == q : return True
        if root.left.data == q and root.right.data == p : return True
    return isSiblings(root.left, p, q) or isSiblings(root.right, p, q)

def DistanceBetweenTwoNodes(root, node1, node2):
    def Helper(root, target, lev): # Finds the distance 
        if not root : return -1 
        if root.data == target : return lev
        tmp = Helper(root.left, target, lev + 1)
        if tmp != -1 : return tmp # If found on left return dist 
        tmp = Helper(root.right, target, lev + 1) # Else search on right 
        return tmp  

    def Lca(root, p, q):  # This, instead of returung node of the lca, returns its data 
        if not root : return None 
        if root.data in (p, q) : return root.data
        left_res, right_res = 0, 0
        if root.left:
            left_res = Lca(root.left, p, q)
        if root.right:
            right_res = Lca(root.right, p, q)
        if left_res and right_res : 
            return root.data 
        return left_res or right_res 

    def Getnode(root, num): # This takes that data and returns the node 
        if not root : return 
        if root.data == num:
            return root 
        return Getnode(root.left, num) or Getnode(root.right, num)

    lca =  Getnode(root, Lca(root, node1, node2))
    d1 = Helper(lca, node1, 0)
    d2 = Helper(lca, node2, 0)
    return d1 + d2 


def MaxPAthCostFromRootToLeaf(root):
    class sol : 
        def __init__(self):
            self.max = 0 
        def Helper(self, root, summ):
            if not root : return  
            if not root.left and not root.right and summ + root.data > self.max:
                self.max = summ + root.data
                return 
            self.Helper(root.left, summ + root.data)
            self.Helper(root.right, summ + root.data)
    s = sol()
    s.Helper(root, 0)
    return s.max


def RemoveAllNodesIfSumLessThanK(root, k):
    if not root : return 
    def Helper(root, k, s):
        if not root : return 0 
        Helper(root.left, k, s + root.data)
        Helper(root.right, k, s + root.data)
        if not root.left and not root.right and s + root.data < k:
            return None 

    Helper(root, k, 0)
    return 

def CheckIfSequenceInRootToPath(root, arr):
    if not arr or not root : raise ValueError
    def Helper(root, arr, idx):
        if not root : return False 
        if idx >= len(arr) or root.data != arr[idx]:
            return False 
        if not root.left and not root.right and idx == len(arr) - 1:
            return True 
        return Helper(root.left, arr, idx + 1) or Helper(root.right, arr, idx + 1)

    return Helper(root, arr, 0)


def DeepestLevelWithLeaf(root):
    # the level must be odd 
    class sol:
        def __init__(self):
            self.max = 0 

        def solver(self, root):
            def Helper(root, level):
                if not root : return 
                if not root.left and not root.right and level > self.max and level & 1:
                    self.max = level 
                Helper(root.left, level + 1)
                Helper(root.right, level + 1)

            Helper(root, 1)

    if not root : raise ValueError 
    s = sol()
    s.solver(root)
    return s.max


def DeepestLeftLeaf(root):
    if not root :
        raise ValueError 

    class sol:
        def __init__(self):
            self.max = 0 
            self.res = 0

        def solver(self, root):
            def Helper(root, level, isLeft):
                if not root : return 
                if not root.left and not root.right and level > self.max and isLeft:
                    self.res = root.data 
                    self.max = level 
                Helper(root.left, level + 1, True)
                Helper(root.right, level + 1, False)
            Helper(root, 1, True)

    s = sol()
    s.solver(root)
    return s.res 

def NodesAtDistanceKFromRoot(root, k):
    class sol:
        def Solver(self, root, k):
            self.k = k 
            if not root : raise ValueError
            def Helper(root, lvl):
                if not root : return 
                if lvl == self.k:
                    print(root.data)
                    return 
                Helper(root.left, lvl + 1)
                Helper(root.right, lvl + 1)
            Helper(root, 0)

    s = sol()
    s.Solver(root, k)
    return None 


def Difference(root):
    # Find the difference between even and odd level nodes 
    class sol:
        def __init__(self):
            self.even = 0 
            self.odd = 0 

        def Solver(self, root):
            if not root : raise ValueError
            def Helper(root, level):
                if not root : return 
                if not level & 1 : self.even += root.data
                else: self.odd += root.data 
                Helper(root.left, level + 1)
                Helper(root.right, level + 1)
            Helper(root, 1)

    s = sol()
    s.Solver(root)
    return abs(s.even - s.odd)


def BuildTreePostorder(inorder, postorder):
    if not inorder or not postorder : raise ValueError 
    def Helper(ino, post):
        if ino:
            x = post.pop()
            root = node(x)
            idx = ino.index(x)

            # As we build the tree from postorder, start building right to left 
            root.right = Helper(ino[idx + 1 : ], post)
            root.left = Helper(ino[:idx], post)
            return root 
    return Helper(inorder, postorder)


def BuildTreePreOrder(inorder, preorder):
    if not preorder or not inorder : raise ValueError
    def Helper(pre, ino):
        if ino:
            x = pre.pop(0)
            idx = ino.index(x)
            root = node(x)

            # Build normally from the left 
            root.left = Helper(pre, ino[:idx])
            root.right = Helper(pre, ino[idx + 1 :])
            return root 
    return Helper(preorder, inorder)




'''

root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)
print(DeepestLevelWithLeaf(root))

'''

# root :      20
#            /  \
#           8   22
#          / \    \ 
#         4  12   25
#           /  \
#          10  14






