def Trips(arr):
    n=len(arr)
    for i in range(n):
        arr[i]=arr[i]**2
    arr.sort()
    for i in range(n):
        j=0 
        k=i-1
        while j<k:
            if arr[j] +arr[k] ==arr[i]:
                return True 
            else:
                if arr[j]+arr[k]<=arr[i]:
                    j+=1
                else:
                    k-=1
    return True 

def Dups(arr):
    n=len(arr)
    s=set()
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
        else:
            print(arr[i])
def dups(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                print(arr[j])
def rev(sti):
    n=len(sti)
    sti=[i for i in sti]
    j=0
    for i in range(n-1,n//2,-1):
        if sti[i].isalpha():
            while j<i:
                if sti[j].isalpha():
                    sti[i], sti[j] = sti[j], sti[i]
                    j+=1
                    break
                else:
                    j+=1 
    return sti

def Kadens(arr):
    n=len(arr)
    i=0 
    j=arr[i]
    for k in range(n):
        j=j+arr[k]
        if i<j:
            i=j 
        if j<0:
            j=0 
    return i 

def UNique(sti):
    n=len(sti)
    s, q = set(), []
    for i in range(n):
        if sti[i] not in s:
            s.add(sti[i])
        else:
            q.append(sti[i])
    for i in sti:
        if i not in q:
            print(i)


def Blocks(arr,interests):
    q=[]
    n=len(arr)
    for i in arr:
        count=0
        for j,k in i.items():
            for z in range(len(interests)):
                if j==interests[z] and k==True:
                    count+=1
        q.append(count)
    res=q[0]
    for i in range(len(q)):
        res=max(res,q[i])
    return q.index(res)+1 


def Houses(arr,b):
    n=len(arr)
    q=[]
    for i in range(n):
        if arr[i]>b:
            continue 
        initial = arr[i]
        count = 1
        for j in range(n):
            if i==j:
                continue
            if arr[j] + initial <= b:
                initial= initial + arr[j]
                count+=1
        q.append(count)
    res=q[0]
    for i in range(len(q)):
        res=max(res,q[i])
    return res 

def Subarraysum(arr,k):
    window_sum=sum(arr[:k])
    res=0 
    for i in range(len(arr)-k):
        window_sum= window_sum -arr[i] + arr[i+k]
        res=max(res, window_sum)
    return res 

def maxelement(arr,k):
    q=[]
    n=len(arr)
    res=0
    for i in range(k):
        q.append(arr[i])
    for i in range(n-k+1):
        for j in range(k):
            res=max(res,q[j])
        q.pop(0)
        if i+k<n:
            q.append(arr[i+k])
    return res 


def startingWith(arr,pattern):
    n=len(pattern)
    q=[]
    for i in arr:
        count=0
        for j in range(len(pattern)):
            if i[j] == pattern[j]:
                count +=1
            else:
                break 
            if count == len(pattern):
                q.append(i)
    return q 



def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        Heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        Heapify(arr, i, 0)
def Heapify(arr,n,i):
    large=i 
    l=2*i+1
    r=2*i+2
    if l<n and arr[large]<arr[l]:
        large = l
    if r<n and arr[large]<arr[r]:
        large = r
    if large != i :
        arr[large], arr[i] = arr[i], arr[large]
        Heapify(arr, n, large)

def Mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        Mergesort(l)
        Mergesort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k +=1
        while i<len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k] = r[j]
            j +=1
            k +=1
#HEAPSORT 
a=[2,4,3,6,5,8,7]
Mergesort(a)
print(a)



