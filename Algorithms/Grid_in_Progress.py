def NumIslands(grid):
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
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1 :
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
		if grid[i][0] == "O":
			Helper(grid, i, 0)
	for i in range(m):
		if grid[i][n - 1] == 'O':
			Helper(grid, i, n - 1)
	for i in range(n):
		if grid[0][i] == 'O':
			Helper(grid, 0, i)
	for i in range(n):
		if grid[m - 1][i] == 'O':
			Helper(grid, m - 1, i)
	for i in range(m):
		for j in range(n):
			if grid[i][j] == - 1:
				grid[i][j] = "O"
			elif grid[i][j] == "O":
				grid[i][j] = "X"
	return grid 

def WordSearch(grid, word):
	def Helper(grid, word, count, i, j):
		if count == len(word) : return True 
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[count]:
			return False 
		grid[i][j] = - 1
		return Helper(grid, word, count + 1, i + 1, j) or \
			   Helper(grid, word, count + 1, i - 1, j) or \
			   Helper(grid, word, count + 1, i, j + 1) or \
			   Helper(grid, word, count + 1, i, j - 1) 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and Helper(grid, word, 0, i, j):
				return True 
	return False 

def WallsAndGates(grid):
	def Helper(grid, count, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] < count:
			return 
		grid[i][j] = count 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, count + 1, i + dx, j + dy)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 0:
				Helper(grid, 0, i, j)
	return grid 

def RottenOranges(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	q, fresh, min = [], 0, 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 2:
				q.append((i, j))
			elif grid[i][j] == 1 : 
				fresh += 1
	while q and fresh : 
		min += 1
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 2 or grid[x][y] == 0 : 
					continue 
				q.append((x, y))
				fresh -= 1 
				grid[x][y] = 2 
	return min 

def GridIlluminations(n, lights, queries):
	def Helper(grid, i, j, dx, dy):
		grid[i][j] = 1 
		x = i + dx 
		y = j + dy 
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : return 
		Helper(grid, x, y, dx, dy)

	def Helper_(grid, i, j):
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : continue 
			grid[x][y] = 0 
		return 

	if n == 0 : raise ValueError
	grid = [[0 for _ in range(n)] for _ in range(n)]
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
	for i, j in lights:
		grid[i][j] = 0 
		for dx, dy in neighbours:
			x = i + dx
			y = j + dy 
			if x < 0 or x >= len(grid) or j < 0 or j >= len(grid[0]) : continue 
			Helper(grid, i, j, dx, dy)
		grid[i][j] = 1 
	
	res = []
	for i, j in queries :
		if grid[i][j] == 0 : res.append(0)
		elif grid[i][j] == 1 : res.append(1)
		Helper_(grid, i, j)
	return res 

def GridConvolutions(grid):
	m, n = len(grid), len(grid[0])
	neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0))
	if m == 0 or n == 0 : raise ValueError
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

def FirstOne(grid):
	def Helper(arr, l, h):
		if h < l : return -1 
		while h >= l :
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0 ):
				return mid 
			if arr[mid] == 0 : l = mid + 1
			else : h = mid - 1
		return - 1

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		idx = Helper(grid[i], 0, n - 1)
		if idx != - 1 : 
			break 
	return i, idx 

def DiagonalTraversal(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	d = {}
	for i in range(m):
		for j in range(n):
			if i + j in d :
				d[i + j].append(grid[i][j])
			else:
				d[i + j] = [grid[i][j]]
	res = []
	for key in d.keys():
		if key % 2 == 0 : [res.append(x) for x in d[key][::-1]]
		else: [res.append(x) for x in d[key]]
	return res 

def MineSweeper(grid, click):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 'E':
			return 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
		count = 0 
		for dx, dy in neighbours:
			x = i + dx
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "M" : continue 
			count += 1
		if count :
			grid[i][j] = count 
		else:
			grid[i][j] = "B"
			for dx, dy in neighbours:
				Helper(grid, i + dx, j + dy)

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	i, j = click 
	if grid[i][j] == 'M':
		grid[i][j] = 'X'
	else:
		Helper(grid, i, j)
	return grid 

def ExitMaze(grid, start):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	i, j = start
	q = [(i, j)]
	grid[i][j] = '+'
	moves = 0 
	while q:
		moves += 1 
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '+':
					continue 
				if x == 0 or x == m - 1 or y == 0 or y == n - 1  : return moves 
				grid[x][y] = "+"
				q.append((x, y))
	return -1 


def findKeys(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q = []
	keys = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] in 'abcdef':
				keys += 1
			elif grid[i][j] == '@':
				start = (i, j)
	i, j = start
	q.append((i, j, ''))
	moves = 0 
	seen = set()
	while q :
		moves += 1 
		for _ in range(len(q)):
			i, j, key = q.pop(0)
			if (i, j, key) in seen : continue 
			if len(key) == keys : return moves - 1
			seen.add((i, j, key))
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) : continue 
				val = grid[x][y]
				if val in 'ABCDEF' and val.lower() in 'abcdef':
					q.append((x, y, key))
				elif val in '@.':
					q.append((x, y, key))
				else:
					if val in 'abcdef' and val not in key:
						q.append((x, y, key + val))
					else:
						q.append((x, y, key))
	return -1 

