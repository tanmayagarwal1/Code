from BinaryTreeFull import node, show
import heapq
from math import * 

def insert(root, data):
	if not root : 
		return node(data)
	else:
		if root.data < data:
			root.right = insert(root.right, data)
		elif root.data > data:
			root.left = insert(root.left, data)
		return root 

def show(root):
	if not root : return 
	show(root.left)
	print(root.data)
	show(root.right)

def delete(root, data):
	if not root : return 
	if root.left:
		root.left = delete(root.left, data)
	if root.right:
		root.right = delete(root.right, data)
	else:
		if root.data == data:
			return None 
		return root 

def adder(root):
	if not root : return 0 
	return root.data + adder(root.left) + adder(root.right)

def LeafCount(root):
	if not root : return 0 
	if not root.left and not root.right : return 1 
	return LeafCount(root.left) + LeafCount(root.right)

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

	if not root : return 0 
	res = [-9999]
	Helper(root, res)
	return res[0]

def Height(root):
	if not root : return 0 
	l = Height(root.left)
	r = Height(root.right)
	return max(l, r) + 1

def Diameter(root):
	def Helper(root):
		nonlocal res 
		if not root : return 0 
		l = Helper(root.left)
		r = Helper(root.right)
		res = max(res, l + r + 1)
		return max(r, l) + 1
	if not root : raise ValueError 
	res = 0 
	Helper(root)
	return res - 1


def LevelOrder(root):
	if not root : raise ValueError 
	q = [root]
	while q:
		x = q.pop(0)
		print(x.data)
		if x.left : q.append(x.left)
		if x.right : q.append(x.right)
	return 

def LevelOrderReverse(root):
	if not root : raise ValueError 
	q = [root]
	while q:
		x = q.pop()
		print(x.data)
		if x.right : q.insert(0, x.right)
		if x.left : q.insert(0, x.left)
	return 


def ZigZag(root):
	if not root : return 
	q = [root]
	bool = True 
	res = []
	while q :
		tmp_res = []
		if bool: 
			for _ in range(len(q)):
				x = q.pop(0)
				tmp_res.append(x.data)
				if x.left : q.append(x.left)
				if x.right : q.append(x.right)
		else:
			for _ in range(len(q)):
				x = q.pop()
				tmp_res.append(x.data)
				if x.right : q.insert(0, x.right)
				if x.left : q.insert(0, x.left)
		bool = not bool 
		res.append(tmp_res)
	return res 


def SumLeftLeaves(root):
	if not root : return 0 
	if root.left and not root.left.left and not root.left.right:
		return root.left.data + SumLeftLeaves(root.right)
	return SumLeftLeaves(root.left) + SumLeftLeaves(root.right)

def SumRightLeaves(root):
	if not root : return 0 
	if root.right and not root.right.left and not root.right.right:
		return root.righ.data + SumLeftLeaves(root.left)
	return SumRightLeaves(root.right) + SumRightLeaves(root.left)

def isPathSumToTarget(root, target):
	if not root : return 
	if not root.left and not root.right and root.data == target : 
		return True 
	return isPathSumToTarget(root, target - root.data) or isPathSumToTarget(root ,target - root.data)

def ReturnAllPathsToleaf(root, target):
	def Helper(root, target, path, res):
		if not root : return 
		if not root.left and not root.right and root.data == target:
			path.append(root.data)
			res.append(path)
		Helper(root.left, target - root.data, path + [root.data], res)
		Helper(root.right, target - root.data, path + [root.data], res)

	if not root : raise ValueError 
	res = []
	Helper(root, target, [], res)
	return res 

def AllPaths(root):
	if not root : return ''
	if not root.left and not root.right:
		return [str(root.data)]
	paths = []
	l = AllPaths(root.left)
	r = AllPaths(root.right)
	for i in l :
		paths.append(str(root.data) + '->' + i)
	for i in r :
		paths.append(str(root.data) + '->' + i)
	return paths

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
				q.append((x.right, q.left))
			return True 
	if not root : raise ValueError
	return Helper(root.left, root.right)

def IsBst(root):
	def Helper(root, lower, upper):
		if not root : return True
		if lower < root.data < upper:
			return Helper(root.left, lower, root.data) and Helper(root.right, root.data, upper) 
		return False 

	if not root : raise ValueError 
	return Helper(root, float('-inf'), float('inf'))

