def IsValidSudokuSolver(grid):
	def RowHelper(grid): # Check Row 
		for row in grid:
			if not Helper(row):
				return False 
			return True

	def ColHelper(grid): # Check Col 
		for col in zip(*grid):
			if not Helper(col):
				return False 
			return True 

	def BoxHelper(grid): # Check Box. Note : its i, j in (0, 3, 6) and not range(0, 3, 6)
		for i in (0, 3, 6):
			for j in (0, 3, 6):
				box = [grid[x][y] for x in range(i, i + 2) for y in range(j, j + 3)]
				if not Helper(box):
					return False 
		return True 

	def Helper(arr): # Actual function which checks for duplicate 
		check_arr = [i for i in arr if i != '.']
		return len(set(check_arr)) == len(check_arr)

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	return RowHelper(grid) and ColHelper(grid) and BoxHelper(grid)

grid =  [["5","3",".",".","7",".",".",".","."]
		,["6",".",".","1","9","5",".",".","."]
		,[".","9","8",".",".",".",".","6","."]
		,["8",".",".",".","6",".",".",".","3"]
		,["4",".",".","8",".","3",".",".","1"]
		,["7",".",".",".","2",".",".",".","6"]
		,[".","6",".",".",".",".","2","8","."]
		,[".",".",".","4","1","9",".",".","5"]
		,[".",".",".",".","8",".",".","7","9"]]

print(IsValidSudokuSolver(grid))