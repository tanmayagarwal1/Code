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

def BuildTree(preorder, inorder, tree: node=None):
	if len(preorder) and preorder[0] in inorder:
		index=inorder.index(preorder[0])
		return index
		tree=node(data=inorder[index])
		tree.left= BuildTree(preorder[1:index+1], inorder[:index] )
		tree.right=BuildTree(preorder[index+1: ], inorder[index+1:])
	return tree 
def BuildTree2(inorder, postorder, tree: node=None):
	if len(postorder) and postorder[-1] in inorder:
		index=inorder.index(postorder[-1])
		return index
		tree=node(data=inorder[index])
		tree.left= BuildTree(postorder[-1:index-1:-1], inorder[:index] )
		tree.right=BuildTree(postorder[index-1:-1:-1 ], inorder[index+1:])
	return tree 


#postorder = [9,15,7,20,3] 
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(BuildTree2(postorder,inorder))


