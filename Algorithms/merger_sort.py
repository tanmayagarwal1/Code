def mergesort(ar):
    if len(ar)>1:
        mid= len(ar)//2
        l=ar[:mid]
        r=ar[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                ar[k]=l[i]
                i=i+1
            else: 
                ar[k]=r[j]
                j=j+1
            k=k+1

        while i<len(l):
            ar[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            ar[k]=r[j]
            j=j+1
            k=k+1
a=[3,5,6,8,4,1,2]
mergesort(a)
print(a)                           
