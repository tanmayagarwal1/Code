#import MyPrinter 

def NumIsland(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	count = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				count += HelperIsland(grid, i, j)
	return count 


def HelperIsland(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1 :
		return 0 
	grid[i][j] = -1
	neighbours = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbours:
		HelperIsland(grid, i + dx, j + dy)
	return 1 

def CountIsland(grid, i, j):
	m, n, q= len(grid), len(grid[0]), 0
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
	phi = HelperCount(grid, i + 1, j)
	psi = HelperCount(grid, i, j + 1)
	mu  = HelperCount(grid, i, j - 1)
	nu  = HelperCount(grid, i - 1, j)
	return phi + psi + mu + nu + 1

def Surrounding(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	for i in range(m):
		if grid[i][0] == 'O':
			HelperSurround(grid, i, 0)
	for i in range(m):
		if grid[i][n - 1] == 'O':
			HelperSurround(grid, i, n - 1)
	for i in range(n):
		if grid[0][i] == 'O':
			HelperSurround(grid, 0, i)
	for i in range(n):
		if grid[m - 1][i] == 'O':
			HelperSurround(grid, m - 1, i)
	for i in range(m):
		for j in range(n):
			if grid[i][j] == -1:
				grid[i][j] = 'O'
			elif grid[i][j] == 'O':
				grid[i][j] = "X"
	return grid 

def HelperSurround(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 'O':
		return 
	grid[i][j] = -1
	neighbours = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbours:
		HelperSurround(grid, i + dx, j + dy)
	return 

def WordSearch(grid, word):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and HelperWord(grid, word, i, j, 0):
				return True 
	return False 

def HelperWord(grid, word, i, j, count):
	if count == len(word):
		return True 
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[0]:
		return False 
	grid[i][j] = -1 
	Boolean = HelperWord(grid, word, i + 1, j, count + 1) or \
			  HelperWord(grid, word, i, j + 1, count + 1) or \
			  HelperWord(grid, word, i, j - 1, count + 1) or \
			  HelperWord(grid, word, i - 1, j, count + 1) 
	return Boolean 

def PacificAtlantic(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	pacific_visited = [[False for _ in range(n)] for _ in range(m)]
	atlantic_visited = [[False for _ in range(n)] for _ in range(m)]
	for i in range(m):
		HelperOcean(grid, i, 0, pacific_visited)
		HelperOcean(grid, i, n - 1, atlantic_visited)
	for i in range(n):
		HelperOcean(grid, 0, i, pacific_visited)
		HelperOcean(grid, m - 1, i, atlantic_visited)
	res = []
	for i in range(m):
		for j in range(n):
			if pacific_visited[i][j] and atlantic_visited[i][j]:
				res.append([i, j])
	return res 

def HelperOcean(grid, i, j, visited):
	visited[i][j] = 1
	neighbours = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbours:
		x = i + dx 
		y = j + dy
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] < grid[i][j] :
			continue 
		HelperOcean(grid, x, y, visited)

def RottenOranges(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	rotten, fresh, minutes = [], 0, 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 2:
				rotten.append((i, j))
			elif grid[i][j] == 1:
				fresh += 1
	while rotten and fresh:
		minutes += 1
		for _ in range(len(rotten)):
			i, j = rotten.pop(0)
			neighbours = ((0,1), (0,-1), (-1,0), (1,0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 2 or grid[x][y] == 0:
					continue
				grid[x][y] = 2
				fresh -= 1
				rotten.append((x, y))
	return minutes 


def FloodFill(grid, sr, sc, new):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return - 1
	HelperFlood(grid, sr, sc, grid[sr][sc], new)
	return grid 

def HelperFlood(grid, i, j, old, new):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] != old:
		return 
	grid[i][j] = new 
	neighbours = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbours:
		HelperFlood(grid, i + dx, j + dy, old, new)
	return 

def LampIlluminations(n, lamps, queries): # 1 = Off , 0 = On 
	if not lamps or not n or not queries : return - 1
	grid = BuildGrid(n)
	neighbours = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1, -1))
	for i, j in lamps:
		grid[i][j] = 0
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
				continue
			Helperilluminate(grid, x, y, dx, dy)
	res = []
	for i, j in queries:
		if grid[i][j] == 0:
			res.append(1)
		else:
			res.append(0)
		HelperDilluminate(grid, i, j) 
	return res 

def Helperilluminate(grid, i, j, dx, dy):
	grid[i][j] = 0 
	x = i + dx
	y = j + dy 
	if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
		return 
	Helperilluminate(grid, x, y, dx, dy)


def HelperDilluminate(grid, i, j):
	neighbours = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1, -1))
	for dx, dy in neighbours:
		x = i + dx 
		y = j + dy 
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
			continue
		grid[x][y] = 1

def BuildGrid(n):
	return [[1 for _ in range(n)] for _ in range(n)]

def IncreasingSubPath(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0 : return -1 
	dp = [[0 for _ in range(n)]for j in range(m)]
	res = []
	for i in range(m):
		for j in range(n):
			res.append(dfs(grid, i, j, dp))
	return max(res)

def dfs(grid, i, j, dp):
	if not dp[i][j]:
		val = grid[i][j]

		if i and val > grid[i - 1][j]:
			Up = dfs(grid, i - 1, j, dp)
		else:
			Up = 0 

		if i < len(grid) - 1 and val > grid[i + 1][j]:
			Down = dfs(grid, i + 1, j, dp)
		else:
			Down = 0 

		if j and val > grid[i][j - 1]:
			Left = dfs(grid, i, j - 1, dp)
		else:
			Left = 0 

		if j < len(grid[0]) - 1 and val > grid[i][j + 1]:
			Right = dfs(grid, i, j + 1, dp)
		else:
			Right = 0 

		dp[i][j] = max(Up, Down, Left, Right) + 1 

	return dp[i][j]


def UniquePath(m, n):
	if not m or not n :
		 return -1 
	dp = [[1 for _ in range(n)]for _ in range(m)]
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
		if not grid[i][0] : dp[i][0] = 1 # 0th Col

	for i in range(1, n):
		if not grid[0][i] : dp[0][i] = 1 # 0th Row

	for i in range(1, m):
		for j in range(1, n):
			if grid[i][j]:
				continue 
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

	return dp[m - 1][n - 1]

def MinimumCostPath(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[0][0] = grid[0][0]
	for i in range(1, m):
		dp[i][0] = dp[i - 1][0] + grid[i][0]

	for i in range(1, n):
		dp[0][i] = dp[0][i - 1] + grid[0][i]

	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = min(dp[i][j] + dp[i - 1][j], dp[i][j] + dp[i][j - 1]) + grid[i][j]
	return dp[m - 1][n - 1]

def FirstOccurance(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	for i in range(m):
		for j in range(n):
			idx = HelperFirst(grid[i], 0, n - 1)
			if idx != - 1: break 
	return i, idx 

def HelperFirst(arr, l, h):
	if h < l : return -1 
	while h >= l:
		mid = l + (h - l)//2
		if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
			return mid 
		elif arr[mid] == 0:
			l = mid + 1
		else:
			h = mid - 1
	return - 1

def MaxOccurance(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return - 1
	res = 0 
	for i in range(m):
		for j in range(n):
			idx = HelperMax(grid[i], 0, n - 1)
			if idx != - 1: 
				count = n - idx 
				if res < count:
					res = count
					my_idx = i  

	return res, my_idx

def HelperMax(arr, l, h):
	if h < l : return - 1
	while h >= l : 
		mid = l + (h - l)//2
		if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
			return - 1
		elif arr[mid] == 0 :
			l = mid + 1
		else:
			h = mid - 1
	return -1 

def DiagonalTraversal(grid):
	m, n, res = len(grid), len(grid[0]), []
	if m == 0 or n == 0 :
		return -1 
	d = dict()
	for i in range(m):
		for j in range(len(grid[i])):
			if i + j in d.keys():
				d[i + j].append(grid[i][j])
			else:
				d[i + j] = [grid[i][j]]
	for i in d.keys():
		if i & 1 :
			[res.append(x) for x in d[i]]
		else:
			[res.append(x) for x in d[i][::-1]]
	return res 

def SpiralMatrix(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	Top, Bottom, Left, Right, arr, max_arr = 0, m - 1, 0, n - 1, [], m * n
	while len(arr) < max_arr:
		for i in range(Left, Right + 1):
			if len(arr) < max_arr:
				arr.append(grid[Top][i])
		Top += 1

		for i in range(Top, Bottom + 1):
			if len(arr) < max_arr:
				arr.append(grid[i][Right])
		Right -= 1

		for i in range(Right, Left - 1, -1):
			if len(arr) < max_arr:
				res.append(grid[Bottom][i])
		Bottom -= 1

		for i in range(Bottom, Top - 1, -1):
			if len(arr) < max_arr:
				res.append(grid[i][Left])
		Left += 1

	return arr 

def AntiSpiralMatrix(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	Top, Bottom, Left, Right, arr, max_arr = 0, m - 1, 0, n - 1, [], m * n
	while len(arr) < max_arr:
		for i in range(Right, Left - 1, - 1):
			if len(arr) < max_arr:
				arr.append(grid[Top][i])
		Top += 1

		for i in range(Top, Bottom + 1):
			if len(arr) < max_arr:
				arr.append(grid[i][Left])
		Left += 1

		for i in range(Left, Right + 1):
			if len(arr) < max_arr:
				arr.append(grid[Bottom][i])
		Bottom -= 1

		for i in range(Bottom, Top - 1, -1):
			if len(arr) < max_arr:
				arr.append(grid[i][Right])
		Right -= 1

	return arr 












