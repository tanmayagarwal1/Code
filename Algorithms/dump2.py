from BinaryTreeFull import node, show
import heapq
from math import * 

class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None 

def PathSum(root, target):
	if not root : raise ValueError 
	res = 0 
	def Helper(root, d, Sum):
		nonlocal res 
		if not root : return 0 
		Sum = Sum + root.data 
		old_sum = Sum - target
		res += d.get(old_sum, 0)
		d[Sum] = d.get(Sum, 0) + 1
		Helper(root.left, d, Sum)
		Helper(root.right, d, Sum)
		d[Sum] -= 1
	d = { 0 : 1 }
	Helper(root, d, 0)
	return res 







root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)
print(PathSum(root, 34))

# root :      20
#            /  \
#           8   22
#          / \    \ 
#         4  12   25
#           /  \
#          10  14


