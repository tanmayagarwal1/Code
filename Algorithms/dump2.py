from BinaryTreeFull import node, show
import heapq


def KthSmallest(root, k):
	class sol:
		def solver(self, root, k):
			def Helper(root):
				if root:
					Helper(root.left)
					if self.k == 0 : 
						print(root.data)
						return 
					elif self.k < 0 : return 
					else: self.k -= 1
					Helper(root.right)
				else:
					return 

			self.k = k 
			return Helper(root)
	s = sol()
	s.solver(root, k)
	return None 



root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)
#print(deepestLeftLeaf(root))
print(KthSmallest(root, 2))

# root :      20
#            /  \
#           8   22
#          / \    \ 
#         4  12   25
#           /  \
#          10  14