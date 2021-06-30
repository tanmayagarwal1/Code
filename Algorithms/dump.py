def NumIsland(grid):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return 0 
		grid[i][j] = - 1
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy)
		return 1 

	m, n = len(grid), len(grid[0])
	if  m == 0 or n == 0 : raise ValueError 
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	count = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				count += Helper(grid, i, j)
	return count

def CountIsland(grid):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return 0 
		grid[i][j] = - 1
		Phi = Helper(grid, i + 1, j)
		Psi = Helper(grid, i, j + 1)
		Mu  = Helper(grid, i, j - 1)
		Nu  = Helper(grid, i - 1, j)
		return Phi + Psi + Mu + Nu + 1 

	m, n = len(grid), len(grid[0])
	if  m == 0 or n == 0 : raise ValueError 
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	q = []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				count = Helper(grid, i, j)
				q.append(count)
	return q 

def Surrounding(grid):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "O":
			return 
		grid[i][j] = - 1
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		if grid[i][0] == "O":
			Helper(grid, i, 0)
	for i in range(m):
		if grid[i][n - 1] == "O":
			Helper(grid, i, n - 1)
	for i in range(n):
		if grid[0][i] == "O":
			Helper(grid, 0, i)
	for i in range(n):
		if grid[m - 1][i] == "O":
			Helper(grid, m - 1, i)
	for i in range(m):
		for j in range(n):
			if grid[i][j] == -1:
				grid[i][j] = "O"
			elif grid[i][j] == "O":
				grid[i][j] = "X"
	return grid 

def WordSearch(grid, word):
	def Helper(grid, i, j, word, count):
		if count == len(word) : return True 
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[count] : return False 
		grid[i][j] = - 1
		Boolean = Helper(grid, i + 1, j, word, count + 1) or \
				  Helper(grid, i, j + 1, word, count + 1) or \
				  Helper(grid, i, j - 1, word, count + 1) or \
				  Helper(grid, i - 1, j, word, count + 1) 
		return Boolean

	m, n = len(grid),len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and Helper(grid, i, j, word, 0):
				return True 
	return False 

def PacificAtlantic(grid):
	def Helper(grid, i, j, visited):
		visited[i][j] = True 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[i][j] > grid[x][y]:
				continue 
			Helper(grid, x, y, visited)

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	pacific_visited = [[False for _ in range(n)] for _ in range(m)]
	atlantic_visited = [[False for _ in range(n)] for _ in range(m)]
	for i in range(m):
		Helper(grid, i, 0, pacific_visited)
		Helper(grid, i, n - 1, atlantic_visited)
	for i in range(n):
		Helper(grid, 0, i, pacific_visited)
		Helper(grid, m - 1, i, atlantic_visited)
	res = []
	for i in range(m):
		for j in range(n):
			if pacific_visited[i][j] and atlantic_visited[i][j]:
				res.append([i, j])
	return res 

def RottenOranges(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
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
			i, j = rotten.pop()
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 2 or grid[x][y] == 0 :
					continue 
				grid[x][y] = 2
				fresh -= 1
				rotten.append((x, y))
	return minutes

def GridIllumination(n, lamps, queries):
	def Helper(grid, i, j, dx, dy):
		grid[i][j] = 1
		x = i + dx
		y = j + dy 
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
			return 
		Helper(grid, x, y, dx, dy)

	def HelperOff(grid, i, j):
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
		for dx, dy in neighbours:
			x = i + dx
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
				continue 
			grid[x][y] = 0
		return 

	if not n : raise ValueError
	grid = [[0 for _ in range(n)] for _ in range(n)]
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
	for i, j in lamps:
		grid[i][j] = 0 
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
				continue
			Helper(grid, x, y, dx, dy)
		grid[x - dx][y - dy] = 1 

	res = []
	for i, j in queries:
		if grid[i][j] : res.append(1)
		else: res.append(0)
		HelperOff(grid, i, j)
	return res 

def Convolutions(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0))
	for i in range(m):
		for j in range(n):
			tmp = []
			for dx, dy in neighbours:
				x = i + dx
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
					continue 
				tmp.append(grid[x][y])
			grid[i][j] = sum(tmp)//len(tmp)
	return grid 

def FirstOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return -1
		while h >= l :
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
				return mid 
			elif arr[mid] == 0 :
				l = mid + 1
			else:
				h = mid - 1
		return - 1
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		idx = Helper(grid[i], 0, n - 1)
		if idx != - 1: break 
	return i, idx 

def MaxOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return -1
		while h >= l :
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid ==0):
				return mid
			elif arr[mid] == 0 :
				l = mid + 1
			else:
				h = mid - 1
		return -1 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	res = 0 
	for i in range(m):
		idx = Helper(grid[i], 0, n - 1)
		if idx != - 1: 
			count = n - idx 
			if res < count:
				res = count 
				my_idx = i 
	return res, i  