def LeftView(root):
	def Helper(root, lvl):
		if not root : return 
		nonlocal max_lvl, sol 
		if lvl > max_lvl:
			max_lvl = lvl 
			sol.append(root.data)
		Helper(root.left, lvl + 1)
		Helper(root.right, lvl + 1)
	if not root : raise ValueError
	sol = []
	max_lvl = 0 
	Helper(root, 1)
	return sol 

def RightView(root):
	def Helper(root, lvl):
		if not root : return 
		nonlocal sol, max_lvl
		if lvl > max_lvl:
			max_lvl = lvl 
			sol.append(root.data)
		Helper(root.right, lvl + 1)
		Helper(root.left, lvl + 1)
	if not root : raise ValueError
	sol = []
	max_lvl = 0 
	Helper(root, 1)
	return sol 

def MergeTree(root1, root2):
	if root1 and root2:
		root = node(root1.data + root2.data)
		root.left = MergeTree(root1.left, root2.left)
		root.right = MergeTree(root1.right, root2.right)
		return root 
	else:
		return root1 or root2

def Inorder(root):
	if not root : return []
	return Inorder(root.left) + [root.data] + Inorder(root.right)

def ReconstructTree(root):
	if not root : raise ValueError
	arr = Inorder(root)
	arr.sort()
	BuilderFromTraversal(root, arr)

def BuilderFromTraversal(root, arr):
	if not root : return 
	BuilderFromTraversal(root.left, arr)
	root.data = arr.pop()
	BuilderFromTraversal(root.right, arr)

def BuilderFromArray(arr, l, h):
	if h < l : return
	if h >= l :
		mid = l + (h - l)//2
		root = node(arr[mid])
		root.left = BuilderFromArray(arr, l, mid - 1)
		root.right = BuilderFromArray(arr, mid + 1, h)
		return root 

def SortedArrayToBst(arr):
	if not arr : raise ValueError 
	return BuilderFromArray(arr, 0, len(arr) - 1)

def LinkedListToBst(head):
	if not head : return 
	if not head.next : return node(head.data)
	slow, fast = head, head 
	while fast.next.next:
		fast = fast.next.next 
		prev = slow 
		slow = slow.next 
	prev.next = None 
	root = node(slow)
	root.left = LinkedListToBst(head)
	root.right = LinkedListToBst(slow.next)
	return root 

def TreeToBst(root):
	if not root : raise ValueError 
	arr = Inorder(root)
	arr.sort()
	BuilderFromTraversal(root, arr)

def BstToBalancedBst(root):
	if not root : raise ValueError
	sol = Inorder(root)
	sol.sort()
	return BuilderFromArray(sol)

def BstToMaxHeap(root):
	def Helper(root, arr):
		if not root : return 
		Helper(root.left)
		Helper(root.right)
		root.data = arr.pop(0)

	if not root : raise ValueError 
	arr = Inorder(root)
	Helper(root, arr)

def BstToMinHeap(root):
	def Helper(root, arr):
		if not arr : return 
		root.data = arr.pop(0)
		Helper(root.left, arr)
		Helper(root.right, arr)
	if not root : raise ValueError
	sol = Inorder(root)
	Helper(root, sol)

def BstToDll(root):
	if not root : raise ValueError 
	class list:
		def __init__(self):
			self.head = self.prev = None 

		def Build(self, root):
			if not root : return 
			self.Build(root.left)
			tmp = root.data 
			if not self.head:
				self.head = tmp 
			else:
				self.prev.right = tmp
				tmp.left = self.prev 
			self.prev = tmp 

			self.Build(root.right)
			return root 

	sol = list()
	return sol.Build(root)

def Kthanc(root, k, target):
	if not root : raise ValueError 
	k = k 
	def Helper(root, target):
		if not root : return 
		nonlocal k 
		if root.data == target or Helper(root.left, target) or Helper(root.right, target):
			if k > 0 : k -= 1
			elif k == 0 : 
				print(root.data)
				return None 
			return root 
	Helper(root, target)

def Countnode(root):
	if not root : return 0 
	return 1 + Countnode(root.left) + Countnode(root.right)

