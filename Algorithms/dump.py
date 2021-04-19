def ini(self,data):
	self.data=data
	self.next=None
node=type('node',(),{'__init__':ini})
def ini1(self):
	self.head=None
def append(self,data):
	if self.head==None:
		self.head=node(data)
	else:
		temp=self.head
		n=node(data)
		while temp.next!=None:
			temp=temp.next 
		temp.next=n 
		n.next=None
def view(self):
	temp=self.head 
	while temp!=None:
		print(temp.data)
		temp=temp.next 
def lent(self):
	count=0 
	temp=self.head 
	while temp != None:
		count+=1
		temp=temp.next 
	return count 

def adder(self,other):
	x=ll()
	k=self.lent()
	l=other.lent()
	if k<l:
		temp1=self.head
		temp2=other.head 
	else:
		temp1=other.head
		temp2=self.head 
	while  temp1 != None:
		x.append(temp1.data+temp2.data)
		temp1=temp1.next
		temp2=temp2.next
	while temp2 != None:
		x.append(temp2.data)
		temp2=temp2.next
	return x 
ll=type('ll',(),{'__init__':ini1,'append':append,'view':view,'lent':lent,'__add__':adder})
l=ll()
l.append(1)
l.append(2)
l.append(3)
l.append(4)

y=ll()
y.append(1)
y.append(1)
y.append(1)
y.append(1)
y.append(6)

z=l+y
z.view()


