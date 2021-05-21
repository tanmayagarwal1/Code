n=3
def minimumCostPath(cost,x,y):
	tc=[[0 for i in range(n)] for j in range(n)]
	tc[0][0]=cost[0][0]
	for i in range(1,x+1):
		tc[i][0]=tc[i-1][0]+cost[i][0]
	for j in range(1,y+1):
		tc[0][j]=tc[0][j-1]+cost[0][j]
	for i in range(1,x+1):
		for j in range(1,y+1):
			tc[i][j]=min(tc[i][j] + tc[i-1][j], tc[i][j] + tc[i][j-1] )+cost[i][j]
	return tc[x][y]


cost= [[1, 2, 3],
       [4, 8, 2],
       [1, 5, 3]]

print(minimumCostPath(cost, 2, 2))
