class node:
	def __init__(self,data):
		self.data=data
		self.left=self.right=None 
def push(root,data):
	if root==None:
		return node(data)
	else:
		if root.data<data:
			root.right=push(root.right,data)
		elif root.data>data:
			root.left=push(root.left,data)
		return root
def show(root):
	if root:
		show(root.left)
		print(root.data)
		show(root.right)
	else:
		return 
def height(root):
	if root==None:
		return 0 
	else:
		l=height(root.left)
		r=height(root.right)
		if l<r:
			return r+1
		else:
			return l+1

root=node(10)
push(root,20)
push(root,30)
push(root,5)
push(root,6)
push(root,4)
print(height(root))