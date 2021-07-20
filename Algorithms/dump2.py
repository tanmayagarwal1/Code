from BinaryTreeFull import node, show
import heapq
from math import * 

class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None 


def MergeKSortedLists(arr):
	ll.__lt__ : lambda self, other : self.data < other.data 
	ll.__eq__ : lambda self, other : self.data == other.data 
	if not arr : raise ValueError 
	pq = []
	for node in arr:
		if node:
			heapq.heappush(pq, (node.val, node))
	dummy = root = node(0)
	while pq:
		node = heapq.heapop(pq)[1]
		root.next = node
		root = root.next 
		if node.next:
			heapq.heappush(pq, (node.next.val, node.next))
	return dummy.next 

def Addnumbers(head1, head2):
	if not head1 or not head2 : raise ValueError
	dummy = root = node(0)
	carry = 0 
	while head1 or head2 or carry:
		if head1:
			carry += head1.data 
			head1 = head1.next 
		if head2:
			carry += head2.data 
			head2 = head2.next 
		root.next = node(carry % 10)
		root = root.next 
		carry //= 10 

	return dummy.next 

def CopyList(head):
	if not head : raise ValueError 
	curr = head 
	while curr:
		tmp = curr.next 
		curr.next = node(curr.data)
		curr.next.next = tmp 
		curr = tmp 

	curr = head 
	while curr:
		if curr.random:
			curr.next.random = curr.random.next 
		curr = curr.next.next 

	final = curr = head.next 
	while curr.next:
		head.next = curr.next 
		head = head.next 
		curr.next = head.next 
		curr = curr.next 
	head.next = None 
	return final 




root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12) # 12 
root.left.right.left = node(10)
root.left.right.right = node(14) # 14 
root.right = node(22)
root.right.right = node(25)
print(MaxLeafPath(root))

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
