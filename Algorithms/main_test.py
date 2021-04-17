class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class ll:
	def __init__(self):
		self.head=None 
	def append(self,data):
		if self.head==None:
			self.head=node(data)
		else:
			nn=node(data)
			temp=self.head 
			while temp.next != None:
				temp=temp.next
			temp.next=nn
			nn.next=None
	def view(self):
		temp=self.head 
		while temp != None:
			print(temp.data)
			temp=temp.next 
	def len(self):
		count=0 
		temp=self.head 
		while temp != None:
			count+=1
			temp=temp.next 
		return count 
	def remdup(self):
		head=self.head 
		while head.next!=None:
			temp=head.next 
			pre=head 
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
		temp=head.next 
		pre=temp 
		n=self.len()
		while temp.next != None:
			head.next=temp.next 
			head=temp 
			temp=temp.next 
		if n%2==0:
			head.next=pre 
			temp.next=None
		else:
			head.next=None
			temp.next=pre 
l=ll()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(10)
l.append(60)
l.remdup()
l.view()

