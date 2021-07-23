from BinaryTreeFull import node, show
import heapq
from math import * 

class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None 


def isBalanced(root):
	if not root : raise ValueError 
	def Helper(root):
		if not root : return 0 
		l = Helper(root.left)
		if l == - 1 : return - 1
		r = Helper(root.right)
		if r == - 1: return -1 
		if abs(r - l) > 1: return - 1
		return max(r, l) + 1
	res = Helper(root)
	return True if res >= 0 else False 




root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12) # 12 
root.left.right.left = node(10)
root.left.right.right = node(14) # 14 
root.right = node(22)
root.right.right = node(25)
print(isBalanced(root))

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
