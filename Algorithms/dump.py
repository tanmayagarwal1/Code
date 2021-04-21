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
			temp=self.head 
			n=node(data)
			while temp.next != None:
				temp=temp.next 
			temp.next=n
			n.next=None
	def view(self):
		temp=self.head 
		while temp != None:
			print(temp.data)
			temp=temp.next 
	def len(self):
		count =0 
		temp=self.head 
		while temp != None:
			count+=1
			temp=temp.next
		return count 
	def ispal(self):
		second=fast=slow=pre=self.head 
		midnode=None
		while self.head != None and self.head.next != None:
			while fast!=None and fast.next != None:
				fast=fast.next.next 
				pre=slow 
				slow=slow.next 
			if fast != None:
				midnode=slow 
				slow=slow.next 
			pre.next=None
			second=slow 
			second=self.rev(second)
			res=self.compare(self.head,second)
			second=self.rev(second)
			if midnode !=None:
				midnode.next = second 
				pre.next=midnode
			else:
				pre.next=second
			return res 
	def rev(self,second):
		temp=second 
		pre=ne=None
		while temp!=None:
			ne=temp.next 
			temp.next=pre 
			pre=temp
			temp=ne 
		second=pre 
		return second
	def compare(self,head1,head2):
		while head1 and head2:
			if head1.data==head2.data:
				head1=head1.next 
				head2=head2.next 
			else:
				return False 
		if head1==None and head2==None:
			return True 
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
			temp.next=pre 
			head.next=None
	def dups(self):
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

l=ll()
l.append(1)
l.append(2)
l.append(1)
l.append(4)
l.append(5)
l.append(6)
l.dups()
l.view()