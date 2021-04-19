def  ini(self,data):
	self.data=data
	self.next=None 
node=type("node",(),{'__init__':ini})

class ll:
	def __init__(self):
		self.head=None
	def append(self,data):
		if self.head==None:
			self.head=node(data)
		else:
			temp=self.head 
			nn=node(data)
			while temp.next!=None:
				temp=temp.next
			temp.next=nn
			nn.next=None
	def dele(self,n):
		count=0
		temp=self.head 
		while temp.next !=None and count<n-1:
			count+=1
			pre=temp
			temp=temp.next
		pre.next=temp.next 
		temp=temp.next 
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
		while head.next != None:
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
	def ispal(self):
		slow=fast=pre=second=self.head 
		midnode=None
		while self.head != None and self.head.next != None:
			while fast != None and fast.next != None:
				fast=fast.next.next 
				pre=slow 
				slow=slow.next 
			if fast != None:
				midnode=slow 
				slow=slow.next 
			pre.next=None
			second=slow 
			second=self.reve(second)
			res=self.compare(self.head,second)
			second=self.reve(second)
			if midnode != None:
				midnode.next=second 
				pre.next=midnode
			else:
				pre.next=second 
			return res 
	def reve(self,second):
		temp=second
		pre=ne=None
		while temp != None:
			ne=temp.next 
			temp.next=pre 
			pre=temp
			temp=ne 
		second=pre 
		return second 
	def compare(self,head,second):
		head1=head 
		head2=second
		while head1 and head2:
			if head1.data==head2.data:
				head1=head1.next 
				head2=head2.next 
			else:
				return False 
		if head1==None and head2==None:
			return True 
		return False 
l=ll()
l.append(1)
l.append(1)
l.append(1)
l.append(0)
l.append(0)
l.append(1)
l.append(1)
print(l.ispal())



