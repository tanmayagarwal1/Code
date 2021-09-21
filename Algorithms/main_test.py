class node:
	def __init__(self, data):
		self.data = data 
		self.left = self.right = None 

def insert(root, data):
	if not root : return node(data)
	else:
		if root.data < data:
			root.right = insert(root.right, data)
		elif root.data > data : 
			root.left = insert(root.left, data)
		return root 

def show(root):
	if not root : return 
	show(root.left)
	print(root.data)
	show(root.right)

def adder(root):
	if not root : return 0 
	return root.data + adder(root.left) + adder(root.right)

def countLeafs(root):
	if not root : return 0 
	if not root.left and not root.right : return 1 
	return countLeafs(root.left) + countLeafs(root.right)

def delete(root, data):
	if root.left:
		root.left = delete(root.left, data)
	if root.right:
		root.right = delete(root.right, data)
	else:
		if root.data == data:
			return None 
	return root 

def search(root, target):
	if not root : return False 
	if root.data == target : return True 
	return search(root.left, target) or search(root.right, target)

def MaxSumSubtree(root):
	def Helper(root, res):
		if not root : return 0 
		curr = root.data + Helper(root.left, res) + Helper(root.right, res)
		res[0] = max(res[0], curr)
		return curr 
	if not root : raise ValueError 
	res = [-99999]
	Helper(root, res)
	return res[0]

def Height(root):
	if not root : return 0 
	l = Height(root.left)
	r = Height(root.right)
	return max(l, r) + 1 

def width(root):
	if not root : raise ValueError 
	q = [root]
	res = 0 
	while q:
		tmp = 0 
		for _ in range(len(q)):
			x = q.pop(0)
			tmp += 1
			if x.left : q.append(x.left)
			if x.right : q.append(x.right)
		res = max(res, tmp)
	return res 

def diameter(root):
	def Helper(root):
		nonlocal res 
		if not root : return 0 
		l = Helper(root.left)
		r = Helper(root.right)
		res = max(res, l + r + 1)
		return max(l, r) + 1
	res = 0 
	if not root : raise ValueError 
	Helper(root)
	return res - 1

def LevelOrder(root):
	if not root : raise ValueError 
	q = [(root)]
	arr = []
	while q :
		tmp = []
		for _ in range(len(q)):
			x = q.pop()
			tmp.append(x.data)
			if x.right : q.insert(0, x.right)
			if x.left : q.insert(0, x.left)
		arr.append(tmp)
	return arr 

def ZigZag(root):
	if not root : raise ValueError 
	q = [(root)]
	res = []
	flag = True 
	while q :
		tmp = []
		if flag:
			for _ in range(len(q)):
				x = q.pop(0)
				tmp.append(x.data)
				if x.left : q.append(x.left)
				if x.right : q.append(x.right)
		else:
			for _ in range(len(q)):
				x = q.pop()
				tmp.append(x.data)
				if x.right : q.insert(0, x.right)
				if x.left : q.insert(0, x.left)
		res.append(tmp)
		flag = not flag 
	return res 

def SumLeftLeaves(root):
	if not root : return 0 
	if root.left and not root.left.left and not root.left.right:
		return root.left.data + SumLeftLeaves(root.right)
	return SumLeftLeaves(root.left) + SumLeftLeaves(root.right)

def SumRightLeaves(root):
	if not root : return 0 
	if root.right and not root.right.left and not root.right.right : return root.right.data + SumRightLeaves(root.left)
	return SumRightLeaves(root.right) + SumRightLeaves(root.left)

def Boundary(root):
	if not root : raise ValueError 
	def leafs(root):
		if root:
			leafs(root.left)
			if not root.left and not root.right : print(root.data)
			leafs(root.right)

	def Down(root):
		if root: 
			if root.left:
				print(root.data)
				Down(root.left)
			elif root.right:
				print(root.data)
				Down(root.right)
	def Up(root):
		if root:
			if root.right:
				Up(root.right)
				print(root.data)
			elif root.left:
				Up(root.left)
				print(root.data)
	print(root.data)
	Down(root.left)
	leafs(root.left)
	leafs(root.right)
	Down(root.right)

