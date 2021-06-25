class node:
	def __init__(self, data):
		self.data = data 
		self.left = self.right = None 

class builder:
	def __init__(self):
		pass 
	@staticmethod
	def Inorder(root):
		if root :
			return builder.Inorder(root.left) + [root.data] + builder.Inorder(root.right)
		else:
			return []

	@staticmethod
	def Incopy(root, arr):
		if root : 
			builder.Incopy(root.left, arr)
			root.data = arr[0]
			arr.pop(0)
			builder.Incopy(root.right, arr)
		else:
			return 

	@staticmethod
	def build(arr, l, h):
		if h < l : return 
		if h >= l :
			mid = l + (h  - l)//2
			root = node(arr[mid])
			root.left = builder.build(arr, l, mid - 1)
			root.right = builder.build(arr, mid + 1, h)
			return root 

class Dll:
	def __init__(self):
		self.head = self.tail = None 

	@staticmethod 
	def convert(root):
		if root:
			convert(root.left)
			tmp = root 
			if not self.head:
				self.head = tmp 
			else:
				self.tail.right = tmp 
				tmp.left = self.tail 
			self.tail = tmp 

			convert(root.right)
			return self.head 

	@staticmethod
	def showlist(head):
		if not head : return 
		while head != None:
			print(head.data)
			head = head.right 

def push(root, data):
	if not root : return node(data)
	else:
		if root.data < data:
			root.right = push(root.right, data)
			root.left = push(root.left, data)
			return root 

def show(root):
	if root:
		show(root.left)
		print(root.data)
		show(root.right)
	else:
		return 

def add(root):
	if not root : return 0 
	return root.data + add(root.left) + add(root.right)

def leaf(root):
	if not root : return 0 
	if not root.left and not root.right : return 1 
	return leaf(root.left) + leaf(root.right)

def height(root):
	if not root : return 0 
	l = height(root.left)
	r = height(root.right)
	if l < r : return r + 1
	else: return l + 1

def levelorder(root):
	if not root : return 
	q = [root]
	while q :
		node = q.pop(0)
		print(node.data)
		if node.left : q.append(node.left)
		if node.right: q.append(node.right)
	return 

def width(root):
	if not root : return 
	q = [root]
	count = []
	while q :
		tmp, cnt = len(q), 0 
		while tmp > 0:
			tmp -= 1
			cnt += 1
			node = q.pop(0)
			if node.left : q.append(node.left)
			if node.right : q.append(node.right)
		count.append(cnt)
	return max(count)

def subtree(root):
	def subtreeu(root, res):
		if not root : return 
		curr = root.data + subtreeu(root.left, res) + subtreeu(root.right, res)
		res[0] = max(res[0], curr)
		return curr 

	if not root : return 
	res = [-999999]
	subtreeu(root, res)
	return res[0]

def kthanc(root, n, k):
	if not root : return 
	if root.data == n or kthanc(root.left, n,k) or kthanc(root.right, n, k):
		if k[0] > 0 : k[0] -= 1
		elif k[0] == 0:
			print(root.data)
			return None 
		return root 

def search(root, data):
	if not root : return False 
	if root.data < data : search(root.right, data)
	if root.data > data : search(root.left, data)
	return True 

def delete(root, target):
	if root.left:
		root.left = delete(root.left, target)
	if root.right:
		root.right = delete(root.right, target)
	if root.data == target:
		return None 
	return root 

def levelorderRightToLeft(root):
	if not root : return 
	q = [root]
	while q :
		node = q.pop()
		print(node.data)
		if node.right : q.insert(0, node.right)
		if node.left : q.insert(0, node.left)
	return 

def ZigZag(root):
	if not root : return 
	q = [root]
	Mode = True  # True = left to right 
	res = []
	while q:
		tmp = len(q)
		if Mode:
			while tmp > 0:
				tmp -= 1
				node = q.pop(0)
				res.append(node.data)
				if node.left : q.append(node.left)
				if node.right : q.append(node.right)
		else:
			while tmp > 0:
				node = q.pop()
				tmp -= 1
				res.append(node.data)
				if node.right : q.insert(0, node.right)
				if node.left  : q.insert(0, node.left)
		Mode = not Mode 
	return res 

def ZigZagAnti(root):
	if not root : return 
	q = [root]
	res = []
	Mode = False
	while q:
		tmp = len(q)
		if Mode:
			while tmp > 0 :
				tmp -= 1
				x = q.pop(0)
				res.append(x.data)
				if x.left : q.append(x.left)
				if x.right : q.append(x.right)
		else:
			while tmp > 0 :
				tmp -= 1
				y = q.pop()
				res.append(y.data)
				if y.right : q.insert(0, y.right)
				if y.left  : q.insert(0, y.left)
		Mode = not Mode 
	return res 


def SumLeftLeaves(root):
	if not root : return 0 
	if root.left and not root.left.left and not left.right.right : 
		return root.left.data + SumLeftLeaves(root.right)
	return SumLeftLeaves(root.left) + SumLeftLeaves(root.right)

