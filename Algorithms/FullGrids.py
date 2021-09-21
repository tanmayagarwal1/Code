def NumIsland(grid):
	def Helper(grid, i, j):
		if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != 1 : 
			return 0 
		grid[i][j] = - 1
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy)
		return 1 

	m, n = len(grid), len(grid[0])
	if not m or not n : raise ValueError 
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	count = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1 : 
				count += Helper(grid, i, j)
	return count 

def CountIslands(grid):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return 0 
		grid[i][j] = -1
		Phi = Helper(grid, i + 1, j)
		Psi = Helper(grid, i, j + 1)
		Mu  = Helper(grid, i, j - 1)
		Nu  = Helper(grid, i - 1, j)
		return max(Phi, Psi, Mu, Nu) + 1
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	res = []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1 :
				res.append(Helper(grid, i, j))
	return res 

def Surrounding(grid):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "O":
			return 
		grid[i][j] = -1 
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
		if grid[i][n - 1] == 'O':
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
	def Helper(grid, word, count, i, j):
		if count == len(word): return True 
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[count]:
			return False 
		grid[i][j] = - 1
		return Helper(grid, word, count + 1, i + 1, j) or \
			   Helper(grid, word, count + 1, i, j + 1) or \
			   Helper(grid, word, count + 1, i, j - 1) or \
			   Helper(grid, word, count + 1, i - 1, j) 
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	count = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and Helper(grid, word, count, i, j):
				return True 
	return False 

def SubIslands(grid, gridd):
	def Helper(grid, s, i, j):
		if i < 0 or i >= len(grid) or j < 0 or  j >= len(grid[0]) or grid[i][j] != 1 :
			return 
		s.add((i, j))
		grid[i][j] = - 1
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, s, i + dx, j + dy )
		return 

	m, n = len(grid), len(gridd)
	if not m or not n : raise ValueError
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				s = set()
				Helper(grid, s, i, j)

	res = 0 
	for i in range(len(gridd)):
		for j in range(len(gridd[0])):
			if gridd[i][j] == 1 : 
				check = set()
				Helper(gridd, check, i, j)
				if all(grid[a][b] == -1 for a, b in check):
					res += 1 
	return res 

def ConnectedPerimeter(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	area, connected = 0 , 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1 : 
				area += 1 
				if i and grid[i - 1][j] : connected += 1 
				if j and grid[i][j - 1] : connected += 1
	return (area * 4) - (connected * 2)

def pacificAtlantic(grid):
	def Helper(grid, visited, i, j):
		visited[i][j] = 1 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[i][j] > grid[x][y]:
				continue 
			Helper(grid, visited, x, y)

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	pacific_visited = [[0 for _ in range(n)] for _ in range(m)]
	atlantic_visited = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(m):
		Helper(grid, pacific_visited, i, 0)
		Helper(grid, atlantic_visited, o, n - 1)
	for i in range(n):
		Helper(grid, pacific_visited, 0, i)
		Helper(grid, atlantic_visited, 0, i)
	res = []
	for i in range(m):
		for j in range(n):
			if pacific_visited[i][j] and atlantic_visited[i][j]:
				res.append((i, j))
	return res 

def GridIlluminations(m, lamps, queries):
	def Helper(grid, i, j, dx, dy):
		grid[i][j] = 1
		x = i + dx 
		y = j + dy 
		if x < 0 or x >= len(grid) or j < 0 or y >= len(grid[0]) : return 
		Helper(grid, x, y, dx, dy)

	def Helper2(grid, i, j):
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or j < 0 or y >= len(grid[0]) : continue 
			grid[x][y] = 0 
		return 

	if not m: raise ValueError
	grid = [[0 for _ in range(m)] for _ in range(m)]
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))
	for i, j in lamps:
		grid[i][j] = 0 
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : continue 
			Helper(grid, x, y, dx, dy)
		grid[i][j] = 1 

	res = []
	for i, j in queries:
		if grid[i][j] == 0 : res.append(0)
		elif grid[i][j] == 1 : res.append(1)
		Helper2(grid, i, j)
	return res 

