def ImageSmoother(grid):
	m, n = len(grid), len(grid[0])
	row = m
	col = n 
	if m == 0 or n == 0 :
		return -1 
	res = [[0 for _ in range(n)] for j in range(m)]
	neighbours = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1))
	for i in range(m):
		for j in range(n):
			temp = [grid[i+m][j+n] for m,n in neighbours if 0<=i+m<row and 0<=j+n<col] 
			res[i][j] = sum(temp)//len(temp)
	return res 

grid = [[100,200,100],[200,50,200],[100,200,100]]
print(ImageSmoother(grid))