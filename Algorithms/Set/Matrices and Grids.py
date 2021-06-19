n = 4 
def NumIslands(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 :
		return - 1
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	count = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				count += HelperIsland(grid, i, j)
	return count 

def HelperIsland(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
		return 0 
	grid[i][j] = -1
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
	for dx, dy in neighbours:
		HelperIsland(grid, i + dx, j + dy)
	return 1 

def CountIsland(grid):
	m, n, q = len(grid), len(grid[0]), []
	if m == 0 or n == 0:
		return - 1
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				x = HelperCount(grid, i, j)
				q.append(x)
	return q 

def HelperCount(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
		return 0 
	grid[i][j] = -1
	Phi = HelperCount(grid, i + 1, j)
	Psi = HelperCount(grid, i - 1, j)
	Mu  = HelperCount(grid, i, j + 1)
	Nu  = HelperCount(grid, i, j - 1)
	return Phi + Psi + Mu + Nu + 1

def Surrounding(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return - 1
	for i in range(m):
		if grid[i][0] == "O":
			HelperSurround(grid, i, 0)
	for i in range(m):
		if grid[i][n - 1] == "O":
			HelperSurround(grid, i, n - 1)
	for i in range(n):
		if grid[0][i] == "O":
			HelperSurround(grid, 0, i)
	for i in range(n):
		if grid[m - 1][i] == "O":
			HelperSurround(grid, m - 1, i)
	for i in range(m):
		for j in range(n):
			if grid[i][j] == -1:
				grid[i][j] = "O"
			elif grid[i][j] == "O":
				grid[i][j] = "X"
	return grid 

def HelperSurround(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "O":
		return 
	grid[i][j] = -1
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
	for dx, dy in neighbours:
		HelperSurround(grid, i + dx, j + dy)
	return 

def WordSearch(grid, word):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return - 1
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and HelperWord(grid, i, j, word, 0):
				return True 
	return False 

def HelperWord(grid, i, j, word, count):
	if count == len(word):
		return True
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[count]:
		return False
	grid[i][j] = -1 
	Boolean = HelperWord(grid, i + 1, j, word, count + 1) or \
			  HelperWord(grid, i, j + 1, word, count + 1) or \
			  HelperWord(grid, i, j - 1, word, count + 1) or \
			  HelperWord(grid, i - 1, j, word, count + 1) 
	return Boolean

def PacificAtalntic(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	pacific_visited = [[False for _ in range(n)] for _ in range(m)]
	atlantic_visited = [[False for _ in range(n)] for _ in range(m)]
	for i in range(m):
		HelperOCean(grid, i, 0, pacific_visited)
		HelperOCean(grid, i, n - 1, atlantic_visited)
	for i in range(n):
		HelperOCean(grid, 0, i, pacific_visited)
		HelperOCean(grid, m - 1, i, atlantic_visited)
	res = []
	for i in range(m):
		for j in range(n):
			if pacific_visited[i][j] and atlantic_visited[i][j]:
				res.append([i, j])
	return res 

def HelperOCean(grid, i, j, visited):
	visited[i][j] = True
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
	for dx, dy in neighbours:
		x = i + dx
		y = j + dy 
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[i][j] > grid[x][y]:
			continue 
		HelperOCean(grid, x, y, visited)

def RottenOranges(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	fresh, minutes, rotten = 0, 0, []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 2:
				rotten.append([i, j])
			elif grid[i][j] == 1:
				fresh += 1
	while rotten and fresh:
		minutes += 1
		for _ in range(len(rotten)):
			i, j = rotten.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 2 or grid[x][y] == 0:
					continue
				grid[x][y] = 2
				fresh -= 1
				rotten.append([x, y])
	return minutes

def FloodFill(grid, sr, sc, new):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return -1 
	HelperFlood(grid, sr, sc, grid[sr][sc], new)
	return grid 

def HelperFlood(grid, i, j, old, new):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != old:
		return 
	grid[i][j] = new 
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
	for dx, dy in neighbours:
		HelperFlood(grid, i + dx, j + dy, old, new)
	return 

def FloodFillBfs(grid, sr, sc, new):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 :
		return - 1
	q = [(sr, sc)]
	old = grid[sr][sc]
	grid[sr][sc] = new 
	while q:
		i, j = q.pop(0)
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			x = i + dx
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != old:
				continue
			q.append((x, y))
			grid[x][y] = new
	return grid 

def SearchInSortedMatrix(grid, target):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 :
		return - 1
	i, j = 0, len(grid[0]) - 1
	while i < len(grid) and j >= 0:
		if grid[i][j] == target:
			return True
		elif grid[i][j] > target:
			j -= 1
		elif grid[i][j] < target:
			i += 1
	return -1 

def UniquePath(m, n):
	if m == 0 or n == 0:
		return - 1
	dp = [[1 for _ in range(n)] for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
	return dp[m - 1][n - 1]

def UniquePaths2(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	dp = [[0 for _ in range(n)] for _ in range(m)]
	if not grid[0][0] : dp[0][0] = 1
	for i in range(1, m):
		if not grid[i][0]: dp[i][0] = 1
	for i in range(1, n):
		if not grid[0][i] : dp[0][i] = 1 
	for i in range(1, m):
		for j in range(1, n):
			if not grid[i][j]:
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
			else:
				continue
	return dp[m - 1][n - 1]

def MinimumcostPath(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[0][0] = grid[0][0]
	for i in range(1, m):
		dp[i][0] = dp[i - 1][0] + grid[i][0]
	for i in range(1, n):
		dp[0][i] = dp[0][i - 1] + grid[0][i]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = min(dp[i][j] + dp[i - 1][j], dp[i][j] + dp[i][j - 1])
	return dp[m - 1][n - 1]

def FirstOccurance(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	for i in range(m):
		idx = Binary(grid[i], 0, n - 1)
		if idx != -1:
			break 
	return i, idx 

def Binary(arr, l, h):
	if h < l : return - 1 
	while h >= l:
		mid = l + (h - l)//2
		if arr[mid] == 1 and(arr[mid - 1] == 0 or mid == 0):
			return mid 
		elif arr[mid] == 0:
			l = mid + 1
		else:
			h = mid - 1
	return  - 1

def MaxOccurance(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	res = 0 
	for i in range(m):
		idx = BinaryHelper(grid[i], 0, n - 1)
		if idx != -1:
			count = n - idx 
			if res < count:
				res = count 
				my_idx = i 
	return res, my_idx

def BinaryHelper(arr, l, h):
	if h < l : return -1 
	while h >= l:
		mid = l + (h - l)//2
		if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
			return mid 
		elif arr[mid] == 0:
			l = mid + 1
		else:
			h = mid - 1
	return -1 

def DiagonalTraversal(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	d = dict()
	for i in range(m):
		for j in range(len(grid[i])):
			if i + j in d:
				d[i + j].append(grid[i][j])
			else:
				d[i + j] = [grid[i][j]]
	res = []
	for i in d:
		if i & 1:
			[res.append(x) for x in d[i]]
		else:
			[res.append(x) for x in d[i][::-1]]
	return res 

def GridIllumination(n, lamps, queries):
	if not n or not lamps : return []
	grid = [[0 for _ in range(n)] for _ in range(n)]
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
	for i, j in lamps:
		grid[i][j] = 0 
		for dx, dy in neighbours:
			x = i + dx
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
				continue 
			HelperIlluminate(grid, x, y, dx, dy)
		grid[i][j] = 1 
	
	res = []
	for i, j in queries:
		if grid[i][j] == 1:
			res.append(1)
		else:
			res.append(0)
		IlumminateHelper(grid, i, j)
	return res 


def HelperIlluminate(grid, i, j, dx ,dy):
	grid[i][j] = 1 
	x = i + dx 
	y = j + dy 
	if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
		return 
	HelperIlluminate(grid, x, y, dx, dy)

def IlumminateHelper(grid, i, j):
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
	for dx, dy in neighbours:
		x = i + dx
		y = j + dy 
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
			continue
		grid[x][y] = 0

def GridConvolutions(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0))
	for i in range(m):
		for j in range(n):
			temp = []
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= m or y < 0 or y >= n:
					continue
				temp.append(grid[x][y])
			grid[i][j] = sum(temp)//len(temp)
	return grid 

def Nqueen():
	b = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0] ]
	if NqueenU(b, 0) == False:
		return False 
	printgrid(b)

def NqueenU(b, col):
	if col >= n:
		return True 
	for i in range(n):
		if issafe(b, i, col):
			b[i][col] = 1
			if NqueenU(b, col + 1):
				return True 
			b[i][col] = 0 
	return False 

def issafe(grid, row, col):
	for i in range(col):
		if grid[row][i] == 1:
			return False
	for i, j in zip(range(row, -1 , -1), range(col, -1, -1)):
		if grid[i][j] == 1:
			return False 
	for i, j in zip(range(row, n), range(col, -1, -1)):
		if grid[i][j] == 1:
			return False 
	return True 

def MazeSolver(grid):
	sol = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
	if MazeSolverU(grid, 0, 0, sol) == False:
		return False 
	printgrid(sol)

def MazeSolverU(grid, i, j, sol):
	if i == n - 1 and j == n - 1 and grid[i][j] == 1:
		sol[i][j] = 1
		return True 
	if Issafe(grid, i, j):
		if sol[i][j]:
			return False 
		sol[i][j] = 1
		if MazeSolverU(grid, i + 1, j, sol):
			return True 
		if MazeSolverU(grid, i, j + 1, sol):
			return True 
		if MazeSolverU(grid, i, j - 1, sol):
			return True 
		if MazeSolverU(grid, i - 1, j, sol):
			return True 
		sol[i][j] = 0 
	return False

def Issafe(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
		return False 
	return True 

def goldmine(grid):
	gt = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
	for col in range(len(grid[0]) - 1, -1 ,-1):
		for row in range(n):
			if col == n - 1:
				right = 0 
			else:
				right = gt[row][col + 1]
			if col == n - 1 or row == n - 1:
				right_down = 0 
			else:
				right_down = gt[row + 1][col + 1]
			if col == n - 1 or row == 0:
				right_up = 0 
			else:
				right_up = gt[row - 1][col + 1]
			gt[row][col] = max(right_up, right_down, right) + grid[row][col]
	res = gt[0][0]
	for i in range(n):
		res = max(res, gt[i][0])
	return res 

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()

def Rotate(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return -1 
	grid.reverse()
	for i in range(m):
		for j in range(i + 1, n):
			grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
	return grid 

def SpiralMatrix(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	Up, Down, Left, Right, arr, max_arr = 0, m - 1, 0, n - 1, [], m * n 
	while len(arr) < max_arr:
		for i in range(Left, Right + 1):
			if len(arr) < max_arr:
				arr.append(grid[Top][i])
		Top += 1

		for i in range(Top, Down + 1):
			if len(arr) < max_arr:
				arr.append(grid[Right][i])
		Right -= 1

		for i in range(Right, Left - 1, -1):
			if len(arr) < max_arr:
				arr.append(grid[Down][i])
		Down -= 1

		for i in range(Down, Top - 1, -1):
			if len(arr) < max_arr:
				arr.append(grid[i][Left])
		Left -= 1
	return arr 


def MineSweeper(grid, clicks):
	i, j = clicks
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 :
		return - 1
	if grid[i][j] == "M":
		grid[i][j] = "X"
	elif grid[i][j] == "E":
		dfs(grid, i, j)
	return grid 

def dfs(grid, i, j):
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
	if not Available(grid, i, j) or grid[i][j] == "E":
		return 
	count = 0 
	for dx, dy in neighbours:
		if Available(grid, i + dx, j + dy) and grid[i + dx][j + dy] == "M":
			count += 1
	if count:
		grid[i][j] = count 
	else:
		grid[i][j] = "B"
		for dx, dy in neighbours:
			dfs(grid, i + dx, j + dy)
	 

def Available(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
		return False 
	return True 

