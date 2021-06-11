def PaintersPartition(arr, k):
    if len(arr) == 0 : return -1 
    l, h, res = max(arr), sum(arr), 0
    while h >= l : 
        mid = (l + h)//2
        if IsValid(arr, k, mid):
            res = mid 
            h = mid - 1
        else:
            l = mid + 1
    return mid

def IsValid(arr, k, constraint):
    count, stu = 0, 1 
    for i in range(len(arr)):
        count += arr[i]
        if count > constraint:
            count = arr[i]
            stu += 1
    if stu > k : return False 
    return True 

arr = [15, 17, 20]
k = 2 
print(PaintersPartition(arr, k))