def VerticalPrint(root):
	def Helper(root, d, idx, lvl):
		if not root : return 
		if idx in d :
			d[idx].append(root.data)
		else:
			d[idx] = [root.data]
		Helper(root.left, d, idx - 1, lvl)
		Helper(root.right, d, idx + 1, lvl)
	if not root : raise ValueError 
	d, res = {}, []
	Helper(root, d, 1, 0)
	for key in sorted(d.keys()):
		res.append(d[key])
	return res 

def BstToGreaterBst(root):
	if not root : raise ValueError
	Sum = 0 
	def Helper(root):
		if not root : return 
		nonlocal Sum 
		Helper(root.right)
		root.data = Sum = root.data + Sum 
		Helper(root.left)
	Helper(root)

def Lca(root, p, q):
	if not root : return 
	if root.data in (p, q) : return root.data
	left, right = 0, 0 
	if root.left:
		left = Lca(root.left, p, q)
	if root.right:
		right = Lca(root.right, p, q)
	return root.data if left and right else left or right

def BoundaryTraversal(root):
	if not root : raise ValueError 
	def Leafs(root):
		if not root : return 
		Leafs(root.right)
		if not root.left and not root.right : print(root.data)
		Leafs(root.left)

	def Down(root):
		if root:
			if root.right:
				print(root.data)
				Down(root.right)
			elif root.left:
				print(root.data)
				Down(root.left)
		else:
			return 

	def Up(root):
		if root:
			if root.left:
				Up(root.left)
				print(root.data)
			elif root.right:
				Up(root.right)
				print(root.data)
		else:
			return 

	print(root.data)
	Down(root.right)
	Leafs(root.right)
	Leafs(root.left)
	Up(root.left)

def BoundaryReverse(root):
	if not root : raise ValueError 
	def Leafs(root):
		if not root : return 
		Leafs(root.left)
		if not root.left and not root.right : print(root.data)
		Leafs(root.right)

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
	Leafs(root.left)
	Leafs(root.right)
	Up(root.right)

# Iterators 

def PairEqualTarget(root, target):
	if not root : raise ValueError 
	fwd, rev = [], []
	tmp = root
	while tmp:
		fwd.append(tmp)
		tmp = tmp.left 
	tmp = root 
	while tmp:
		rev.append(tmp)
		tmp = tmp.right

	while fwd[-1] != rev[-1]:
		val1 = fwd[-1].data
		val2 = rev[-1].data 
		if val1 + val2 == target:
			return True 
		elif val1 + val2 < target:
			tmp = fwd[-1].right
			fwd.pop()
			while tmp:
				fwd.append(tmp)
				tmp = tmp.left 
		else:
			tmp = rev[-1].left
			rev.pop()
			while tmp:
				rev.append(tmp)
				tmp = tmp.right
	return - 1

def Triplets(root, target):
	if not root : raise ValueError 
	def Helper(root, target):
		if not root : return 
		if PairEqualTarget(root, target - root.data) != -1 :
			return True 
		return Helper(root.left, target) or Helper(root.right, target)

	return Helper(root, target)

def SumLeafs(root):
	if not root : raise ValueError 
	Sum = 0 
	def Helper(root):
		if not root : return 
		nonlocal Sum 
		if not root.left and not root.right:
			Sum += root.data 
		Helper(root.left)
		Helper(root.right)

	Helper(root)
	return Sum 

def IsBalanced(root):
	if not root : raise ValueError 
	def Helper(root):
		if not root : return 0 
		l = Helper(root.left)
		if l == - 1 : return - 1
		r = Helper(root.right)
		if r == - 1 : return - 1
		if abs(l - r) > 1 : return - 1
		return max(l, r) + 1

	return True if Helper(root) != -1 else False 

def PrintAncestors(root, target):
	if not root : return 
	if root.data == target : return True 
	if PrintAncestors(root.left, target) or PrintAncestors(root.right, target):
		print(root.data)
		return True 
	return False 

def GetParent(root, target):
	if not root : return 
	if root.left and root.left.data == target : return root.data 
	if root.right and root.right.data == target : return root.data
	return GetParent(root.left, target) or GetParent(root.right, target)

def GetSibling(root, target):
	if not root : return 
	if root.left and root.left.data == target:
		if root.right : return root.right.data
	if root.right and root.right.data == target:
		if root.left : return root.left.data 
	return GetSibling(root.left, target) or GetSibling(root.right, target)