def VerticalPrint(root):
	def Helper(root, d, idx):
		if root:
			d[idx] = d.get(idx, []) + [root.data]
			Helper(root.left, d, idx - 1)
			Helper(root.right, d, idx + 1)

	if not root : raise ValueError 
	d, res= {}, []
	idx = 0 
	Helper(root, d, idx)
	for i in sorted(d.keys()):
		tmp = []
		for num in d[i]:
			tmp.append(num)
		res.append(tmp)
	return res 

def LeftView(root):
	def Helper(root, lvl):
		if not root : return 
		nonlocal res, max_lvl
		if lvl > max_lvl:
			max_lvl = lvl 
			res.append(root.data)
		Helper(root.left, lvl + 1)
		Helper(root.right, lvl + 1)

	if not root : raise ValueError 
	max_lvl = 0 
	res = []
	Helper(root, 1)
	return res 

def RightView(root):
	def Helper(root, lvl):
		nonlocal res, max 
		if not root : return 
		if lvl > max:
			max = lvl 
			res.append(root.data)
		Helper(root.right, lvl + 1)
		Helper(root.left, lvl + 1)

	if not root : raise ValueError 
	res = []
	max = 0 
	Helper(root, 1)
	return res 

def TopView(root):
	def Helper(root, lvl, depth, d):
		if root:
			if lvl not in d:
				d[lvl] = [root.data, depth]
			elif d[lvl][1] > depth:
				d[lvl] = [root.data, depth]
			Helper(root.left, lvl - 1, depth + 1, d)
			Helper(root.right, lvl + 1, depth + 1, d)

	if not root : raise ValueError 
	d = {}
	Helper(root, 0, 1, d)
	for i in sorted(d.keys()):
		print(d[i][0])

def BottomView(root):
	if not root : raise ValueError 
	def Helper(root, lvl, depth, d):
		if root : 
			if lvl not in d :
				d[lvl] = [root.data, depth]
			elif depth > d[lvl][1]:
				d[lvl] = [root.data, depth]
			Helper(root.left, lvl - 1, depth + 1, d)
			Helper(root.right, lvl + 1, depth + 1, d)

	d = {}
	Helper(root, 0, 1, d)
	for i in sorted(d.keys()):
		print(d[i][0])

def isSymmetric(root):
	def Helper(rootl, rootr):
		q = [(rootl, rootr)]
		while q:
			x, y = q.pop(0)
			if not x and not y : continue 
			if not x or not y  : return False 
			if x.data != y.data : return False 
			else:
				q.append((x.left, y.right))
				q.append((x.right, y.left))
		return True 


	if not root : raise ValueError 
	return Helper(root.left, root.right)

def isBst(root):
	def Helper(root, lower, upper):
		if not root : return True 
		if lower < root.data < upper :
			return Helper(root.left, lower, root.data) and Helper(root.right, root.data, upper)
		return False 

	if not root : raise ValueError 
	return Helper(root, float('-inf'), float('inf'))

def mergeTrees(t1, t2):
	if t1 and t2:
		root = node(t1.data + t2.data)
		root.left = mergeTrees(t1.left, t2.left)
		root.right = mergeTrees(t1.right, t2.right)
		return root 
	else:
		return t1 or t2 

def fromArray(arr, l, h):
	if h < l : return 
	if h >= l :
		mid = l + (h - l)//2
		root = node(arr[mid])
		root.left = fromArray(arr, l, mid - 1)
		root.right = fromArray(arr, mid + 1, h)
		return root 

def toArray(root):
	if not root : return []
	return toArray(root.left) + [root.data] + toArray(root.right)

def construct(root, arr):
	if not root : return 
	construct(root.left)
	root.data = arr.pop(0)
	construct(root.right)

def treeToBst(root):
	if not root : raise ValueError
	arr = toArray(root)
	arr.sort()
	construct(root, arr)

def BstToBalancedTree(root):
	if not root : raise ValueError
	arr = toArray(root)
	new_root = fromArray(arr, 0, len(arr) - 1)
	return new_root

def BstToMaxHeap(root, arr):
	def Helper(root):
		if not root : return 
		Helper(root.left, arr)
		Helper(root.right, arr)
		root.data = arr.pop(0)

	if not root : raise ValueError
	arr = toArray(root)
	Helper(root, arr)

def BstToMinHeap(root):
	def Helper(root, arr):
		if not root : return 
		root.data = arr.pop(0)
		Helper(root.left, arr)
		Height(root.right, arr)
	if not root : raise ValueError
	arr = toArray(root)
	Helper(root, arr)

