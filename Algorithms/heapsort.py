def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
    
    
def heapify(arr,n ,i ):
    large=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[large]<arr[l]:
        large=l
    if r<n and arr[large]<arr[r]:
        large=r
    if large != i:
        arr[i],arr[large]=arr[large],arr[i]
        heapify(arr,n,large)
         
a=[2,4,3,6,5,8,7]
print(a)
heapsort(a)
print(f"after sorting array is {a}")