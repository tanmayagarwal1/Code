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
			if grid[i][j] == 1:
				count += Helper(grid, i, j)
	return count 

def CounIsalands(grid):
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
	if m == 0 or n == 0 : return - 1
	grid, q = [[int(grid[i][j]) for j in range(n)] for i in range(m)], []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				x = Helper(grid, i, j)
				q.append(x)
	return q 

def WordSearch(grid, word):
	def Helper(grid, word, i, j, count):
		if count == len(word):
			return True 
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[count]:
			return False 
		grid[i][j] = - 1
		Boolean = Helper(grid, word, i + 1, j, count + 1) or \
				  Helper(grid, word, i, j + 1, count + 1) or \
				  Helper(grid, word, i, j - 1, count + 1) or \
				  Helper(grid, word, i - 1, j, count + 1) 
		return Boolean

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return - 1
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and Helper(grid, word, i, j, 0):
				return True 
	return False 

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
		if grid[i][0] == 'O':
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
			if grid[i][j] == -1:
				grid[i][j] = "O"
			elif grid[i][j] == "O":
				grid[i][j] = "X"
	return grid 

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
	if m == 0 or n == 0 :
		raise ValueError
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
				fresh -=1 
				rotten.append((x, y))
	return minutes 

def FloodFill(grid, sr, sc, new):
	def Helper(grid, i, j, old, new):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != old:
			return 
		grid[i][j] = new 
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, old, new)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	Helper(grid, sr, sc, grid[sr][sc], new)
	return grid 

def FloodFillBfs(grid, sr, sc, new):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	old = grid[sr][sc]
	q = [(sr, sc)]
	while q:
		i, j = q.pop(0)
		grid[i][j] = new 
		neighbours = ((0, 1), (1, 0), (-1, 0), (0, -1))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != old:
				continue
			q.append((x, y))
	return grid 

def GridIlluminations(n, lamps, queries):
	def Helper(grid, i, j, dx, dy):
		grid[i][j] = 1 
		x = i + dx 
		y = j + dy 
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
			return 
		Helper(grid, x, y, dx, dy)

	def HelperOff(grid, i, j):
		grid[i][j] = 0 
		neighbours = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
				continue
			grid[x][y] = 0 
		return 

	if not n : raise ValueError
	grid = [[0 for _ in range(n)] for _ in range(n)]
	neighbours = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
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
		if grid[i][j]: res.append(1)
		else: res.append(0)
		HelperOff(grid, i, j)
	return res 

def Convolutions(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : return - 1
	neighbours = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, 0))
	for i in range(m):
		for j in range(n):
			temp = []
			for dx, dy in neighbours:
				x = i + dx
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
					continue 
				temp.append(grid[x][y])
			grid[i][j] = sum(temp)//len(temp)
	return grid 

def SearchSortedMatrix(grid, target):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	i, j = 0, n - 1
	while i < m and j >= 0 :
		if grid[i][j] > target:
			j -= 1
		elif grid[i][j] < target:
			i += 1
		elif grid[i][j] == target:
			return i, j 
	return -1 

def FirstOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return - 1
		while h >= l:
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
				return mid 
			elif arr[mid] == 0:
				l = mid + 1
			else:
				h = mid - 1
		return -1 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	l, h = 0, n - 1
	for i in range(m):
		idx = Helper(grid[i], 0, n - 1)
		if idx != -1 : break 
	return i, idx 

def MaxOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return - 1
		while h >= l:
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid -1] == 0 or mid == 0 ):
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
		if idx != -1:
			count = n - idx
			if res < count :
				res = count 
				my_idx = i 
	return res, my_idx

