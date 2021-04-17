def heap(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        Heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        Heapify(arr,i,0)
        
def Heapify(arr,n,i):
    mini=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[mini]>arr[l]:
        mini=l
    if r<n and arr[mini]>arr[r]:
        mini=r
    if mini != i:
        arr[i],arr[mini]=arr[mini],arr[i]
        Heapify(arr,n,mini)
a=[4,2,67,4,3,221,5,4323,123,1415]
heap(a)
print(a)