def CountNum(grid):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0:
		return -1 
	grid=[[int(grid[i][j]) for  j in range(n)]for i in range(m)]
	count = 0 
	q=[]
	for i in range(m):
		for j in range(n):
			if grid[i][j] ==1:
				r=HelperNum(grid, i, j, count)
				return r
	res=q[0]
	for i in range(len(q)):
		res=max(res, q[i])
	return res

def HelperNum(grid, i, j, count):
	if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
		return count 
	grid[i][j] = -1 
	x = HelperNum(grid, i+1, j, count+1)
	y = HelperNum(grid, i, j+1, count+1)
	z = HelperNum(grid, i-1, j, count+1)
	k = HelperNum(grid, i, j-1, count+1)
	return max(x,y,z,k)



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(CountNum(grid))