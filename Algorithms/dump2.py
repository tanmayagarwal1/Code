from BinaryTreeFull import node, show
import heapq
from math import * 

class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None 

def KthLagest(root, k):
	if not root : raise ValueError 
	c = [0]
	k = k 
	res = 0 
	def Helper(root, c):
		nonlocal k, res 
		if not root or c[0] >= k : return 
		Helper(root.right, c)
		c[0] += 1
		if c[0] == k:
			res = root.data 
			return 
		Helper(root.left, c)
	Helper(root, c)
	return res 
    




root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12) # 12 
root.left.right.left = node(10)
root.left.right.right = node(14) # 14 
root.right = node(22)
root.right.right = node(25)
print(KthLagest(root, 2))

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