def MineSweeper(grid, clicks):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "E":
			return 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
		count = 0 
		for dx, dy in neighbours:
			x = i + dx
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 'M':
				continue 
			count += 1
		if count : 
			grid[i][j] = count 
		else:
			grid[i][j] = "B"
			for dx, dy in neighbours:
				Helper(grid, i + dx, j + dy)
			return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	i, j = clicks 
	if grid[i][j] == "M":
		grid[i][j] = "B"
	elif grid[i][j] == "E":
		Helper(grid, i, j)
	return grid 

def DiagonalTraversal(grid):
	d = {}
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	for i in range(m):
		for j in range(len(grid)):
			if i + j in d :
				d[i + j].append(grid[i][j])
			else:
				d[i + j] = [grid[i][j]]
	res = []
	for i in d.values():
		if i & 1 : [res.append(x) for x in d[i]]
		else: [res.append(x) for x in d[i][::-1]]
	return res 

def ColourGrid(n):
	if not n : raise ValueError
	a121 = 6 
	a123 = 6 
	for i in range(n - 1):
		tmp1 = a121 * 3 + a123 * 2 
		tmp2 = a121 * 2 + a123 * 2 
		a121 = tmp1 
		a123 = tmp2 
	return a121 + a123 

def KnightDialer(n):
	x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 0 
	for _ in range(n - 1):
		x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
		x6 + x8, \
		x7 + x9, \
		x4 + x8, \
		x9 + x3 + x0,\
		0, \
		x1 + x7 + x0, \
		x2 + x6, \
		x1 + x3, \
		x4 + x2, \
		x4 + x6  
	return (x1+ x2+ x3+ x4+ x5+ x6+ x7+ x8+ x9+ x0 ) % (10**9 + 7)

def WallsAndGates(grid):
	def Helper(grid, i, j, count):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] < count:
			return 
		grid[i][j] = count 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, count + 1)
		return 

	m, n = len(grid),len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 0:
				Helper(grid, i, j, 0)
	return grid 

def KnightProbabiltiy(n, k, r, c):
	if not n : raise ValueError
	res = 0 
	def Helper(n, i, j, moves, res):
		if i < 0 or i >= n or j < 0 or j >= n : return 0
		if moves == 0 : return 1
		neighbours = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
		for dx, dy in neighbours:
			res += Helper(n, i + dx, j + dy, moves - 1, res)
		return res / 8 

	return Helper(n, r, c, k, res)

def FloodFill(grid, sr, sc, new):
	if not grid : raise ValueError
	m, n = len(grid), len(grid[0])
	old = grid[sr][sc]
	q = [(sr, sc)]
	while q:
		i, j = q.pop(0)
		grid[i][j] = new 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid) or grid[x][y] != old:
				continue
			q.append((x, y))
	return grid 

def FloodFillDfs(grid, sr, sc, new):
	def Helper(grid, i, j, old, new):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != old:
			return 
		grid[i][j] = new 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, old, new)
		return 
	if not sr or not sc or not grid : raise ValueError
	Helper(grid, sr, sc, grid[sr][sc], new)
	return grid 


def SpiralMatrix(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
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
				arr.append(grid[Bottom][i])
		Bottom -= 1

		for i in range(Bottom, Top - 1, -1):
			if len(arr) < max_arr:
				arr.append(grid[i][Left])
		Left += 1
	return arr 


def AntiSpiral(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	Top, Bottom, Left, Right, arr, max_arr = 0, m - 1, 0, n - 1, [], m * n 
	while len(arr) < max_arr:
		for i in range(Right, Left - 1, -1):
			if len(arr) < max_arr :
				arr.append(grid[Top][i])
		Top += 1

		for i in range(Top, Bottom + 1):
			if len(arr) < max_arr :
				arr.append(grid[i][Left])
		Left += 1

		for i in range(Left, Right + 1):
			if len(arr) < max_arr :
				arr.append(grid[Bottom][i])
		Bottom -= 1

		for i in range(Bottom, Top - 1, -1):
			if len(arr) < max_arr :
				arr.append(grid[i][Right])
		Right -= 1

	return arr 

def SubIslands(grid, gridd):
	def Helper(grid, i, j, seen):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return 
		grid[i][j] = -1
		seen.add((i, j))
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, seen)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	sen = set()
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				Helper(grid, i, j, sen)
	res = 0
	for i in range(len(gridd)):
		for j in range(len(gridd[0])):
			if gridd[i][j] == 1:
				seen = set()
				Helper(gridd, i, j, seen)
				if all(grid[a][b] == -1 for a, b in seen):
					res += 1
	return res 

def MaxPerimeter(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	area = 0
	connect = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				area += 1
				if i > 0 and grid[i - 1][j] : connect += 1
				if j > 0 and grid[i][j - 1] : connect += 1

	return ( area * 4 ) - ( connect * 2 )








