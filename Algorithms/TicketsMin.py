def mincostTickets(days, costs):
    dp = [-1 for _ in range(366)]
    dp[0] = 0
    for day in days:
        dp[day] = 0
    for i in range(1,366):
        if dp[i] == -1:
            dp[i] = dp[i-1]
        else:
            dp[i] = min( dp[i-1] + costs[0],
                         dp[max(i-7,0)] + costs[1],
                         dp[max(i-30,0)] + costs[2] )
    return dp[365]

days = [1,4,6,7,8,20]
costs = [2,7,15]
print(mincostTickets(days, costs))                   