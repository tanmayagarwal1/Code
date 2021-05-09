def numBoats(arr, limit):
    n=len(arr)
    arr.sort()
    i, j, count = 0, n-1, 0
    while i<=j :
        if arr[i] +arr[j] <= limit:
            i+=1
            j-=1
        else:
            j-=1 
        count+=1
    return count 



print(numBoats([3,2,2,1],3))