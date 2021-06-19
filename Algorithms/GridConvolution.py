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
			tmp = []
			for dx, dy in neighbours:
				x = i + dx
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
					continue 
				tmp.append(grid[x][y])
			res[i][j] = sum(tmp)//len(tmp)
	return res 

grid = [[100,200,100],[200,50,200],[100,200,100]]
print(ImageSmoother(grid))