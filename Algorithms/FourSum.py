def fourSum(arr, target):
    def Helper(arr, target, n, path, res):
        if len(arr) < n or n < 2 or target < arr[0] * n or target > arr[-1] * n:
            return 
        if n == 2:
            l, r = 0, len(arr) - 1
            while l < r :
                s = arr[l] + arr[r]
                if s == target:
                    res.append(path + [arr[l], arr[r]])
                    l += 1 
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(arr) - n + 1):
                if i == 0 or (i > 0 and arr[i - 1] != arr[i]):
                    Helper(arr[i + 1:], target - arr[i], n - 1, path + [arr[i]],res)
    res = []
    Helper(sorted(arr), target, 4, [], res)
    return res 

arr = [2,2,2,2,2]
target = 8
print(fourSum(arr, target))