def checkIfSiblings(root, p, q):
	if not root : return 
	if root.left and root.right and ((root.left.data, root.right.data) == (p, q) \
	   or (root.left.data, root.right.data) == (q, p)): return True
	return checkIfSiblings(root.left, p, q) or checkIfSiblings(root.right, p, q)

def DistanceBetweenTwoNodes(root, p, q):
	if not root : raise ValueError 
	def lca(root, p, q):
		if not root : return 
		if root.data in (p, q) : return root
		left, right = 0, 0 
		if root.left : left = lca(root.left, p, q)
		if root.right : right = lca(root.right, p, q)
		return root if left and right else left or right

	def Helper(root, p, dist):
		if not root : return - 1
		if root.data == p : return dist 
		tmp = Helper(root.left, p, dist + 1)
		if tmp != -1 : return tmp 
		tmp = Helper(root.right, p, dist + 1)
		return tmp 

	Root = lca(root, p, q)
	d1 = Helper(Root, p, 0)
	d2 = Helper(Root, q, 0)
	return d1 + d2 

def MaxPathCostRootToLeaf(root):
	if not root : raise ValueError 
	Sum = 0 
	def Helper(root, sum):
		nonlocal Sum 
		if not root : return 
		if not root.left and not root.right and sum + root.data > Sum:
			Sum = sum + root.data 
		Helper(root.left, sum + root.data)
		Helper(root.right, sum + root.data)

	Helper(root, 0)
	return Sum 

def RemoveNodesIfLessThanTarget(root, target):
	if not root : raise ValueError 
	def Helper(root, sum):
		if not root : return 
		if root.left:
			root.left = Helper(root.left, sum + root.data)
		if root.right:
			root.right = Helper(root.right, sum + root.data)
		if not root.left and not root.right and sum + root.data > target:
			return None 
		return root 

	Helper(root, 0)
	return 

def checkSequence(root, arr):
	if not root : raise ValueError 
	def Helper(root, arr, idx):
		if not root : return 
		if idx >= len(arr) or arr[idx] != root.data : return False 
		if not root.left and not root.right and idx == len(arr) - 1 : return True 
		return Helper(root.left, arr, idx + 1) or Helper(root.right, arr, idx + 1)
	return Helper(root, arr, 0)

def DeepestOddLevelLeaf(root):
	if not root : raise ValueError 
	maxlvl = 0 
	res = 0 
	def Helper(root, lvl):
		if not root : return 
		nonlocal maxlvl, res
		if not root.left and not root.right and lvl > maxlvl and lvl % 2 != 0 :
			maxlvl = lvl 
			res = root.data 
		Helper(root.left, lvl + 1)
		Helper(root.right, lvl + 1)

	Helper(root, 1)
	return res


def DeepestLeftLeaf(root):
	if not root : raise ValueError 
	max = 0 
	res = 0 
	def Helper(root, lvl, bool):
		if not root : return 
		nonlocal max, res 
		if not root.left and not root.right and lvl > max and bool:
			max = lvl 
			res = root.data 
		Helper(root.left, lvl + 1, True)
		Helper(root.right, lvl + 1, False)

	Helper(root, 1, True)
	return max, res 


def DistanceKFromRoot(root, k):
	if not root : raise ValueError 
	def Helper(root, dist):
		if not root : return 
		if dist == k :
			print(root.data)
		Helper(root.left, dist + 1)
		Helper(root.right, dist + 1)

	Helper(root, 0)

def DifferenceOddAndEven(root):
	if not root : raise ValueError 
	odd = 0 
	even = 0 
	def Helper(root, lvl):
		if not root : return 
		nonlocal odd, even
		if lvl % 2 == 0 : even += root.data 
		else : odd += root.data 
		Helper(root.left, lvl + 1)
		Helper(root.right, lvl + 1)
	Helper(root, 0)
	return abs(odd - even)

def BuildFromPreOrder(ino, pre):
	if not ino or not pre : raise ValueError 
	def Helper(ino, pre):
		if ino :
			idx = ino.index(pre.pop(0))
			root = node(ino[idx])
			root.left = Helper(ino[:idx], pre)
			root.right = Helper(ino[idx + 1 :], pre)
			return root 

	return Helper(ino, pre)

def BuildFromPost(ino, post):
	if not ino or not post : raise ValueError 
	def Helper(ino, post):
		idx =  ino.index(post.pop())
		root = node(ino[idx])
		root.right = Helper(ino[idx + 1 :], post)
		root.left = Helper(ino[:idx], post)
		return root 

	return Helper(ino, post)

