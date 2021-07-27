from BinaryTreeFull import node, show
import heapq
from math import * 

class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None 

def FindDistance(root, p, q):
	if not root : raise ValueError 
	def Lca(root, p, q):
		if not root : return 
		if root.data in (p, q) : return root
		left, right = 0, 0 
		if root.left:
			left = Lca(root.left, p, q)
		if root.right:
			right = Lca(root.right, p, q)
		return root if left and right else left or right

	def dist(root, p, lvl):
		if not root : return - 1
		if root.data == p : return lvl 
		left = dist(root.left, p, lvl + 1)
		if left != - 1: return left 
		left = dist(root.right, p, lvl + 1)
		return left 

	lca = Lca(root, p, q)
	left = dist(lca, p, 0)
	right = dist(lca, q, 0)
	return left + right



root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12) # 12 
root.left.right.left = node(10)
root.left.right.right = node(14) # 14 
root.right = node(22)
root.right.right = node(25)
print(FindDistance(root, 8, 14))


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
