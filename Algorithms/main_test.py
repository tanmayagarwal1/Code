class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

class dll:
	def __init__(self):
		self.head = self.tail = None

	def construct(self, root):
		if root : 
			self.construct(root.left)
			node = root
			if not self.head : self.head = node 
			else: 
				self.tail.right = node 
				node.left = self.tail 
			self.tail = node
			self.construct(root.right)
			return self.head 
		else: return 

class sol:
	def __init__(self):
		self.max_level = 0 
		self.arr = []

	def LeftView(self, root):
		if not root : return 
		self.dfsLeft(root, 1)
		self.max_level = 0
		return self.arr

	def dfsLeft(self, root, level):
		if not root : return 
		if self.max_level < level:
			self.arr.append(root.data)
			self.max_level = level 
		self.dfsLeft(root.left, level + 1)
		self.dfsLeft(root.right, level + 1)

	def RightView(self, root):
		if not root : return 
		self.dfsRight(root, 1)
		self.max_level = 0
		return self.arr

	def dfsRight(self, root, level):
		if not root : return 
		if self.max_level < level:
			self.arr.append(root.data)
			self.max_level = level 
		self.dfsRight(root.right, level + 1)
		self.dfsRight(root.left, level + 1)

def push(root, data):
	if not root: return node(data)
	if root.data < data  : root.right = push(root.right, data)
	elif root.data > data: root.left = push(root.left, data)
	return root 

def show(root):
	if root:
		show(root.left)
		print(root.data)
		show(root.right)
	else : return 

def adder(root):
	if not root: return 0 
	return root.data + adder(root.left) + adder(root.right)

def leafs(root):
	if not root : return 0 
	if not root.left and not root.right : return 1 
	return leafs(root.left) + leafs(root.right)

def delete(root, data):
	if root.left : delete(root.left, data)
	if root.right : delete(root.right, data)
	else:
		if root.data == data:
			return None 
	return root

def search(root, data):
	if not root : return False 
	if root.data < data : search(root.right, data)
	if root.data > data : search(root.left, data)
	return True 

def subtree(root):
	if not root : return 0 
	res = [-9999]
	subtreeu(root, res)
	return res[0]

def subtreeu(root, res):
	if not root : return 0 
	cur = root.data + subtreeu(root.left, res) + subtreeu(root.right, res)
	res[0] = max(res[0], cur)
	return cur 

def height(root):
	if not root: return 0 
	l = height(root.left)
	r = height(root.right)
	if l < r : return r + 1
	else: return l + 1

def width(root):
	if not root : return 0 
	h = height(root)
	count = [0]*h
	widthHelper(root, count, 0)
	return max(count)

def widthHelper(root, arr, idx):
	if root :
		arr[idx] += 1
		widthHelper(root.left, arr, idx + 1)
		widthHelper(root.right, arr, idx + 1)
	else : return 

def levelorder(root):
	if not root : return 0 
	q, arr= [root], []
	while q:
		node = q.pop(0)
		arr.append(node.data)
		if node.left  : q.append(node.left)
		if node.right : q.append(node.right)
	return arr

def kthanc(root, n, k):
	if not root : return 
	if root.data == n or kthanc(root.left, n, k) or kthanc(root.right, n, k):
		if k[0] > 0 : k[0] -= 1
		elif k[0] == 0 :
			print(root.data)
			return None 
		return root 

def clock(root):
	if not root : return -1 
	q, arr, Mode = [root], [], False
	while q:
		tmp = len(q)
		if not Mode:
			while tmp > 0 :
				tmp -= 1
				node = q.pop(0)
				arr.append(node.data)
				if node.left  : q.append(node.left)
				if node.right : q.append(node.right)
		else:
			while tmp > 0:
				tmp -= 1
				node = q.pop()
				arr.append(node.data)
				if node.right : q.insert(0, node.right)
				if node.left  : q.insert(0, node.left)
		Mode = not Mode 
	return arr 

def counterclock(root):
	if not root : return - 1
	q, arr, Mode = [root], [], True
	while q:
		tmp = len(q)
		if not Mode:
			while tmp > 0 :
				tmp -= 1
				node = q.pop(0)
				arr.append(node.data)
				if node.left  : q.append(node.left)
				if node.right : q.append(node.right)
		else:
			while tmp > 0:
				tmp -= 1
				node = q.pop()
				arr.append(node.data)
				if node.right : q.insert(0, node.right)
				if node.left  : q.insert(0, node.left)
		Mode = not Mode
	return arr 

def sumLeftLeaves(root):
	if not root : return 0 
	if root.left and not root.left.left and not root.left.right : return root.data + sumLeftLeaves(root.right)
	return sumLeftLeaves(root.left) + sumLeftLeaves(root.right)

def sumRightLeaves(root):
	if not root : return 0 
	if root.right and not root.right.right and not root.right.left : return root.data + sumRightLeaves(root.left)
	return sumRightLeaves(root.right) + sumRightLeaves(root.left)

def pathToTarget(root, target):
	if not root : return False 
	if not root.left and not root.right and root.data == target : return True 
	return pathToTarget(root.left, target - root.data) or pathToTarget(root.right, target - root.data)