def WallsAndGates(grid):
	def Helper(grid, i, j, count):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] < count:
			return 
		grid[i][j] = count 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, count + 1)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 0 : 
				Helper(grid, i, j, 0)
	return grid 

def RottenOranges(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q, fresh, min = [], 0, 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 2 : q.append((i, j))
			elif grid[i][j] == 1 : fresh += 1 
	while q and fresh:
		min += 1 
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 2 or grid[x][y] == 0 : 
					continue 
				grid[x][y] = 2 
				q.append((x, y))
				fresh -= 1
	return min 

def FloodFill(grid, sr, sc, new):
	def Helper(grid, i, j, old, new):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != old:
			return 
		grid[i][j] = new 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, old, new)

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	old = grid[sr][sc]
	Helper(grid, sr, sc, old, new)
	return grid 

def FloodFillBfs(grid, sr, sc, new):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	old = grid[sr][sc]
	q = [(sr, sc)]
	while q :
		i, j = q.pop(0)
		grid[i][j] = new 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != old : continue 
			q.append((x, y))
	return grid 

def MineSweeper(grid, click):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "E":
			return 
		count = 0 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))
		for dx, dy in neighbours :
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid) or grid[x][y] != "M":
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
	i, j = click 
	if grid[i][j] == 'M':
		grid[i][j] = "X"
	elif grid[i][j] == 'E':
		Helper(grid, i, j)
	return grid 

def FirstOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return  - 1
		while h >= l:
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
				return mid 
			elif arr[mid] == 0 : 
				l = mid + 1 
			else:
				h = mid -1 
		return -1 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	for i in range(m):
		idx = Helper(grid[i], 0, n - 1)
		if idx != -1 : 
			break 
	return i, idx 

def MaxOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return - 1
		while h >= l:
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
				return mid 
			elif arr[mid] == 0 : l = mid + 1 
			else : h = mid - 1 
		return -1 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	res = 0 
	for i in range(m):
		idx = Helper(grid[i], 0, n - 1)
		if idx != -1 : 
			count = n - idx 
			if count > res : 
				res = count 
				my_dx = i
	return my_dx, count 

def SearchInSortedMatrix(grid, target):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	i, j = 0, n - 1
	while i < m - 1 and j >= 0 : 
		if grid[i][j] == target : return (i, j)
		if grid[i][j] > target : j -= 1 
		elif grid[i][j] < target : i += 1 
	return -1 

def Reshape(grid, r, c):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 or r * c != m * n : raise ValueError
	box = [[0 for _ in range(c)] for _ in range(r)]
	arr = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
	idx = 0 
	for i in range(r):
		for j in range(c):
			box[i][j] = arr[idx]
			idx += 1
	return box 

