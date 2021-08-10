def IsIsland(grid):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return 0 
		grid[i][j] = - 1
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy)
		return 1 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
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
		grid[i][j] = - 1
		Phi = Helper(grid, i + 1, j)
		Psi = Helper(grid, i - 1, j)
		Mu  = Helper(grid, i, j + 1)
		Nu  = Helper(grid, i, j - 1)
		return Phi + Psi + Mu + Nu + 1 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	q = []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				q.append(Helper(grid, i, j))
	return q 

def Surrounding(grid):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 'O':
			return 
		grid[i][j] = - 1
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	for i in range(m):
		if grid[i][0] == 'O':
			Helper(grid, i, 0)
	for i in range(m):
		if grid[i][n - 1] == 'O':
			Helper(grid, i, 0)
	for i in range(n):
		if grid[0][i] == 'O':
			Helper(grid, 0, i)
	for i in range(n):
		if grid[m - 1][0] == 'O':
			Helper(grid, m - 1, 0)
	for i in range(m):
		for j in range(n):
			if grid[i][j] == -1:
				grid[i][j] = 'O'
			elif grid[i][j] == 'O':
				grid[i][j] = "X"
	return grid 

def WordSearch(grid, word):
	def Helper(grid, word, count, i, j):
		if count == len(word) : return True 
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[0]:
			return False 
		grid[i][j] = - 1
		return Helper(grid, word, count + 1, i + 1, j) or Helper(grid, word, count + 1, i, j + 1) \
		 	   or Helper(grid, word, count + 1, i - 1, j) or Helper(grid, word, count + 1, i, j - 1)

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and Helper(grid, word, 0, i, j):
				return True 
	return False 

def SubsIslands(grid, another):
	def Helper(grid, i, j, set):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return 
		s.add((i, j))
		grid[i][j] = -1
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				s = set()
				Helper(grid, i, j, s)

	count = 0
	for i in range(len(another)):
		for j in range(len(another[0])):
			if another[i][j] == 1 :
				res = set()
				Helper(another, i, j, res)
				if all(grid[x][y] == -1 for x, y in res):
					count += 1
	return count 

def RottingOranges(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q, minutes, fresh = 0, 0, 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] ==2 :
				q.append((i, j))
			elif grid[i][j] == 1 :
				fresh += 1
	while q and fresh:
		minutes += 1
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 2 or grid[x][y] == 0:
					continue 
				grid[x][y] = 2 
				fresh -= 1
				q.append((x, y))
	return minutes 

def GridIlluinations(m, lamps, que):
	def Helper(grid, i, j, dx, dy):
		grid[i][j] = 1 
		x = i + dx 
		y = j + dy 
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : return 
		Helper(grid, x, y, dx, dy)

	def Helper2(grid, i, j):
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : continue 
			grid[x][y] = 0 
		return 

	if not m : raise ValueError
	grid = [[0 for _ in range(m)] for _ in range(m)]
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
	for i, j in lamps:
		grid[i][j] = 0 
		for dx, dy in neighbours:
			x = i + dx
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : continue 
			Helper(grid, x, y, dx, dy)
		grid[i][j] = 1 

	res = []
	for i, j in que:
		if grid[i][j] == 1 : res.append(1)
		else : res.append(0)
		Helper2(grid, i, j)
	return res 

def GatesAndbrindges(grid):
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
			if grid[i][j] == 0:
				Helper(grid, i, j, 0)
	return grid 

def PacificAtlantic(grid):
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
				res.append((i, j))
	return res 

def PerimeterIsland(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	area = 0
	connected = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1 : 
				area += 1
				if i and grid[i - 1][j] == 1 : connected += 1
				if j and grid[i][j - 1] == 1 : connected += 1
	return area * 4 - connected * 2 

def FirstOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return - 1
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
		if idx != -1 : break 
	return i, idx 
	
def MaxOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return - 1
		while h >= l :
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0 ):
				return mid 
			if arr[mid] == 0 : l = mid + 1
			else : h = mid - 1
		return - 1

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	res = 0 
	for i in range(m):
		idx = Helper(grid[i], 0, n - 1)
		if idx != - 1 :
			count = n - idx 
			if res < count:
				res = count 
				row = i 
	return res, row 

def OutOfBounds(m, n, i, j, moves):
	if not m or not n : raise ValueError
	dp = [[[-1]*(moves + 1) for _ in range(n)] for _ in range(m)]
	def Helper(i, j, moves):
		if i < 0 or i >= m or j < 0 or j >= n : return 1 
		if moves < 0 : return 0 
		if dp[i][j][moves] : return d[i][j][moves]
		Phi = Helper(i + 1, j, moves - 1)
		Psi = Helper(i, j + 1, moves - 1)
		Mu  = Helper(i, j - 1, moves - 1)
		Nu  = Helper(i - 1, j, moves - 1)
		dp[i][j][moves] = (Phi + Psi + Mu + Nu ) % ((10**9) + 7)
		return dp[i][j][moves]

	return Helper(m, n, moves)

