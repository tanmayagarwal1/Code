def Amazon(arr):
    if not arr: return 0 
    res = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i] : res[i-1] += 1
        else: res[i] += 1
    return res 

print(Amazon([10,15,5,3,16,12,2]))