def BstToDll(root):
	if not root : raise ValueError 
	class sol:
		def __init__(self):
			self.head = None 
			self.prev = None 

		def solve(root):
			self.solve(root.left)
			tmp = root
			if not self.head:
				self.head = tmp
			else:
				self.prev.right = tmp 
				tmp.left = self.prev
			self.prev = tmp 
			self.solve(root.right)
			return self.head 

	s = sol()
	return s.solve(root)

def KthLargest(root, k):
	def Helper(root):
		nonlocal res 
		if not root or res >= k : return 
		Helper(root.right)
		res += 1 
		if res == k : 
			print(root.data)
			return None 
		Helper(root.left)
	if not root : raise ValueError 
	res = 0 
	Helper(root)

def isBalanced(root):
	def Helper(root):
		if not root : return 0
		l = Helper(root.left)
		if l == -1 : return -1 
		r = Helper(root.right)
		if r == - 1 : return - 1
		if(abs(l - r) > 1) : return -1
		return max(l, r) + 1  

	if not root : raise ValueError
	return False if Helper(root) == -1 else True 

def greaterSumBst(root):
	def Helper(root):
		nonlocal res 
		if not root : return 
		Helper(root.right)
		root.data = res = root.data + res 
		Helper(root.left)

	if not root : raise ValueError 
	res = 0 
	Helper(root)

def Lca(root, p, q):
	if not root : return 
	if root.data in (p, q) : return root.data 
	l, r = 0, 0 
	if root.left:
		l = Lca(root.left, p, q)
	if root.right : 
		r = Lca(root.right, p, q)
	return root.data if l and r else l or r 

def LeftMostLeaf(root):
	def Helper(root, lvl, bool):
		nonlocal res, max_lvl
		if not root : return 
		if not root.left and not root.right and lvl > max_lvl and lvl % 2 != 0 and bool:
			max_lvl = lvl 
			res = root.data 
		Helper(root.left, lvl + 1, True)
		Helper(root.right, lvl + 1, False)
	if not root : raise ValueError 
	res = 0 
	max_lvl = 0
	Helper(root, 1, True)
	return res 

def DistanceBetweenNodes(root, p, q):
	def Lca(root, p, q):
		if not root : return 
		if root.data in (p, q) : return root 
		l, r = 0, 0 
		if root.left:
			l = Lca(root.left, p, q)
		if root.right:
			r = Lca(root.right, p, q)
		return root if l and r else l or r 

	def Helper(root, nd, dist):
		if not root : return -1 
		if root.data == nd : return dist 
		l, r = 0, 0
		if root.left:
			l = Helper(root.left, nd, dist + 1)
		if l != -1 and l > 0 : return l 
		if root.right:
			r = Helper(root.right, nd, dist + 1)
		return r 

	if not root : raise ValueError
	parent = Lca(root, p, q)
	dist1 = Helper(parent, p, 0)
	dist2 = Helper(parent, q, 0)
	return dist1 + dist2

def AllAncestors(root, target):
	def Helper(root, target):
		if not root : return 
		if root.data == target : return True 
		if (Helper(root.left, target) or Helper(root.right, target)):
			res.append(root.data)
			return True 
		return False 

	if not root : raise ValueError 
	res = []
	Helper(root, target)
	return res 

def KthAncestor(root, target, k):
	def Helper(root, target):
		nonlocal res, lvl
		if not root : return 0 
		if root.data == target : return True 
		if Helper(root.left, target) or Helper(root.right, target):
			if lvl > 0 : lvl -= 1 
			elif lvl == 0 : 
				res = root.data 
				return None 
			return root 

	if not root : raise ValueError 
	lvl = k 
	res = 0 
	Helper(root, target)
	return res 

def MaxRootToLEafPath(root):
	def Helper(root, summ):
		nonlocal res 
		if not root : return  
		if not root.left and not root.right and summ + root.data > res :
			res = summ + root.data 
		Helper(root.left, summ + root.data)
		Helper(root.right, summ + root.data)
	if not root : raise ValueError 
	res = 0 
	Helper(root, 0)
	return res 

def doesExistSequence(root, arr):
	def Helper(root, arr, idx):
		if not root : return 
		if idx >= len(arr) or arr[idx] != root.data : return False 
		if not root.left and not root.right and idx == len(arr) - 1:
			return True 
		return Helper(root.left, arr, idx + 1) or Helper(root.right, arr, idx + 1)
	if not root : raise ValueError 
	return Helper(root, arr, 0)