def KnightProbability(m, n, i, j, moves):
	if not m or not n : raise ValueError
	def Helper(i, j, moves):
		if i < 0 or i >= m or j < 0 or j >= n : return 0 
		if moves == 0 : return 1 
		return (Helper(i + 1, j + 2, moves - 1) + \
				Helper(i + 1, j - 2, moves - 1) + \
				Helper(i - 1, j + 2, moves - 1) + \
				Helper(i - 1, j - 2, moves - 1) + \
				Helper(i + 2, j + 1, moves - 1) + \
				Helper(i + 2, j - 1, moves - 1) + \
				Helper(i - 2, j + 1, moves - 1) + \
				Helper(i - 2, j - 1, moves - 1)) / 8

	return Helper(i, j, moves)

def GridConvolutions(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0))
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

def MineSweeper(grid, click):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 'E':
			return 
		count = 0 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 'M':
				continue
			count += 1
		if count :
			grid[i][j] = count 
		else:
			grid[i][j] = 'B'
			for dx, dy in neighbours:
				Helper(grid, i + dx, j + dy)

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	i, j = click
	if grid[i][j] == 'M':
		grid[i][j] = 'X'
	elif grid[i][j] == 'E':
		Helper(grid, i, j)
	return grid 

n = 4 
def Nqueen():
	def Nqueenu(b, col):
		if col >= n: 
			return True 
		for i in range(n):
			if issafe(b, i, col):
				b[i][col] = 1 
				if Nqueenu(b, col + 1):
					return True 
				b[i][col] = 0 
		return False 

	def issafe(b, row, col):
		for i in range(col):
			if b[row][i] == 1 : 
				return False 
		for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
			if b[i][j] == 1: 
				return False 
		for i, j in zip(range(row, n), range(col, -1, -1)):
			if b[i][j] == 1 : 
				return False 
		return True 

	b = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	if Nqueenu(b, 0) == False:
		return False 
	printsol(b)

def printsol(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = " ")
		print("")

def MazSolver(maze):
	sol = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	def MazSolveru(maze, x, y):
		if x == n - 1 and y == n - 1 and maze[x][y] == 1 : 
			sol[x][y] = 1
			return True 
		if issafe(maze, x, y):
			if sol[x][y] == 1 : 
				return False 
			sol[x][y] = 1 
			if MazSolveru(maze, x + 1, y):
				return True 
			if MazSolveru(maze, x, y + 1):
				return True 
			if MazSolveru(maze, x - 1, y):
				return True 
			if MazSolveru(maze, x, y - 1):
				return True 
			sol[x][y] = 0 
		return False 

	def issafe(maze, x, y):
		if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] != 1:
			return False 
		return True 

	if MazSolveru(maze, 0, 0) == False:
		return False 
	printsol(sol)

def GoldMax(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	sol = [[0 for _ in range(n)] for _ in range(m)]
	for col in range(n - 1, -1, -1):
		for row in range(m):
			if col == n - 1 : 
				right = 0 
			else:
				right = sol[row][col + 1]
			if col == n -1 or row == m - 1 :
				right_down = 0 
			else:
				right_down = sol[row + 1][col + 1]
			if col == n - 1 or row == 0 :
				right_up = 0 
			else:
				right_up = sol[row - 1][col + 1]
			sol[row][col] = max(right, right_up, right_down) + grid[row][col]

	res = float('-inf')
	for i in range(m):
		res = max(res, sol[i][0])
	return  res 

def GoldMine(grid):
	def Helper(grid, i, j, gold):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] <= 0 :
			return gold 
		tmp = grid[i][j]
		gold += tmp 
		grid[i][j] = -1 
		res = 0 
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