def MatrixRotation(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	grid.reverse()
	for i in range(m):
		for j in range(i + 1, m):
			grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
	return grid 

def SprialMatrix(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	Top, Bottom, Left, Right, arr, max = 0, m - 1, 0, n - 1, [], m * n 
	while len(arr) < max:
		for i in range(Left, Right + 1):
			if len(arr) < max:
				arr.append(grid[Top][i])
		Top += 1 

		for i in range(Top, Bottom + 1):
			if len(arr) < max:
				arr.append(grid[i][Right])
		Right -= 1

		for i in range(Right, Left - 1, - 1):
			if len(arr) < max:
				arr.append(grid[Bottom][i])
		Bottom -= 1

		for i in range(Bottom, Top - 1, -1):
			if len(arr) < max:
				arr.append(grid[i][Left])
		Left += 1

	return arr 

def OutOfBounds(m, n, sr, sc, moves):
	def Helper(m, n, i, j, moves):
		if moves < 0 : return 0 
		if i < 0 or i >= m or j < 0 or j >= n : return 1 
		if dp[i][j][moves] != -1 : return dp[i][j][moves]
		Phi = Helper(m, n, i + 1, j, moves - 1)
		Psi = Helper(m, n, i, j + 1, moves - 1)
		Mu  = Helper(m, n, i, j - 1, moves - 1)
		Nu  = Helper(m, n, i - 1, j, moves - 1)
		dp[i][j][moves] = (Phi + Psi + Mu + Nu) % ((10**9) + 7)
		return dp[i][j][moves]
	if not m or not n : raise ValueError
	dp = [[[-1] * (moves + 1) for _ in range(n + 1)]for _ in range(m + 1)]
	return Helper(m, n, sr, sc, moves)

def ProbabilityKnight(n, sr, sc, moves):
	def Helper(i, j, moves):
		if i < 0 or i >= n or j < 0 or j >= n : return 0 
		if moves == 0 : return 1 
		return (Helper(i + 1, j + 2, moves - 1) + 
				Helper(i + 1, j - 2, moves - 1) + 
				Helper(i - 1, j + 2, moves - 1) + 
				Helper(i - 1, j - 2, moves - 1) + 
				Helper(i + 2, j + 1, moves - 1) + 
				Helper(i + 2, j - 1, moves - 1) + 
				Helper(i - 2, j + 1, moves - 1) + 
				Helper(i - 2, j - 1, moves - 1))/ 8 
	if not n : raise ValueError
	return Helper(sr, sc, moves)

def ColorGrid(rows):
	if not rows : raise ValueError
	a121, a123 = 6, 6
	for _ in range(rows - 1):
		a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2
	return (a121 + a123) % ((10**9) + 7)

def EscapeGrid(grid, start):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	i, j = start
	q = [(i, j)]
	grid[i][j] = '+'
	moves = 0 
	while q:
		moves +=1 
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '+' : continue 
				if x == 0 or x == m - 1 or y == 0 or y == n - 1 : return moves 
				q.append((x, y))
	return moves 


def KeysAndLocks(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	keys = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == '@':
				start = (i, j)
			elif grid[i][j] in 'abcdef':
				keys += 1 
	i, j = start 
	q = [(i, j, '')]
	seen = set()
	moves = 0 
	while q :
		moves += 1
		for _ in range(len(q)):
			i, j, key = q.pop(0)
			if (i, j, key) in seen : continue 
			if len(key) == keys : return moves -1 
			seen.add((i, j, key))
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '#':
					continue 
				val = grid[x][y]
				if val in "ABCDEF" and val.lower() in key:
					q.append((x, y, key))
				elif val in ".@":
					q.append((x, y, key))
				elif val in "abcedf":
					if val not in key:
						q.append((x, y, key + val))
					else:
						q.append((x, y, key))
	return -1

def MaxDistanceFromLand(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
	dist = 0 
	while q :
		dist += 1 
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or j < 0 or y >= len(grid[0]) or grid[x][y] != 0 : continue 
				grid[x][y] = 1 
				q.append((x, y))
	return dist 


def DungeonGame(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
	dp[m - 1][n], dp[m][n - 1] = 1, 1 
	for i in range(m - 1, -1, -1):
		for j in range(n - 1, -1, -1):
			dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - grid[i][j], 1)
	return dp[0][0]


def DiagonalTraversal(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	d = {}
	for i in range(m):
		for j in range(n):
			if i + j in d:
				d[i + j].append(grid[i][j])
			else:
				d[i + j] = [grid[i][j]]
	res = []
	for key in d:
		if key % 2 == 0 : [res.append(num) for num in d[key][::-1]]
		else : [res.append(num) for num in d[key]]
	return res 

def RobotMoves(sti):
	if not sti : raise ValueError
	x, y, dx, dy = 0, 0, 0, 1 
	for char in sti:
		if char == "G"   : x, y = x + dx, y + dy 
		elif char == "L" : dx, dy = -dy, dx 
		elif char == "R" : dx, dy = dy, -dx
	return (x, y) == (0, 0) or (dx, dy) != (0, 1) 

def GridConvolutions(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, 0))
	for i in range(m):
		for j in range(n):
			tmp = []
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : continue 
				tmp.append(grid[x][y])
			grid[i][j] = sum(tmp)//len(tmp)
	return grid 

def IncreasingSubPath(grid):
	def Helper(grid, i, j):
		if not dp[i][j] : 
			Phi, Psi, Mu, Nu = 0, 0, 0, 0
			val = grid[i][j]
			if i and val > grid[i - 1][j]:
				Phi = Helper(grid, i -1, j)

			if i < m - 1 and val > grid[i + 1][j]:
				Psi = Helper(grid, i + 1, j)

			if j and val > grid[i][j - 1]:
				Mu = Helper(grid, i, j - 1)

			if j < n - 1 and val > grid[i][j + 1]:
				Nu = Helper(grid, i, j + 1)

			dp[i][j] = max(Phi, Psi, Mu, Nu) + 1 
		return dp[i][j]

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	dp = [[0 for _ in range(n)] for _ in range(m)]
	res = 0
	for i in range(m):
		for j in range(n):
			res = max(res, Helper(grid, i, j))
	return res 

n = 4 
def NQueen():
	def isSafe(b, row, col):
		for i in range(col):
			if b[row][i] == 1 : return False 
		for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
			if b[i][j] == 1 : return False 
		for i, j in zip(range(row, n), range(col, -1, -1)):
			if b[i][j] == 1 : return False 
		return True 

	def Helper(b, col):
		if col >= n : return True 
		for i in range(n):
			if isSafe(b, i, col):
				b[i][col] = 1 
				if Helper(b, col + 1):
					return True 
				b[i][col] = 0 
		return False 

	sol = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
	if not Helper(sol, 0) : return -1 
	printsol(sol)

def printsol(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = " ")
		print()


def MazSolver(grid):
	def isSafe(maze, x, y):
		if x < 0 or x >= len(maze) or y < 0 or y >= len(maze) or maze[x][y] != 1 :
			return False 
		return True 

	def Helper(maze, x, y):
		if x == n - 1 and y == n - 1 : 
			sol[x][y] = 1 
			return True 
		if isSafe(maze, x, y):
			if sol[x][y] == 1 : return False
			sol[x][y] = 1 
			if Helper(maze, x + 1, y) : return True 
			if Helper(maze, x, y + 1) : return True 
			if Helper(maze, x, y - 1) : return True 
			if Helper(maze, x - 1, y) : return True 
			sol[x][y] = 0 
		return False 

	sol = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	if not Helper(maze, 0, 0) : return False 
	printsol(sol)

def GoldMax(grid):
	m, n = len(grid), len(grid[0])
	if not m or not n : raise ValueError
	gold = [[0 for _ in range(n)] for _ in range(m)]
	for col in range(n - 1, -1, -1):
		for row in range(m):
			if col == n - 1 : 
				right = 0 
			else:
				right = gold[row][col + 1]
			if col == n - 1 or row == m -1  : 
				right_down = 0 
			else:
				right_down = gold[row + 1][col + 1]
			if col == n - 1 or row == 0 : 
				right_up = 0 
			else:
				right_up = gold[row - 1][col + 1]
			gold[row][col] = max(right_down, right_up, right) + grid[row][col]
	res = 0 
	for i in range(m):
		res = max(res, gold[i][0])
	return res 

def GoldMine(grid):
	def Helper(grid, i, j, gold):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] <= 0 : 
			return gold 
		gold += grid[i][j]
		tmp = grid[i][j]
		res = 0 
		grid[i][j] = -1 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			res = max(res, Helper(grid, i + dx, j + dy, gold))
		grid[i][j] = tmp 
		return res 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	res = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] > 0 : 
				res = max(res, Helper(grid, i, j, 0))
	return res 



