from BinaryTreeFull import node, show, RemoveAllNodesIfSumLessThanK
import heapq
from math import * 


array = [[0 for j in range(2)] for i in range(2)]
print(array)




root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)
#print(Difference(root))

# root :      20
#            /  \
#           8   22
#          / \    \ 
#         4  12   25
#           /  \
#          10  14


