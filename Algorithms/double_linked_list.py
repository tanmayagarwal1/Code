class node:
    def __init__(self,data):
        self.data=data
        self.next=self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head == None:
            self.head=node(data)
        else:
            nn=node(data)
            nn.next=self.head
            self.head.prev=nn
            nn.prev=None
            self.head=nn
    def append(self,data):
        if self.head == None:
            self.head=node(data)
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next 
            nn=node(data)
            temp.next=nn
            nn.prev=temp
            nn.next=None 
    def dele(self,data):
        count=0
        if self.head == None: 
            return 
        else:
            temp=self.head
            pre=None
            while temp.data != data:
                pre=temp
                count +=1
                temp=temp.next
            pre.next=temp.next
            temp.next.prev=pre 
            print("deleted the number {}".format(count))
    def search(self,data):
        if self.head == None: 
            return
        else : 
            if self.head.data==data:
                print(self.head.data)
            else:
                temp=self.head
                while temp.data != data:
                    temp=temp.next
                print(temp.data)
    def show(self):
        if self.head==None :
            return 
        else :
            temp=self.head
            while temp != None:
                print(f"{temp.data}-->")
                temp=temp.next
li=dll()
li.append(2)
li.append(3)
li.append(4)
li.show()
li.dele(3)
li.show()