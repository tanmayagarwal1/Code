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
def view(root):
	if root:
		view(root.left)
		print(root.data)
		view(root.right)
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
def levelorder(root):
	if root==None:
		return 
	else:
		h=height(root)
		q=[]
		for i in range(h):
			levelorderu(root,i,q)
		return q 
def levelorderu(root,l,q):
	if root==None:
		return 
	if l==0:
		q.append(root.data)
	else:
		levelorderu(root.left,l-1,q)
		levelorderu(root.right,l-1,q)

class ll:
	def __init__(self):
		self.head=None
	def append(self,data):
		if self.head==None:
			self.head=node(data)
		else:
			temp=self.head
			n=node(data)
			while temp.right != None:
				temp=temp.right 
			temp.right=n
			n.left=temp 
			n.right=None
	def make(self,q):
		for i in q:
			self.append(i)
	def show(self):
		temp=self.head 
		while temp != None:
			print(temp.data)
			temp=temp.right


root=node(10)
push(root,11)
push(root,12)
push(root,9)
push(root,8)


l=ll()
l.make(x)
l.show()