def Spiral(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	Top, Bottom, Left, Right, res, maxRes = 0, m - 1, 0, n - 1, [], m * n 
	while len(arr) < maxRes:
		for i in range(Left, Right + 1):
			if len(res) < maxRes :
				res.append(grid[Top][i])
		Top += 1

		for i in range(Top, Bottom + 1):
			if len(res) < maxRes :
				res.append(grid[i][Right])
		Right -= 1

		for i in range(Right, Left - 1, -1):
			if len(res) < maxRes :
				res.append(grid[Bottom][i])

		Bottom -= 1

		for i in range(Bottom, Top - 1, -1):
			if len(res) < maxRes :
				res.append(grid[i][Left])
		Left += 1

	return res 

def SudokuSolver(grid):
	def rowCheck(grid):
		for row in grid:
			if not Helper(row):
				return False 
		return True 

	def colCheck(grid):
		for col in zip(*grid):
			if not Helper(col):
				return False 
		return True 

	def BoxCheck(grid):
		for i in (0, 3, 6):
			for j in (0, 3, 6):
				box = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
				if not Helper(box):
					return False 
		return True 

	def Helper(arr):
		tmp = []
		for num in arr:
			if num != '.' : tmp.append(num)
		return tmp == arr

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	if rowCheck(grid) and colCheck(grid) and BoxCheck(grid):
		return True 
	return False 


def Reshape(grid, r, c):
	m, n = len(grid), len(grid[0])
	if not m or not n or m * n != r*c: raise ValueError 
	arr = [num for row in grid for num in row]
	x = 0 
	new_grid = [[0 for _ in range(c)] for _ in range(r)]
	for i in range(r):
		for j in range(c):
			new_grid[i][j] = arr[x]
			x += 1

	return new_grid 

def MazimumIncresingSubpath(grid):
	def Helper(dp, i, j):
		if not dp[i][j]:
			Up, Down, Left, Right = 0, 0, 0, 0 
			val = grid[i][j]
			if i and val < grid[i - 1][j]:
				Up = Helper(dp, i - 1, j)
			if i < len(grid) - 1 and val < grid[i + 1][j]:
				Left = Helper(dp, i + 1, j)
			if j  and val < grid[i][j - 1]:
				Right = Helper(dp, i, j - 1)
			if j < len(grid[0]) - 1 and val < grid[i][j + 1]:
				Down = Helper(dp, i, j + 1)
			dp[i][j] = max(Up, Down, Left, Right) + 1
		return dp[i][j]
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	res = 0 
	for i in range(m):
		for j in range(n):
			res = max(res, Helper(dp, i, j))
	return res 


def DungeonGame(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
	dp[m - 1][n], dp[m][n - 1] = 1, 1 
	for i in range(m - 1, -1, -1):
		for j in range(n - 1, -1, -1):
			dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - grid[i][j], 1)
	return dp[0][0]

def ExitMaze(grid, start):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	i, j = start
	q = [(i, j)]
	moves = 0 
	grid[i][j] = '+'
	while q :
		moves +=1 
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '+':
					continue 
				if x == 0 or x == m - 1 or y == 0 or y == n - 1 : return moves 
				grid[x][y] = '+'
				q.append((x, y))
	return -1 

def ShortestPathToGetKeys(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	key_count = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == '@':
				start = (i, j)
			elif grid[i][j] in 'abcdef':
				key_count += 1
	i, j = start
	q = [(i, j, '')]
	moves = 0 
	seen = set()
	while q :
		moves += 1 
		for _ in range(len(q)):
			i, j, key = q.pop(0)
			if (i, j, key) in seen : continue 
			if len(key) == key_count : return moves - 1 
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
				if val in '.@':
					q.append((x, y, key))
				if val in 'abcedf':
					if val not in key:
						q.append((x, y, key + val))
					else:
						q.append((x, y, key))
	return - 1

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
	for i in d:
		if i % 2 == 0 : [res.append(x) for x in d[i][::-1]]
		else : [res.append(x) for x in d[i]]
	return res 

def DiagonalTraversalBrokenGrid(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	res = []
	for i, row in enumerate(grid):
		for j, num in enumerate(row):
			if i + j <= len(res):
				res.append([])
			res[i + j].append(num)
	ans = []
	for arr in res:
		for num in reversed(arr):
			ans.append(num)
	return ans 

def EscapeGrid(monsters, target):
	if not target : return ValueError 
	if not monsters : return True
	i, j = target 
	d = abs(i) + abs(j)
	if all(d < abs(i - a) + abs(b - j) for a, b in monsters):
		return True 
	return False

def MaximumDistanceFromLand(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q = []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1 : q.append((i, j))
	if not q or len(q) == m * n : return -1
	dist = 0 
	while q:
		dist += 1 
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 0 :
					continue 
				grid[x][y]  = 1
				q.append((x, y))
	return dist - 1 

def MoveRobot(sti):
	if not sti : raise ValueError 
	x, y, dx, dy = 0, 0, 0, 1 
	for char in sti:
		if char == 'G' : x, y = x + dx, y + dy 
		if char == 'L' : dx, dy = -dy, dx 
		if char == 'R' : dx, dy = dy, -dx 
	return (x, y) == (0, 0) or (dx, dy) != (0, 1)

def KnightDialer(n):
	if not n : raise ValueError 
	x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
	for _ in range(n - 1):
		x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = \
		x4 + x6, \
		x6 + x8, \
		x7 + x9, \
		x8 + x4, \
		x0 + x9 + x3, \
		0, \
		x7 + x1 + x0, \
		x2 + x6, \
		x1 + x3, \
		x2 + x4 
	return (x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) % ((10**9) + 7)

def ColorGraph(rows):
	if not rows : raise ValueError 
	a121, a123 = 6, 6 
	for _ in range(rows - 1):
		a121, a123 = (3 * a121) +( 2 * a123), (2 * a121) + (2 * a123) 
	return (a121 + a123) % ((10**9) + 7)