def Paths(root):
	if not root : return ''
	if not root.left and not root.right : return [str(root.data)]
	path = []
	l = Paths(root.left)
	r = Paths(root.right)
	for i in l : path.append(str(root.data) + '->' + i)
	for i in r : path.append(str(root.data) + '->' + i)
	return path 

def showPathToTarget(root, target):
	if not root : return 0 
	res = []
	showPathToTargetHelper(root, target, [], res)
	return res 

def showPathToTargetHelper(root, target, path, res):
	if not root : return 
	if not root.left and not root.right and root.data == target:
		path.append(root.data)
		res.append(path)
	else:
		showPathToTargetHelper(root.left, target - root.data, path + [root.data], res)
		showPathToTargetHelper(root.right, target - root.data, path + [root.data], res)

def IsSymmetric(root):
	return IsMirror(root.left, root.right)

def IsMirror(rootl, rootr):
	q = [(rootl, rootr)]
	while q:
		x, y = q.pop(0)
		if not x and not y : continue 
		if not x or not y : return False 
		if x.data != y.data : return False 
		q.append((x.left, y.right))
		q.append((x.right, y.left))
	return True

def IsValid(root):
	return IsBst(root, float('-inf'), float('inf'))

def IsBst(root, lower, upper):
	if not root : return True
	if lower < root.data < upper : return IsBst(root.left, lower, root.data) and IsBst(root.right, root.data, upper) 
	return False 


# ---------------- Builders --------------------------

def arrayBST(arr):
	if not arr : return - 1
	return arrayBSTHelper(arr, 0, len(arr) - 1)

def arrayBSTHelper(arr, l, h):
	if h < l : return 
	if h >= l :
		mid = l + (h - l)//2
		root = node(arr[mid])
		root.left = arrayBSTHelper(arr, l, mid - 1)
		root.right = arrayBSTHelper(arr, mid + 1, h)
		return root 

def treeToBst(root):
	sol = Inorder(root)
	sol.sort()
	treeToBstHelper(root, sol)

def Inorder(root):
	if root : return Inorder(root.left) + [root.data] + Inorder(root.right)
	else: return []

def treeToBstHelper(root, arr):
	if root:
		treeToBstHelper(root.left)
		root.data = arr[0]
		arr.pop(0)
		treeToBstHelper(root.right)
	else: return 

def BstToBalanced(root):
	sol = Inorder(root)
	return balancer(root, sol, 0, len(sol) - 1)

def balancer(root, arr, l, h):
	if h < l : return 
	if h >= l :
		mid = l + (h - l)//2
		root = node(arr[mid])
		root.left = balancer(root, arr, l, mid - 1)
		root.right = balancer(root, arr, mid + 1, h)
		return root 

def BstToMaxHeap(root):
	sol = Inorder(root)
	return BstToMaxHeapHelper(root, sol)

def BstToMaxHeapHelper(root, arr):
	if root:
		BstToMaxHeapHelper(root.left, arr)
		BstToMaxHeapHelper(root.right, arr)
		root.data = arr[0]
		arr.pop(0)
	else: return 

def BstToMinHeap(root):
	sol = Inorder(root)
	return BstToMinHeapHelper(root, sol)

def BstToMinHeapHelper(root, arr):
	if root :
		root.data = arr[0]
		arr.pop(0)
		BstToMinHeapHelper(root.left, arr)
		BstToMinHeapHelper(root.right, arr)

def listToBst(head):
	if not head : return 
	if not head.next : return node(head.data)
	slow, fast = head, head.next.next
	while fast != None and fast.next != None:
		slow = slow.next 
		fast = fast.next.next 
	tmp = slow.next 
	slow.next = None
	root = node(tmp.data)
	root.left = listToBst(head)
	root.right = listToBst(tmp.next)
	return root 

def levelorderList(root):
	if not root : return 
	q, arr = [root], []
	while q:
		tmp, tmp_arr = len(q), []
		while tmp > 0:
			tmp -= 1
			node = q.pop(0)
			tmp_arr.append(node.data)
			if node.left  : tmp_arr.append(node.left)
			if node.right : tmp_arr.append(node.right)
		arr.append(tmp_arr)
	return arr 

def toDll(root): # returns head 
	my_list = dll()
	return my_list.construct(root)

#------------------------------------------------------------------------------

def showMaxHeap(root):
	if root : return showMaxHeap(root.left) + showMaxHeap(root.right) + [root.data]
	else: return []

def showMinHeap(root):
	if root : return [root.data] + showMinHeap(root.left) + showMinHeap(root.right)
	else: return []

def showlist(head):
	if not head : return 
	while head.right:
		print(head.data)
		head = head.right 
	return 

def widthpro(root):
	if not root : return 
	q = [root]
	res = 0 
	while q :
		tmp, count = len(q), 0
		while tmp > 0:
			tmp -= 1
			node = q.pop(0)
			count += 1
			if node.left  : q.append(node.left)
			if node.right : q.append(node.right)
		res = max(res, count)
	return res 

#------------------------------------------------------------------------------

root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)
print(widthpro(root))






