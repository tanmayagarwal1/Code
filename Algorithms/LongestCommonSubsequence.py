def lcs(x,y):
    n=len(x)
    m=len(y)
    lcs=[[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                lcs[i][j]=0 #THIS CAN BE SKIPPED BUT STILL WROTE IT 
            if x[i-1]==y[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+1
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
    return lcs[n][m]
print(lcs('tanmay','agarwal'))
