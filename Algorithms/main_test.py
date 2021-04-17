def init(self,x,y):
	self.first=x 
	self.last=y
@property 
def email(self):
	return self.first+self.last+"@gmail.com"
@email.setter
def email(self,sti):
	x,y=sti.split('.')
	self.first=x
	self.last=y 
def stri(self):
	return """This class is a dynamic class and has the following properties : initialise 
with first and last name and then use email attribute which can also be used 
to set the name values with the . operator in middle"""

A=type('A',(),{'__init__':init,'email':email,'__str__':stri})
t=A("tanmay","Agarwal")
print(t)