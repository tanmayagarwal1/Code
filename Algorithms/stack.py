class stack: 
    
    def __init__(self):
        self._size=5
        self.a=[None]*self._size
        self.i=0  

    def push(self,x):
        if(self.i<self._size):
            self.a[self.i]=x 
            self.i +=1
        else:
            print("full")

    def pop(self):
        if(self.i==0):
            print("empty")
        else:
            self.i=self.i-1
            self.a[self.i]=None
            

    def info(self):
        for y in range(self._size):
            print(self.a[y])
    def get_info(self):
        print(self._size)

    def __str__(self):
        return "This is the main stack of size {}".format(self._size)
        
            

class ds(stack):
    def __init__(self):
        stack.__init__(self)
    def get_info(self):
        print(self._size)
    def set_size(self,t):
        self._size=t
    def __str__(self):
        return "THis is the derived class of size{}".format(self._size)
        
        
        
s=stack()
for i in range(5):
    s.push(i)
d=ds()
#d.get_info()
#s.get_info()
d.set_size(6)
d.get_info()
s.get_info()
s.info()
print(s)


            
            
            
