def SearchSorted(grid, target):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return -1 
	i, j = 0 , n - 1
	while i < m - 1 and j >= 0 :
		if grid[i][j] == target: return (i, j) 
		elif grid[i][j] > target : j -= 1
		elif grid[i][j] < target : i += 1
	return -1 

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(SearchSorted(grid, 6))