def SumRightLeaves(root):
	if not root : return 0 
	if root.right and not root.right.left and not root.right.right:
		return root.right.data + SumRightLeaves(root.left)
	return SumRightLeaves(root.right) + SumRightLeaves(root.left)

def isPath(root, target):
	if not root : return False 
	if not root.left and not root.right and root.data == target:
		return True 
	return isPath(root.left, target - root.data) or isPath(root.right, target - root.data)

def ShowPath(root, target):

	def Helper(root, target, path, res):
		if not root : return 
		if not root.left and not root.right and root.data == target:
			path.append(root.data)
			res.append(path)
		Helper(root.left, target - root.data)
		Helper(root.right, target - root.data)

	if not root : return 
	res = []
	Helper(root, target, [], res)
	return res 

def Paths(root):
	if not root : return ''
	path = []
	if not root.left and not root.right : return [str(root.data)]
	l = Paths(root.left)
	r = Paths(root.right)
	for i in l : path.append(str(root.data) + '->' + i)
	for i in r : path.append(str(root.data) + '->' + i)
	return path 

def IsSymmetric(root):
	def Helper(rootl, rootr):
		q = [(rootl, rootr)]
		while q:
			x, y = q.pop(0)
			if not x and not y : continue 
			if not x or not y : return False 
			if x.data != y.data : return False 
			else:
				q.append((x.left, y.right))
				q.append((x.right, y.left))
			return True 
	return Helper(root.left, root.right)

def IsBst(root):
	def IsValid(root, lower, upper):
		if not root : return True 
		if lower < root.data < upper:
			return IsValid(root.left, lower, root.data) and IsValid(root.right, root.data, upper)
		return False 

	return IsValid(root, float('-inf'), float('inf'))

class sol:
	def __init__(self):
		self.max = 0 

	def LeftView(self, root):
		if not root : return 

		def dfs(root, level):
			if not root : return 
			if self.max < level:
				print(root.data)
				self.max = level 
			dfs(root.left, level + 1)
			dfs(root.right, level + 1)
			return None 

		dfs(root, 1)
		return None 

	def RightView(self, root):

		def dfs(root, level):
			if not root : return 
			if self.max < level:
				print(root.data)
				self.max = level 
			dfs(root.right, level + 1)
			dfs(root.left, level + 1)

		dfs(root, 1)
		return None 

def MergeTree(t1, t2):
	if t1 and t2:
		root = node(t1.data + t2.data)
		root.left = MergeTree(t1.left, t2.left)
		root.right = MergeTree(t1.right, t2.right)
		return root 
	else:
		return t1 or t2 

def Recover(root):
	if not root : return 
	sol = builder.Inorder(root) # Returns Inorder array 
	sol.sort() # sort the array 
	builder.Incopy(root, sol) # Copy the elements 

def ArrayToBst(arr):
	return builder.build(arr, 0, len(arr) - 1)

def TreeToBst(root):
	if not root : return 
	sol = builder.Inorder(root)
	sol.sort()
	builder.Incopy(root, sol)
	return None 

def BstToBalancedBst(root):
	if not root : return 
	sol = builder.Inorder(root)
	sol.sort()
	return builder.build(sol, 0, len(sol) - 1)

def BstToMaxHeap(root):
	if not root : return 
	sol = builder.Inorder(root)

	def build(root, sol):
		if root : 
			build(root.left, sol)
			build(root.right, sol)
			root.data = sol[0]
			sol.pop(0)
		else:
			return 	

	build(root, sol)
	return None 

def ShowHeap(root):
	if root:
		ShowHeap(root.left)
		ShowHeap(root.right)
		print(root.data)
	else:
		return 

def BstToMinHeap(root):
	sol = builder.Inorder(root)

	def build(root, sol):
		if root:
			root.data = sol[0]
			sol.pop(0)
			build(root.left, sol)
			build(root.right, sol)
		else:
			return 

	build(root, sol)
	return None 

def ShowMinHeap(root):
	if root:
		print(root.data)
		ShowMinHeap(root.left)
		ShowMinHeap(root.right)
	else:
		return 

def ListToBst(head):
	if not head : return 
	if not head.next : return node(head.data)
	slow, fast = head, head.next.next 
	while fast != None and fast.next != None:
		fast = fast.next.next 
		pre = slow 
		slow = slow.next 
	tmp = slow.next 
	slow.next = None 
	root = node(tmp.data)
	root.left = ListToBst(head)
	root.right = ListToBst(tmp.next)
	return root 

def ToDll(root):
	head = Dll.convert(root)
	Dll.showlist(head)
	return  

def Count(root):
	if not root : return 0 
	return Count(root.left) + Count(root.right) + 1 


root = node(10) 
root.left = node(12) 
root.right = node(13) 
root.right.left = node(14) 
root.right.right = node(15) 
root.right.left.left = node(21) 
root.right.left.right = node(22) 
root.right.right.left = node(23) 
root.right.right.right = node(24) 

root2 = node(15)
root2.left = node(10)
root2.right = node(20)
root2.left.left = node(8)
root2.left.right = node(12)
root2.right.left = node(16)
root2.right.right = node(25)

t1 = MergeTree(root, root2)
t1 = BstToBalancedBst(t1)
show(t1)







