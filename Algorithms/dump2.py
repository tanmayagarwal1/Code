from BinaryTreeFull import node, show
import heapq
from math import * 

class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None 

def height(root):
	if not root : return 0 
	l = height(root.left)
	r = height(root.right)
	return max(l, r) + 1

def isBalanced(root):
	if not root : raise ValueError 
	def Helper(root):
		if not root : return 0
		l = Helper(root.left)
		if l == - 1: return - 1
		r = Helper(root.right)
		if r == - 1 : return - 1
		if abs(l - r) > 1 : return - 1
		return max(l, r) + 1
	return True if Helper(root) != -1 else False 

def LongestUniValuePath(root):
	if not root : raise ValueError 
	res = 0 
	def Helper(root):
		nonlocal res 
		if not root : return 0 
		l = Helper(root.left)
		r = Helper(root.right)
		l = l + 1 if root.left and root.left.data == root.data else 0
		r = r + 1 if root.right and root.right.data == root.data else 0
		res = max(res, r + l)
		return max(r, l)
	Helper(root)
	return res 


def FindTarget(root, target):
	if not root : raise ValueError 
	def Helper(root):
		if not root : return 
		fwd, rev = [], []
		tmp = root
		while tmp:
			fwd.append(root)
			tmp = tmp.left 
		tmp = root 
		while tmp:
			rev.append(tmp)
			tmp = tmp.right 

		while fwd[-1] != rev[-1]:
			val1 = fwd[-1].data 
			val2 = rev[-1].data 
			if val1 + val2 == target : return True 
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
		return -1 

	return Helper(root)


def delete(root, k):
	if not root : return 
	if root.left:
		root.left = delete(root.left, k)
	if root.right : 
		root.right = delete(root.right, k)
	else:
		if root.data == k :
			return None 
	return root 

def Pruning(root):
	# Remove trees not continaing 1's
	if not root : raise ValueError
	def Helper(root):
		if not root : return 
		if root.left : root.left = Helper(root.left)
		if root.right : root.right = Helper(root.right)
		if not root.left and not root.right and not root.data : return None 
		return root 

	return Helper(root)

def trimBst(root, l, h):
	if not root : raise ValueError
	def Helper(root, l, h):
		if not root : return 
		if root.data > h : return Helper(root.left, l, h)
		if root.data < l : return Helper(root.right, l, h)
		else:
			root.left = Helper(root.left, l, h)
			root.right = Helper(root.right, l, h)
		return root 

	return Helper(root, l, h)

def CountPathsToTarget(root, k):
	if not root : raise ValueError
	def Helper(root, d, prefix):
		nonlocal count 
		if not root : return  
		prefix += root.data 
		if prefix - k in d : count += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1
		Helper(root.left, d, prefix)
		Helper(root.right, d, prefix)
		d[prefix] -= 1

	count = 0 
	Helper(root, {0 : 1}, 0)
	return count 


def NodesAtDistanceKfromRoot(root, k):
	if not root : raise ValueError
	k = k 
	def Helper(root, count):
		nonlocal k, res 
		if not root : return 
		if count == k :
			res.append(root.data)
		Helper(root.left, count + 1)
		Helper(root.right, count + 1)
	res = []
	Helper(root, 0)
	return res 

def DeletePathsIfSumLessThank(root, k):
	if not root: raise ValueError 
	def Helper(root, Sum):
		if not root : return 
		if root.left : root.left = Helper(root.left, Sum + root.data)
		if root.right : root.right = Helper(root.right, Sum + root.data)
		if not root.left and not root.right and root.data + Sum > k:
			return None 
		return root 

	return Helper(root, 0)

def LcaBinaryTree(root, p, q):
	if root.data in (None, p, q) : return root.data 
	l, r = 0, 0 
	if root.left:
		l = LcaBinaryTree(root.left, p, q)
	if root.right:
		r = LcaBinaryTree(root.right, p, q)
	return root.data if p and q else p or q 

def LcaBst(root, p, q):
	if not root : raise ValueError
	def Helper(root, p, q):
		if not root : return 
		if p < root.data and q < root.data:
			return Helper(root.left, p, q)
		if p > root.data and q > root.data:
			return Helper(root.right, p, q)
		else:
			return root.data
	return Helper(root, p, q)


def DistanceBetweenNodes(root, p, q):
	if not root : raise ValueError 
	def lca(root, p, q):
		if not root : return None 
		if root.data in (p, q) : return root  
		l, r = 0, 0 
		if root.left:
			l = lca(root.left, p, q)
		if root.right:
			r = lca(root.right, p, q)
		return root if l and r else l or r 

	def Helper(root, lvl, node_):
		if not root : return -1 
		if root.data == node_ : return lvl 
		tmp = Helper(root.left, lvl + 1, node_)
		if tmp != -1 : return tmp 
		tmp = Helper(root.right, lvl + 1, node_)
		return tmp 

	Root = lca(root, p, q)
	d1 = Helper(Root, 0, p)
	d2 = Helper(Root, 0, q)
	return d1 + d2 


def FindAllPaths(root, k):
	if not root : raise ValueError 
	def Helper(root, path, k):
		if not root : return 
		path.append(root.data)
		Helper(root.left, path, k)
		Helper(root.right, path, k) 
		Sum = 0 
		for i in range(len(path) - 1, -1, -1):
			Sum += path[i]
			if Sum == k :
				print(path)
		path.pop()

	Helper(root, [], k)
	return 





root = node(1)
root.left = node(3)
root.left.left = node(2)
root.left.right = node(1)
root.left.right.left = node(1)
root.right = node(-1)
root.right.left = node(4)
root.right.left.left = node(1)
root.right.left.right = node(2)
root.right.right = node(5)
root.right.right.right = node(2)
FindAllPaths(root, 5)








#root = node(20)
#root.left = node(8)
#root.left.left = node(4)
#root.left.right = node(12) # 12 
#root.left.right.left = node(10)
#root.left.right.right = node(14) # 14 
#root.right = node(22)
#root.right.right = node(25)
#print(DistanceBetweenNodes(root, 8, 14))



# root :      20
#            /  \
#           8   22
#          / \    \ 
#         4  12   25
#           /  \
#          10  14


Root = node(1)
Root.left = node(2)
Root.right = node(3)
Root.left.right = node(4)
Root.left.right.right = node(5)
Root.left.right.right.right = node(6)
#print(TopView(Root))
