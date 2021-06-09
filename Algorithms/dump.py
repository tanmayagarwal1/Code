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
			root.left  = push(root.left, data)
		return root 

def show(root):
	if root:
		show(root.left)
		print(root.data)
		show(root.right)
	else:
		return 

def leafs(root):
	if not root:
		return 0 
	if not root.left and not root.right:
		return 1 
	else:
		return leafs(root.left) + leafs(root.right)

def sum(root):
	if not root:
		return 0 
	else:
		return root.data + sum(root.left) + sum(root.right)

def search(root, data):
	if not root:
		return False 
	if root.data == data:
		return True
	else:
		return search(root.left) or search(root.right)

def delete(root, data):
	if root.left:
		root.left = delete(root.left, data)
	if root.right:
		root.right = delete(root.right, data)
	if root.data == data:
		return None
	return root

def height(root):
	if not root:
		return 0
	else:
		l = height(root.left)
		r = height(root.right)
		if l < r:
			return r + 1
		else:
			return l + 1

def subtree(root):
	if not root:
		return 0 
	else:
		res = [-99999]
		subtreeu(root, res)
		return res[0]

def subtreeu(root, res):
	if not root:
		return 0 
	else:
		cur = root.data + subtreeu(root.left, res) + subtreeu(root.right, res)
		res[0] = max(res[0], cur)
		return cur 

def levelorder(root):
	if not root:
		return 
	else:
		h = height(root)
		for i in range(h):
			levelorderu(root, i)

def levelorderu(root, l):
	if not root:
		return 
	if l == 0:
		print(root.data)
	else:
		levelorderu(root.left, l -1)
		levelorderu(root.right, l -1)

def kthanc(root, n, k):
	if not root:
		return 
	if root.data == n or kthanc(root.left, n, k) or kthanc(root.right, n, k):
		if k[0] > 0:
			k[0] -= 1
		elif k[0] == 0:
			print(root.data)
			return None 
		return root

def IsSymmetric(root):
	return IsMirror(root.left, root.right)

def IsMirror(rootl, rootr):
	q = [(rootl, rootr)]
	while q:
		x, y = q.pop(0)
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

def IsValid(root):
	return IsBst(root, float('-inf'), float('inf'))

def IsBst(root, lower, upper):
	if not root:
		return True 
	else:
		if lower < root.data < upper:
			return IsBst(root.left, lower, root.data) and IsBst(root.right, root.data, upper)
		return True 

def Pathsum(root, data):
	if not root:
		return False
	if not root.left and not root.right and root.data == data:
		return True 
	else:
		return Pathsum(root.left, data - root.data) or Pathsum(root.right, data - root.data)

def Paths(root):
	if not root:
		return ''
	if not root.left and not root.right :
		return [str(root.data)]
	path = []
	l = Paths(root.left)
	r = Paths(root.right)
	for i in l:
		path.append(str(root.data) + '->' + i)
	for i in r:
		path.append(str(root.data) + '->' + i)
	return path 

def PathsToSum(root, target):
	if not root:
		return 
	res = []
	dfs(root, target, [], res)
	return res

def dfs(root, target, path, res):
	if not root:
		return 
	if not root.left and not root.right and root.data == target:
		path.append(root.data)
		res.append(path)
	else:
		dfs(root.left, target - root.data, path +[root.data], res)
		dfs(root.right, target - root.data, path +[root.data], res)

class solution:
	def __init__(self):
		self.max = 0 

	def LeftView(self, root):
		if not root:
			return 
		self.LeftViewDfs(root, 1)
		self.max = 0

	def LeftViewDfs(self, root, level):
		if not root:
			return 
		if level > self.max:
			print(root.data)
			self.max = level 
		self.LeftViewDfs(root.left, level + 1)
		self.LeftViewDfs(root.right, level + 1)

	def RightView(self, root):
		if not root:
			return 
		self.RightViewDfs(root, 1)
		self.max = 0 

	def RightViewDfs(self, root, level):
		if not root:
			return 
		if self.max < level :
			print(root.data)
			self.max = level
		self.RightViewDfs(root.right, level + 1)
		self.RightViewDfs(root.left, level + 1)

def SumLeftLEaves(root):
	if not root:
		return 0 
	if root.left and not root.left.left and not root.left.right:
		return root.left.data + SumLeftLEaves(root.right)
	else:
		return SumLeftLEaves(root.left) + SumLeftLEaves(root.right)

def BalanceBinaryTree(root):
	if not root:
		return 
	sol = Inorder(root)
	return Balancer(root, sol, 0, len(sol) - 1)

def Inorder(root):
	if root:
		return Inorder(root.left) + [root.data] + Inorder(root.right)
	else:
		return []

def Balancer(root, sol, l, h):
	if l > h : return None 
	mid = (l + h)//2
	root = node(sol[mid])
	root.left, root.right = Balancer(root, sol, l, mid - 1), Balancer(root, sol, mid + 1, h)
	return root

def SumRightLeaves(root):
	if not root:
		return 0 
	if root.right and not root.right.left and not root.right.right:
		return root.right.data + SumRightLeaves(root.left)
	else:
		return SumRightLeaves(root.right) + SumRightLeaves(root.left)

root=node(5)
push(root,10)
push(root,15)
push(root,6)
push(root,8)
push(root,1)
my_root = BalanceBinaryTree(root)
show(my_root)



