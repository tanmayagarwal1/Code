import csv 
import numpy
from collections import Counter 
from matplotlib import pyplot as plt 
plt.style.use('seaborn')
class plot:
	def __init__(self,x,y,color="yellow",linestyle='-',marker='.'):
		self.x=x
		self.y=y
		self.color=color 
		self.linestyle=linestyle
		self.marker=marker
	def plot(self):
		plt.plot(self.x,self.y,color=self.color,linestyle=self.linestyle)
		plt.tight_layout()
		plt.show()
	def __str__(self):
		return f"The order is x,y,color,linestyle"
	def splot(self):
		color=[]
		for i in self.x:
			color.append(numpy.random.randint(1,10))
		plt.scatter(self.x,self.y,c=color,marker=self.marker)
		plt.tight_layout 
		plt.show()
age=[]
bp=[]
with open(r"/Users/tanmay/Downloads/heart.csv",'r') as f:
	reader=csv.DictReader(f)
	for row in reader:
		age.append(row['age'])
		bp.append(row['trestbps'])
p=plot(age,bp,color="green")
p.splot()

