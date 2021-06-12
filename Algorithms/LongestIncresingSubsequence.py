def LongestIncresingSubsequence(arr):    
    y = Formater(arr)
    return Lcs(arr, y)

def Lcs(x, y):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return -1 
    dp = [[0 for _ in range(n +1)]for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i- 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
    return dp[m][n]

def Formater(arr):
    s, q = set(), []
    for num in arr:
        if num not in s:
            s.add(num)
            q.append(num)
        else:
            continue 
    return sorted(q)
    

arr = [10,9,2,5,3,7,101,18]
print(LongestIncresingSubsequence(arr))
