def CanPartition(arr):
    if len(arr) == 0 :
        return - 1
    target, n = sum(arr), len(arr)
    if target & 1 : return False
    target >>= 1 
    dp = [True] + [False for _ in range(target)]
    for num in arr:
        for i in range(target, num - 1, -1):
            if dp[target] == True : return True 
            dp[i] = dp[i] or dp[i - num]
    return dp[target]


print(CanPartition([2, 2, 3, 5]))
