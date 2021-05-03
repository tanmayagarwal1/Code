def minmoves(arr):
    n=len(arr)
    res=0 
    mini= min(arr)
    for i in range(n):
        diff=arr[i]-mini
        res=res+diff 
    return res 

    
print(minmoves([1,1]))


