def AntiSpiralMatrix(grid):
	m=len(grid)
	n=len(grid[0])
	if m==0 or n==0:
		return -1 
	Top, Bottom, Left, Right, max_arr, arr = 0, m-1, 0, n-1, m*n, []
	while len(arr)<max_arr:
		for i in range(Right, Left-1, -1):
			if len(arr)<max_arr:
				arr.append(grid[Top][i])
		Top += 1

		for i in range(Top, Bottom+1):
			if len(arr)<max_arr:
				arr.append(grid[i][Left])
		Left+=1

		for i in range(Left, Right+1):
			if len(arr)<max_arr:
				arr.append(grid[Bottom][i])
		Bottom -=1 

		for i in range(Bottom, Top-1, -1):
			if len(arr)<max_arr:
				arr.append(grid[i][Right])
		Right -=1
	return arr


matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8],
          [9,10,11,12]]
print(AntiSpiralMatrix(matrix))