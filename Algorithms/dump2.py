from BinaryTreeFull import node, show
import heapq
from math import * 

class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None 

def HeapSort(arr):
	def Helper(arr, n, i):
		large = i 
		l = 2 * i + 1
		r = 2 * i + 2
		if l < n and arr[large] < arr[l]:
			large = l 
		if r < n and arr[large] < arr[r]:
			large = r 
		if large != i:
			arr[large], arr[i] = arr[i], arr[large]
			Helper(arr, n, large)

	if not arr : raise ValueError 
	for i in range(len(arr) - 1//2, -1, -1):
		Helper(arr, len(arr), i)
	for i in range(len(arr) - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		Helper(arr, i, 0)
	return arr

arr = [32, 43, 21, 13, 76, 1, 1, 3]
print(HeapSort(arr))



root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12) # 12 
root.left.right.left = node(10)
root.left.right.right = node(14) # 14 
root.right = node(22)
root.right.right = node(25)
#print(KthLargestBst(root, 1))

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
