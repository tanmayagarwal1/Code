class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class ll:
    def __init__(self):
        self.head=None 
    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else: 
            nn=node(data)
            nn.next=self.head 
            self.head=nn 
    def append(self,data):
        if self.head == None: 
            nn=node(data)
            nn.next=self.head
            self.head=nn
        else : 
            nn=node(data)
            temp=self.head
            while temp.next != None : 
                temp=temp.next
            temp.next=nn
            nn.next=None        

    def  dele(self,data):
        if self.head.data==data:
            self.head=self.head.next
        else:   
            temp=self.head 
            while temp.data != data:
                prev=temp
                temp=temp.next
            prev.next=temp.next
            temp.next=None  

    def rev(self):
        temp=self.head
        ne = None
        pre=None 
        while temp!= None : 
            ne=temp.next 
            temp.next=pre
            pre=temp
            temp=ne
        self.head=pre

    def mid(self):
        fast=self.head
        slow=self.head
        count=0
        while fast != None and fast.next != None:
            count=count+1 
            fast=fast.next.next 
            slow=slow.next 
        print(f"middle of the list is {slow.data} and the node number is {count+1} ")  
    def len(self):
        temp=self.head
        count=0
        while temp != None:
            count =count+1 
            temp=temp.next 
        return count    
      
    def __add__(self,other):
        li3=ll()
        x=self.len()
        y=other.len()
        if x<y: 
            temp=self.head 
            temp2=other.head
        else:
            temp=other.head
            temp2=self.head

        while temp != None: 
            li3.append(temp.data + temp2.data)
            temp=temp.next
            temp2=temp2.next
        while temp2 != None:
            li3.append(temp2.data)
            temp2=temp2.next  
        return li3    

    def remdup(self): # TO REMOVE DUPLICATES 
        temp=self.head
        while temp.next != None:
            temp1=temp.next 
            pre=temp
            while temp1.next != None:
                if temp1.data==temp.data:
                    pre.next=temp1.next
                    temp1=temp1.next 
                    pre=temp1
                else:
                    pre=temp1
                    temp1=temp1.next
            temp=temp.next
    def oddeve(self): # TO GROUP ODD NODES WITH EVEN NODES 
        count=0
        temp1=self.head 
        head=self.head 
        temp=head.next 
        pre=temp
        while temp1 != None:
            count+=1
            temp1=temp1.next
        while temp.next != None:
            head.next=temp.next
            head=temp
            temp=head.next
        if count%2==0:
            head.next=pre
            temp.next=None
        else:            
            temp.next=pre 
            head.next=None
        return count
    def lastn(self,num): # TO DELETE THE SPECIFIED NODE FROM LAST 
        if self.head==None:
            return
        n=self.len()
        res=n-num 
        count=0 
        temp=self.head
        while count<res and temp.next != None:
            pre=temp
            temp=temp.next
            count+=1
        pre.next=temp.next



########PALINDOROME AND ITS UTILITY FUCNTIONS###################

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
            second=slow 
            pre.next=None 
            second=self.palrev(second)
            res = self.palcomp(self.head,second)
            second=self.palrev(second)
            if midnode != None:
                midnode.next=second
                pre.next=midnode
            else : 
                pre.next=second 
            return res 
    def palrev(self,head):
        cur=head
        ne=pre=None 
        while cur != None: 
            ne=cur.next
            cur.next=pre
            pre=cur
            cur=ne 
        head = pre 
        return head 

    def palcomp(self,head,second):
        head1=head
        head2=second
        while head1 and head2 :
            if head1.data == head2.data:
                head1=head1.next
                head2=head2.next
            else :
                return 0 
        if head1 ==None and head2 == None:
            return 1
        return 0 

################################################################
    def show(self):
        temp=self.head
        while temp != None:
            print(f"{temp.data} -->")
            temp=temp.next

    def __str__(self):
        return ("This is a linked list of the following order")

    def show(self):
        temp=self.head
        while temp != None:
            print(f"{temp.data}-->")
            temp=temp.next     

#######################LIST 1
li=ll()
li2=ll()
li.push(1)
li.push(0)
li.push(0)
li.push(1)
#######################LIST 2
li2=ll()
li2.push(3)
li2.push(5)
li2.push(6)
li2.push(3)
li2.append(100)
li2.append(20)
#######################LIST 3
li4=ll()
li4.append(1)
li4.append(2)
li4.append(3)
li4.append(4)
li4.append(5)
li4.append(6)
li4.append(1)
li4.append(8)
li4.append(9)
li4.remdup()
li4.show()
#############################
li2.dele(3)
li2.dele(20)