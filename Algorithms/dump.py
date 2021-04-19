def ini(self,data):
	self.data=data
	self.left=self.right=None
node=type('node',(),{'__init__':ini})

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
def sum(root):
	if root==None:
		return 0 
	else:
		return root.data+sum(root.left)+sum(root.right)
def leaf(root):
	if root==None:
		return 0 
	if root.left==None and root.right==None:
		return 1 
	else:
		return leaf(root.left)+leaf(root.right)
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
def subtree(root):
	if root==None:
		return 0 
	else:
		res=[-99999]
		subtreeu(root,res)
		return res[0] 
def subtreeu(root,res):
	if root==None:
		return 0 
	else:
		curr=root.data+subtreeu(root.left,res)+subtreeu(root.right,res)
		res[0]=max(res[0],curr)
		return curr
def levelorder(root):
	if root==None:
		return 
	else:
		h=height(root)
		for i in range(h):
			levelorderu(root,i)
def levelorderu(root,l):
	if root ==None:
		return 
	if l==0:
		print(root.data)
	else:
		levelorderu(root.left,l-1)
		levelorderu(root.right,l-1)
def invert(root):
	if root:
		root.left,root.right=root.right,root.left
		invert(root.left)
		invert(root.right)
	else:
		return 
root=node(10)
push(root,5)
push(root,6)
push(root,7)
push(root,15)
push(root,14)
push(root,20)
push(root,21)
levelorder(root)
