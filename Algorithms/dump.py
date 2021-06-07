def OrderedSearch(grid, target):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return -1 
	low = 0
	high = m*n - 1
	while high >= low:
		temp = (low + high)//2
		mid = grid[temp//m][temp % n]
		if mid == target:
			return temp//m, temp %n
		elif mid < target:
			low = temp + 1
		else:
			high = temp - 1
	return False 

grid = [[1,2, 3], [4, 5, 6], [7,8,9]]
print(OrderedSearch(grid, 3))