def Spiral(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	Top, Bottom, Left, Right = 0, m - 1, 0, n - 1
	arr, max_arr = [], m * n 
	while len(arr) < max_arr:
		for i in range(Left, Right + 1):
			if len(arr) < max_arr:
				arr.append(grid[Top][i])
		Top += 1

		for i in range(Top, Bottom + 1):
			if len(arr) < max_arr:
				arr.append(grid[i][Right])
		Right -= 1

		for i in range(Right, Left - 1, - 1):
			if len(arr) < max_arr:
				arr.append(grid[Bottom][i])
		Bottom -= 1

		for i in range(Bottom, Top - 1, - 1):
			if len(arr) < max_arr:
				arr.append(grid[i][Left])
		Left += 1

	return arr 

def Rotation(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	grid.reverse()
	for i in range(m):
		for j in range(i + 1, n):
			grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
	return grid 

def Diagonal(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	d = {}
	for i in range(m):
		for j in range(len(grid[i])):
			if i + j in d:
				d[i + j].append(grid[i][j])
			else:
				d[i + j] = [grid[i][j]]

	res = []
	for i in d.keys():
		if i & 1 : [res.append(x) for x in d[i]]
		else : [res.append(x) for x in d[i][::-1]]
	return res 


def Nqueen():
	b = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
	if Nqueenu(b, 0) == False :
		return False 
	printgrid(b)

def Nqueenu(b, col):
	if col >= n :
		return True 
	for i in range(n):
		if Issafe(grid, i, col):
			b[i][col] = 1 
			if Nqueenu(b, col + 1):
				return True 
			b[i][col] = 0 
	return False 

def Issafe(b, row, col):
	for i in range(col):
		if b[row][i] == 1:
			return False 
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if b[i][j] == 1:
			return False 
	for i, j in zip(range(row, n), range(col, -1, -1)):
		return False 
	return True 

def Mazesolver(maze):
	sol = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
	if Mazesolveru(maze, 0, 0, sol) == False:
		return False 
	return True 

def Mazesolveru(maze, x, y, sol):
	if x == n - 1 and y == n - 1 and maze[x][y] == 1:
		sol[x][y] = 1
		return True 
	if issafe(maze, x, y):
		if sol[x][y] == 1:
			return False 
		sol[x][y] = 1
		if Mazesolveru(maze, x + 1, y, sol):
			return True  
		if Mazesolveru(maze, x, y + 1, sol):
			return True  
		if Mazesolveru(maze, x - 1, y, sol):
			return True  
		if Mazesolveru(maze, x, y - 1, sol):
			return True  
		sol[x][y] = 0 
	return False 

def issafe(maze, i, j):
	if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[0]) or maze[i][j] != 1:
		return False 
	return True 

def goldmax(grid):
	m, n = len(grid), len(grid[0])
	gt = [[0 for _ in range(n)] for _ in range(m)]
	if m == 0 or n == 0 : raise ValueError
	for col in range(n -1, -1, -1):
		for row in range(m):
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
			gt[row][col] = max(right, right_up, right_down) + grid[row][col]
	res = gt[0][0]
	for i in range(m):
		res = max(res, gt[i][0])
	return res 

def MineSweeper(grid, click):
	def Helper(grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "E":
			return 
		count = 0 
		neighbours = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
		for dx, dy in neighbours:
			x = i + dx 
			y = j + dy 
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "M":
				continue
			if grid[x][y] == "M":
				count += 1
		if count :
			grid[i][j] = count 
		else:
			grid[i][j] = "B"
			for dx, dy in neighbours:
				Helper(grid, i + dx, j + dy)
			#return 

	i, j = click 
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	if grid[i][j] == 'M':
		grid[i][j] = 'X'
	elif grid[i][j] == "E":
		Helper(grid, i, j)
	return grid 

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
			if grid[i][j] == 0:
				Helper(grid, i, j, 0)
	return grid 

def MergeIslands(grid, gridd):
	def Helper(grid, i, j, visited):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1 :
			return 
		grid[i][j] = - 1
		visited.add((i, j))
		neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
		for dx, dy in neighbours:
			Helper(grid, i + dx, j + dy, visited)
		return 

	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 :
		raise ValueError
	tmp = set()
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				Helper(grid, i, j, tmp)
	res = 0 
	for i in range(len(gridd)):
		for j in range(len(gridd[0])):
			if gridd[i][j] == 1:
				seen = set()
				Helper(gridd, i, j, seen)
				if all(grid[a][b] == -1 for a, b in seen):
					res += 1
	return res 






# Mine Sweeper 

grid = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
print(MineSweeper(grid, click))


# Sub Islands - Grid Matching 
grid = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
gridd = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(MergeIslands(grid, gridd))





