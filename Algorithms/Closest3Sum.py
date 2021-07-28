def Sum3Closest(arr, target):
    if not arr : raise ValueError 
    arr.sort()
    res = 0 
    global_diff = float('inf')
    for i in range(len(arr) - 2):
        if i and arr[i] == arr[i - 1]:
            continue 
        l = i + 1
        r = len(arr) - 1
        while l < r :
            total = arr[i] + arr[l] + arr[r]
            local_diff = abs(total - target)
            if not local_diff : return total 
            if local_diff < global_diff:
                global_diff = local_diff 
                res = total
            if total < target:
                l += 1
            else:
                r -= 1
    return res 


arr = [-1, 2, -1, 4]
target = 1 
print(Sum3Closest(arr, target))