def AllPathsToRoot(root):
	if not root : return ''
	if not root.left and not root.right:
		return [str(root.data)]
	paths = []
	l = AllPathsToRoot(root.left)
	r = AllPathsToRoot(root.right)
	for i in l :
		paths.append(str(root.data) + '->' + i)
	for i in r :
		paths.append(str(root.data) + '->' + i)
	return paths

def NodesAtDistanceK(root, k):
	def Helper(root, curr):
		nonlocal res, needed
		if not root  : return 
		if curr == k : res.append(root.data)
		Helper(root.left, curr + 1)
		Helper(root.right, curr + 1)

	if not root : raise ValueError 
	needed = k 
	res = []
	Helper(root, 0)
	return res 

def BuildTreePreorder(ino, pre):
	def Helper(ino, pre):
		if ino:
			val = pre.pop(0)
			idx = ino.index(val)
			root = node(ino[idx])
			root.left = Helper(ino[:idx], pre)
			root.right = Helper(ino[idx + 1], pre)
			return root 

	if not ino or not pre : raise ValueError 
	return Helper(ino, pre)

def UniValue(root):
	def Helper(rut):
		return not rut or rut.data == root.data and Helper(rut.left) and Helper(rut.right)
	if not root : raise ValueError 
	return Helper(root)

def UniValuePath(root):
	def Helper(root):
		nonlocal res 
		if not root : return 0 
		l = Helper(root.left)
		r = Helper(root.right)
		l = l + 1 if root.left and root.left.data == root.data else 0 
		r = r + 1 if root.right and root.right.data == root.data else 0 
		res = max(res, l + r)
		return max(l, r)

	if not root : raise ValueError
	res = 0 
	Helper(root)
	return res 

def CounPathsEqualToTarget(root, target):
	def Helper(root, d, prefix):
		nonlocal count 
		if not root : return 0 
		prefix += root.data 
		if prefix - target in d:
			count += d[prefix - target]
		d[prefix] = d.get(prefix, 0) + 1 
		Helper(root.left, d, prefix)
		Helper(root.right, d, prefix)
		d[prefix] -= 1

	if not root : raise ValueError
	d = {0 : 1}
	count = 0 
	Helper(root, d, 0)
	return count


def BuildTreePost(ino, post):
	def Helper(ino, post):
		if ino:
			val = post.pop()
			idx = ino.index(val)
			root = node(val)
			root.rigth = Helper(ino[idx + 1 :], post)
			root.left = Helper(ino[:idx], post)
			return root 

	if not ino or not post : raise ValueError 
	return Helper(ino, post)

def TrimBst(root, l, h):
	def Helper(root, l, h):
		if not root : return 
		if root.data > h : 
			return Helper(root.left, l, h)
		elif root.data < l : 
			return Helper(root.right, l, h)
		else:
			root.left = Helper(root.left, l, h)
			root.right = Helper(root.right, l, h)
		return root 

	if not root : raise ValueError 
	return Helper(root, l, h)

def BstPruning(root):
	def Helper(root):
		if not root : return 
		Helper(root.left)
		Helper(root.right)
		if not root.left and not root.right and not root.data : return None 
		return root 

	if not root : raise ValueError 
	return Helper(root)

def AllPathsEquaToTarget(root, target):
	def Helper(root, target, path):
		if not root : return 
		nonlocal res 
		path.append(root.data)
		Helper(root.left, target, path)
		Helper(root.right, target, path)
		Sum = 0 
		for i in range(len(path) - 1, -1, -1):
			Sum += path[i]
			if Sum == target : 
				print(path)
		path.pop()

	if not root : raise ValueError 
	res = []
	Helper(root, target, [])

def invert(root):
    if not root : return 
    root.left, root.right = root.right, root.left 
    invert(root.left)
    invert(root.right)

def Main():
	root = node(20)
	root.left = node(8)
	root.left.left = node(4)
	root.left.right = node(12)
	root.left.right.left = node(10)
	root.left.right.right = node(14)
	root.right = node(22)
	root.right.right = node(25)
	invert(root)
	print(LevelOrder(root))
	



if __name__ == '__main__':
    Main()

# root :      20
#            /  \
#           8   22
#          / \    \ 
#         4  12   25
#           /  \
#          10  14



