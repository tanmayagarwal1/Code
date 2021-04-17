class A:
  def __init__(self,num):
    self.num=num 

  def __gt__(self,other):
    if self.num>other.num:
      return True 
    else:
      return False 
  def __add__(self,other):
    return self.num + other.num 
  def __mul__(self,other):
    return self.num * other.num   

x=A(3)
y=A(4)
if x>y:
  print(f"{x.num} is greater than {y.num}")
else: 
  print(f"{y.num} is greater than {x.num}") 
print(x+y)  
print(x*y)      