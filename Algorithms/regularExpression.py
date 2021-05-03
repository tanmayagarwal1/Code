def regularexpression(sti,pattern):
    if '*' not in pattern and '.' not in pattern:
        return sti==pattern 
    m=len(sti)
    n=len(pattern)
    dp=[[False for _ in range(n+1)]for _ in range(m+1)]
    dp[0][0]=True 
    for i in range(1,len(dp[0])):
        if pattern[i-1]=='*':
            dp[0][i]=dp[0][i-2]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if pattern[j-1]==0 or(sti[i-1]==pattern[j-1]):
                dp[i][j]=dp[i-1][j-1]
            elif pattern[j-1]=='*':
                dp[i][j]=dp[i][j-2]
                if pattern[j-2]=='.' or pattern[j-2]==sti[i-1]:
                    dp[i][j]=(dp[i][j] or dp[i-1][j])

    return dp[m][n]

print(regularexpression("mississippi","mis*is*ip*."))