def KthLargest(root, k):
	if not root : raise ValueError 
	tmp = 0 
	def Helper(root, k):
		nonlocal tmp
		if not root : return 
		Helper(root.right, k)
		tmp += 1
		if tmp == k :
			print(root.data)
			return 
		Helper(root.left, k)

	Helper(root, k)

def IsUniValue(root):
	if not root : raise ValueError 
	def Helper(node):
		return not node or root.data == node.data and Helper(node.left) and Helper(node.right)
	return Helper(root)

def MaximumUniValuePath(root):
	if not root : raise ValueError 
	res = 0 
	def Helper(root):
		if not root : return 0
		nonlocal res 
		left = Helper(root.left)
		right = Helper(root.right)
		left = left + 1 if root.left and root.data == root.left.data else 0 
		right = right + 1 if root.right and root.data == root.right.data else 0 
		res = max(res, left + right)
		return max(left, right)
	Helper(root)
	return res 

def CountPathsToTarget(root, target):
	if not root : raise ValueError 
	def Helper(root, prefix, d):
		if not root : return 
		nonlocal count
		prefix += root.data 
		if prefix - target in d :
			count += d[prefix - target]
		d[prefix] = d.get(prefix, 0) + 1 
		Helper(root.left, prefix, d)
		Helper(root.right, prefix, d)
		d[prefix] -= 1

	d = {}
	count = 0 
	Helper(root, 0, d)
	return count 

def TopView(root):
	def Helper(root, d, idx, lvl):
		if not root : return 
		if idx in d :
			if lvl < d[idx][1]:
				d[idx] = [root.data, lvl]
		else:
			d[idx] = [root.data, lvl]
		Helper(root.left, d, idx - 1, lvl + 1)
		Helper(root.right, d, idx + 1, lvl + 1)
	if not root : raise ValueError 
	d = {}
	Helper(root, d, 0, 1)
	sol = []
	for key in sorted(d.keys()):
		sol.append(d[key][0])
	return sol 

def BottomView(root):
	def Helper(root, d, idx, lvl):
		if not root : return 
		if idx in d :
			if lvl > d[idx][1]:
				d[idx] = [root.data, lvl]
		else:
			d[idx] = [root.data, lvl]
		Helper(root.left, d, idx - 1, lvl + 1)
		Helper(root.right, d, idx + 1, lvl + 1)

	if not root : raise ValueError 
	d = {}
	sol = []
	Helper(root, d, 0, 1)
	for key in sorted(d.keys()):
		sol.append(d[key][0])
	return sol 


def TrimBst(root, l, h):
	if not root : raise ValueError 
	def Helper(root, l, h):
		if not root : return 
		if root.data > h : 
			return Helper(root.left, l, h)
		if root.data < l : 
			return Helper(root.right, l, h)
		else:
			root.left = Helper(root.left, l, h)
			root.right = Helper(root.right, l, h)
		return root 

	return Helper(root, l, h)

def Pruning(root):
	if not root : raise ValueError
	def Helper(root):
		if not root : return 
		root.left = Helper(root.left)
		root.right = Helper(root.right)
		if not root.left and not root.right and not root.data : return None 
		return root 

	return Helper(root)

def LCA_BST(root, p, q):
	if not root : raise ValueError 
	def Helper(root, p, q):
		if not root : return 
		if p > root.data and q > root.data :
			return root.left 
		if p < root.data and q < root.data:
			return root.right 
		else:
			return root 

	return Helper(root, p, q)

def PrintAllPathsToTarget(root, target):
	if not root : raise ValueError
	def Helper(root, target, path):
		nonlocal res 
		if not root : return 
		path.append(root.data)
		Helper(root.left, target, path)
		Helper(root.right, target, path)
		Sum = 0 
		for i in range(len(path) - 1, -1, -1):
			if Sum == target:
				res.append(path)
		path.pop()

	Helper(root, target, [])
	res = []
	return res 

root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12) 
root.left.right.left = node(10)
root.left.right.right = node(14)  
root.right = node(22)
root.right.right = node(25)
print(BottomView(root))







# root :      20
#            /  \
#           8   22
#          / \    \ 
#         4  12   25
#           /  \
#          10  14