def OutOfBounds(m, n, i, j, moves):
	if m == 0 or n == 0 : raise ValueError
	dp = [[[-1]*(moves + 1) for _ in range(n + 1)]for _ in range(m + 1)]
	def Helper(i, j, moves): 
		if i < 0 or i >= m or j < 0 or j >= n : return 1 
		if moves < 0 : return 0
		if dp[m][n][moves] != -1 : return dp[m][n][moves]
		Phi = Helper(i + 1, j, moves - 1)
		Psi = Helper(i, j + 1, moves - 1)
		Mu  = Helper(i, j - 1, moves - 1)
		Nu  = Helper(i - 1, j, moves - 1)
		dp[i][j][moves] = (Phi + Psi + Mu + Nu ) % ((10**9) + 7)
		return dp[i][j][moves]

	return Helper(i, j, moves)


def Resize(grid, r, c):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	if m * n != r * c : return "Not compatible transformation"
	idx = 0 
	arr = [num for num in row for row in grid]
	grid = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(r):
		for j in range(c):
			grid[i][j] = arr[idx]
			idx += 1
	return grid 

def IncreasingSubPath(grid):
	def Helper(grid, i, j):
		if not dp[i][j]:
			val = grid[i][j]
			Phi, Psi, Mu, Nu = 0, 0, 0, 0
			if i and val < grid[i - 1][j]:
				Phi = Helper(grid, i - 1, j)
			if i < m - 1 and val < grid[i + 1][j]:
				Psi = Helper(grid, i + 1, j)
			if j and val < grid[i][j - 1]:
				Mu = Helper(grid, i, j - 1)
			if j < n - 1 and val < grid[i][j + 1]:
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

def SubIslands(grid, gridd):
	def Helper(grid, i, j, s):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1 : 
			return 
		grid[i][j] = -1 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		s.add((i, j))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, s)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				s = set()
				Helper(grid, i, j, s)


	mm, nn = len(gridd), len(gridd[0])
	if mm == 0 or nn == 0 : raise ValueError 
	count = 0 
	for i in range(mm):
		for j in range(nn):
			if gridd[i][j] == 1 : 
				s = set()
				Helper(gridd, i, j, s)
				if all(grid[a][b] == -1 for a, b in s):
					count += 1
	return count 

def MaxDistanceFromLand(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
	if not q or q == m * n : return -1 
	dist = 0 
	while q:
		dist += 1
		for _ in range(len(q)):
			i, j = q.pop(0)
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 0 : continue 
				q.append((x, y))
				grid[x][y] =1 

	return dist -1 

def MoveRobot(sti):
	if not sti : raise ValueError
	x, y, dx, dy = 0, 0, 0, 1 
	for char in sti:
		if char == "G" : x, y = x + dx, y + dy 
		if char == "L" : dx, dy = -dy, dx
		if char == "R" : dx, dy = dy, -dx
	return (x, y) == (0, 0) or (dx, dy) != (0, 1)

def DungeonGame(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
	dp[m - 1][n], dp[n][m  - 1] = 1, 1 
	for i in range(m - 1, -1, -1):
		for j in range(n - 1, -1, -1):
			dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - grid[i][j], 1)
	return dp[0][0]
	
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(IncreasingSubPath(matrix))


