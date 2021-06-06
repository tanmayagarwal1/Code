def MusicRuntime(arr, target):
    if len(arr) == 0:
        return -1 
    res, curr_max = dict(), float('-inf')
    for i in range(len(arr)):
        find = target - 30 - arr[i]
        if find in res.keys():
            if max(find, arr[i]) > curr_max:
                curr_max = max(find, arr[i])
                result = [i, res[find]]
        res[arr[i]] = i 

    if not result : return [-1, -1]
    else : return sorted(result)


time = 100
arr = [1, 10, 25, 35, 60]
print(MusicRuntime(arr, time))