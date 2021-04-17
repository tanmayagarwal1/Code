class node:
	def __init__(self,data):
		self.data=data
		self.next
	def append(self,data):
		if self.head==None:
			self.head=node(data)
		else:
			temp=self.head
			nn=node(data)
			while temp.next != None:
				temp=temp.next 
			temp.next=nn
			nn.next=None
	def show(self):
		temp=self.head 
		while temp!=None:
			print(temp.data)
			temp=temp.next 
	def remdup(self):
		head=self.head 
		while head.next != None:
			temp=head.next 
			pre=temp
			while temp != None:
				if temp.data==head.data:
					pre.next=temp.next 
					temp=temp.next
					pre=temp 
				else:
					pre=temp 
					temp=temp.next
			head=head.next 
	def oddeve(self):
		head=self.head 
		n=self.len()
		temp=head.next 
		pre=temp 
		while temp.next !=None:
			head.next=temp.next 
			head=temp
			temp=temp.next 
		if n%2==0:
			head.next=pre 
			temp.next=None
		else:
			temp.next=pre
			head.next=None
	
