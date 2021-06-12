def LongestPalindromicSubsequence(sti):
    x = sti[::-1]
    return Lcs(sti, x)

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

print(LongestPalindromicSubsequence('agbcba'))