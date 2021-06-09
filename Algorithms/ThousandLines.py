m = n = 4
import numpy as np 
from collections import defaultdict
import heapq
run_max = np.maximum.accumulate
def Unique(sti):
	if len(sti) == 0:
		return -1 
	s = set()
	q = []
	for char in sti:
		if char not in s:
			s.add(char)
		else:
			q.append(char)
	for char in sti:
		if char not in q:
			print(char)

def StartingWith(arr, pattern):
	if len(arr) == 0:
		return - 1
	q = []
	for word in arr:
		count = 0 
		for j in range(len(pattern)):
			if word[j] == pattern[j]:
				count += 1
			else:
				break 
			if len(pattern) == count:
				q.append(word)
	return q 

def License(sti, k):
	if len(sti) == 0:
		return -1 
	sti = ''.join(sti.split('-')).upper()
	i, j, res = 0, len(sti), []
	while j > i :
		if sti[j - k :j] : res.append(sti[j-k:j])
		else: res.append(sti[:j])
		j -= k 
	return '-'.join(res[::-1])

def IsValidPalindrome(sti):
	if len(sti) == 0:
		return 
	sti = ''.join(sti.split(' ')).lower()
	q = []
	for char in sti:
		if char.isalnum():
			q.append(char)
	return q == q[::-1]

def OneSwap(sti):
	if len(sti) == 0:
		return -1 
	i, j = 0, len(sti) - 1
	while j > i:
		if sti[i] == sti[j]:
			i += 1
			j -= 1
		else:
			one, two = sti[i:j], sti[i + 1: j + 1]
			return one == one[::-1] or two == two[::-1]
	return True 

def MinSwap(sti):
	if len(sti) == 0 or not IsValid(sti):
		return -1 
	i, j, swaps = 0, len(sti) - 1, 0 
	sti = [i for i in sti]
	while j > i :
		if sti[i] == sti[j]:
			i += 1
			j -= 1
		else:
			temp = j 
			while temp >= i and sti[temp] != sti[i]:
				temp -= 1
			if i == temp:
				sti[temp], sti[temp + 1] = sti[temp + 1], sti[temp]
				swaps += 1
				continue 
			for x in range(temp, j):
				sti[x], sti[x + 1] = sti[x + 1], sti[x]
				swaps += 1
			i += 1 
			j -= 1
	return swaps 

def IsValid(sti):
	d = dict()
	for char in sti:
		d[char] = d.get(char, 0) + 1
	return len([i for i, j in d.items() if j % 2 != 0]) <= 1

def UniqueLength(arr):
	if len(arr) == 0:
		return -1 
	sol, res = [''], 0
	for word in arr:
		for string in sol:
			temp = word + string 
			if len(temp) == len(set(temp)):
				sol.append(temp)
				res = max(res, len(temp))
	return res 

def FrequencySort(sti):
	if len(sti)  == 0:
		return -1 
	d = dict()
	for char in sti:
		d[char] = d.get(char, 0) + 1
	q = [i for i in d.values()]
	q.sort()
	q, sol = q[::-1], ''
	for i in q:
		for j, k in d.items():
			if i == k :
				sol += j*k
				break 
		del d[j]
	return sol 

def MaxDeletions(sti):
	if len(sti) == 0:
		return -1 
	d = dict()
	for char in sti:
		d[char] = d.get(char, 0) + 1
	exists, count = set(), 0
	for i in d.values():
		while i >= 0 and i in exists:
			i -= 1
			count += 1
		exists.add(i)
	return count 

def Houses(arr, b):
	if len(arr) == 0:
		return -1 
	q = []
	for i in range(len(arr)):
		if arr[i] > b:
			continue
		initial = arr[i]
		count = 1
		for j in range(len(arr)):
			if i == j :
				continue
			if arr[j] + initial <= b:
				initial += arr[j]
				count += 1
		q.append(count)
	res = q[0]
	for i in range(len(q)):
		res = max(res, q[i])
	return res 

def Blocks(arr, interests):
	q  = []
	if len(arr) == 0:
		return -1 
	for i in arr:
		count = 0 
		for j, k in i.items():
			for z in range(len(interests)):
				if j == interests[z] and k == True:
					count += 1
		q.append(count)
	res = q[0]
	for i in range(len(q)):
		res = max(res, q[i])
	return q.index(res) + 1

def PilesHeight(arr):
	arr.sort()
	q, swaps = arr[::-1], 0 
	for i in range(1, len(q)):
		if q[i] != q[i -1]:
			swaps += i 
	return swaps 

def UniqueArray(n):
	return [2 * i - n + 1 for i in range(n)]

def Maxelement(arr, k):
	if len(arr) == 0:
		return - 1
	q, n, res = [], len(arr), 0
	for i in range(k):
		q.append(arr[i])
	for i in range(n - k + 1):
		for j in range(k):
			res = max(res, q[j])
		q.pop(0)
		if i + k < n:
			q.append(arr[i + k])
	return res 

def subarraysum(arr, k):
	if len(arr) == 0:
		return -1 
	windowsum, res = sum(arr[:k]), 0
	for i in range(len(arr) - k):
		windowsum = windowsum - arr[i] + arr[i + k]
		res = max(res, windowsum)
	return res 

def AnagramGroup(arr):
	if len(arr) == 0:
		return -1 
	d = dict()
	for word in arr:
		temp = ''.join(sorted(word))
		if temp in d.keys():
			d[temp].append(word)
		else:
			d[temp] = [word]
	return [i for i in d.values()]


def IsPerfectSqaure(n):
	return int(n**0.5)**2 == n

def IsPerfectCube(n):
	return int(n**(1/3))**3 == n

def ClosestSqaure(n):
	if not n :
		return -1 
	return round(int(n**(1/3))**3)

def LagrangeSquare(n):
	if not n : return -1 
	if int(n ** 0.5)**2 == n : return 1 
	for i in range(int(n ** 0.5)):
		if int((n - i * i)**0.5)**2 == n - i * i:
			return 2 
	while n % 4 == 0:
		n >>= 2 
	if n % 8 == 7:
		return 4 
	return 3 
def ClosestPowerOfTwo(n):
	if not n :
		return - 1
	for i in range(n):
		temp = 2<<i
		if temp > n:
			break 
		res = temp
	return res 

def Lcm(x, y):
	if x < y :
		greater = y 
	else:
		greater = x 
	while True:
		if greater % x == 0 and greater % y == 0:
			lcm = greater
			break 
		greater += 1
	return lcm 

def gcd(x, y):
	while y:
		x, y = y, x % y 
	return x 

def Fib(n):
	x, y = 0, 1 
	if n == 0:
		return x 
	elif n == 1:
		return 1 
	for i in range(2,  n + 1):
		temp = x + y 
		x = y 
		y = temp
	return y 


def HtmlEntitiyParser(sti):
	d = {"&quot;":'"',"&apos;":"'","&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
	keyword, outputs, Mode = [], [], False
	for char in sti:
		if char == '&':
			keyword.append(char)
			Mode = True
		elif Mode:
			keyword.append(char)
			if char == ';':
				keyword = ''.join(keyword)
				outputs.append(d.get(keyword, keyword))
				keyword = []
				Mode = False 
		else:
			outputs.append(char)
	if Mode:
		outputs.append(keyword)
	return ''.join(outputs)

def HtmlTagValidator(sti):
	start, end, br = [], [], ['<', '>', '/']
	for i in range(len(sti)):
		if sti[i] == br[0] and sti[i + 1] != br[2]:
			while sti[i] != br[1]:
				start.append(sti[i])
				i += 1
		elif sti[i] == br[0] and sti[i + 1] == br[2]:
			while sti[i] != br[1]:
				if sti[i] == '/':
					i += 1
					continue
				end.append(sti[i])
				i +=1 
		else:
			i += 1
	return sorted(start) == sorted(end)


def MergeSort(arr):
	if len(arr) > 1:
		mid  = len(arr)//2
		l = arr[:mid]
		r = arr[mid:]
		MergeSort(l)
		MergeSort(r)
		i = j = k = 0
		while i < len(l) and j < len(r):
			if l[i] < r[j]:
				arr[k] = l[i]
				i += 1
			else:
				arr[k] = r[j]
				j += 1
			k += 1
		while i < len(l):
			arr[k] = l[i]
			i += 1
			k += 1
		while j < len(r):
			arr[k] = r[j]
			j += 1
			k += 1

def HeapSort(arr):
	n = len(arr)
	if n == 0:
		return -1 
	for i in range(n - 1//2, -1, -1):
		Heapify(arr, n, i)
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		Heapify(arr, i, 0)

def Heapify(arr, n, i):
	large = i 
	l = 2*i + 1
	r = 2*i + 2
	if l < n and arr[large] < arr[l]:
		large = l 
	if r < n and arr[large] < arr[r]:
		large = r 
	if large != i :
		arr[i], arr[large] = arr[large], arr[i]
		Heapify(arr, n, large)

def QuickSort(arr):
	QuickSortUtil(arr, 0, len(arr) - 1)

def QuickSortUtil(arr, l, h):
	if h > l :
		mid = partition(arr, l, h)
		QuickSortUtil(arr, l, mid - 1)
		QuickSortUtil(arr, mid + 1, h)

def partition(arr, l, h):
	i = l - 1
	pivot = arr[h]
	for j in range(l, h):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[h] = arr[h], arr[i + 1]
	return i + 1

def DutchFlas(arr):
	if len(arr) == 0:
		return -1 
	l, mid, h = 0, 0, len(arr) - 1
	while h >= mid:
		if arr[mid] == 0:
			swap(arr, l, mid)
			l += 1
			mid += 1
		elif arr[mid] == 1:
			mid += 1
		else:
			swap(arr, mid, h)
			h  -=1 
def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

def FloydRabbitHare(arr):
	if len(arr) == 0:
		return -1 
	slow, fast, ans = 0, 0, 0
	while True:
		slow = arr[slow]
		fast = arr[arr[fast]]
		if fast == slow:
			break 
	while ans != slow:
		ans = arr[ans]
		slow = arr[slow]
	return ans 

def BinarySearch(arr, target):
	if len(arr) == 0:
		return -1 
	i, j = 0, len(arr) - 1
	while j >= i :
		mid = (i + j)//2
		if arr[mid] == target:
			return True 
		elif arr[mid] < target:
			i = mid + 1
		else:
			j = mid - 1
	return False

def Nqueen():
	b = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if Nqueenu(b, 0) == False:
		return False 
	printsol(b)

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
		if b[row][i] == 1:
			return False 
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if b[i][j] == 1:
			return False
	for i, j in zip(range(row, n), range(col, -1, -1)):
		if b[i][j] == 1:
			return False
	return True 

def Mazesolver(maze):
	sol = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if Mazesolveru(maze, 0, 0, sol) == False:
		return False 
	printsol(sol)

def Mazesolveru(maze, x, y, sol):
	if x == n - 1 and y == n - 1 and maze[x][y] == 1:
		sol[x][y] = 1
		return True 
	if issafemaze(maze, x, y):
		if sol[x][y] == 1:
			return False
		sol[x][y] = 1
		if Mazesolveru(maze, x + 1, y, sol):
			return True 
		if Mazesolveru(maze, x, y + 1, sol):
			return True
		if Mazesolveru(maze, x, y - 1, sol):
			return True
		if Mazesolveru(maze, x - 1, y, sol):
			return True
		sol[x][y] = 0 
	return False

def issafemaze(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
		return False 
	return True 

def goldmax(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0:
		return -1 
	gt = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for col in range(n - 1, -1, -1):
		for row in range(m):
			if col == n - 1:
				right = 0 
			else:
				right = gt[row][col + 1]
			if col == n- 1 or row == n- 1:
				right_down = 0 
			else:
				right_down = gt[row + 1][col + 1]
			if col == n - 1 or row == 0:
				right_up = 0 
			else:
				right_up = gt[row - 1][col + 1]
			gt[row][col] = grid[row][col] + max(right_up, right_down, right)
	res = gt[0][0]
	for i in range(m):
		res = max(res, gt[i][0])
	return res 

def printsol(b):
	for i in range(m):
		for j in range(n):
			print(b[i][j], end = ' ')
		print()

def Lcs(x, y):
	m = len(x)
	n = len(y)
	if m == 0 or n == 0:
		return -1 
	dp = [[0 for _ in range(n + 1)] for _ in range(m +1)]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i -1] == y[j - 1]:
				dp[i][j] = dp[i-1][j - 1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
	return dp[m][n]

def UniquePaths(m, n):
	if m == 0 or n == 0:
		return -1 
	dp = [[1 for _ in range(n)] for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
	return dp[m - 1][n - 1]

def UniquePaths2(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return - 1
	dp = [[0 for _ in range(n)]for _ in range(m)]
	if not grid[0][0] : dp[0][0] = 1
	for i in range(1, m):
		if not grid[i][0]:
			dp[i][0] = 1
	for i in range(1, n):
		if not grid[0][i]:
			dp[0][i] = 1 
	for i in range(1, m):
		for j in range(1, n):
			if grid[i][j]:
				continue
			dp[i][j] = dp[i-1][j] + dp[i][j -1]
	return dp[m - 1][n - 1]

def MaximumCostPath(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return -1 
	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[0][0] = grid[0][0]
	for i in range(1, m):
		dp[i][0] = dp[i- 1][0] + grid[i][0]
	for i in range(1, n):
		dp[0][i] = dp[0][i - 1] + grid[0][i]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = min(dp[i][j] + dp[i- 1][j], dp[i][j] + dp[i][j-1]) + grid[i][j]
	return dp[m-1][n - 1]

def regularexpression(sti, pattern):
	m = len(sti)
	n = len(pattern)
	if m == 0 or n == 0:
		return -1 
	dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
	dp[0][0] = True
	for i in range(1, n):
		if pattern[i - 1] == '*':
			dp[0][i] = dp[0][i - 2]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if sti[i - 1] == pattern[j - 1] or pattern[j -1] == '.':
				dp[i][j] = dp[i -1][j -1 ]
			elif pattern[j - 1] == '*':
				dp[i][j] = dp[i][j - 2]
				if sti[i - 1] == pattern[j -2 ] or pattern[j - 2] == '.':
					dp[i][j] = dp[i- 1][j]
	return dp[m][n]

def eggs_max(f, n):
	dp = [[0 for _ in range(n + 1)] for _ in range(f +1)]
	for i in range(1, f + 1):
		for j in range(1, n + 1):
			dp[i][j] = dp[i-1][j -1 ] + dp[i - 1][j] + 1
		if dp[i][j] >= f: return i 

def water_collector(height):
	a = np.array(height)
	global_max = np.argmax(a)
	return np.sum(run_max(a[:global_max]) - a[:global_max], dtype = np.int64) + \
			np.sum(run_max(a[:global_max:-1]) - a[:global_max : -1], dtype = np.int64)

def TrainTix(days, cost):
	dp = [-1 for _ in range(366)]
	dp[0] = 0 
	for day in days:
		dp[day] = 0 
	for i in range(1, 366):
		if dp[i] == -1:
			dp[i] = dp[i- 1]
		else:
			dp[i] = min(dp[i -1] + cost[0], dp[max(i - 7, 0)] + cost[1], dp[max(i - 30, 0)] + cost[2])
	return dp[365]

def CoinChange(coins, ammount):
	dp = [float('inf') for _ in range(ammount + 1)]
	dp[0] = 0 
	for i in range(1, ammount + 1):
		for coin in coins:
			if i - coin >= 0:
				dp[i]  = min(dp[i], dp[i - coin] + 1)
	return dp[ammount]

def NumIslands(grid):
	m = len(grid)
	n = len(grid[0])
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
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
		return 0 
	grid[i][j] = -1
	neighbours = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbours:
		HelperIsland(grid, i + dx, j + dy)
	return 1 

def WordSearch(grid, word):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return - 1
	for i in range(m):
		for j in range(n):
			if grid[i][j] == word[0] and HelperWord(grid, word, i, j, 0):
				return True 
	return False 

def HelperWord(grid, word, i, j, count):
	if count == len(word):
		return True
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[count]:
		return False 
	grid[i][j] = -1
	Boolean = HelperWord(grid, word, i + 1, j, count + 1) or \
			  HelperWord(grid, word, i, j + 1, count + 1) or \
			  HelperWord(grid, word, i, j - 1, count + 1) or \
			  HelperWord(grid, word, i - 1, j, count + 1) 
	return Boolean

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
				grid[i][j] = "O"
			elif grid[i][j] == "O":
				grid[i][j] = 'X'
	printgrid(grid)

def HelperSurround(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "O":
		return 
	grid[i][j] = -1
	neighbours = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbours:
		HelperIsland(grid, i + dx, j + dy)
	return 

def CountIsland(grid):
	m = len(grid)
	n = len(grid[0])
	if m == 0 or n == 0:
		return -1 
	grid = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
	q = []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				x = HelperCount(grid, i, j, 0)
				q.append(x)
	return q

def HelperCount(grid, i, j, count):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
		return count 
	grid[i][j] = -1
	phi = HelperCount(grid, i + 1, j, count + 1)
	psi = HelperCount(grid, i, j + 1, count + 1)
	mu  = HelperCount(grid, i, j - 1, count + 1)
	nu  = HelperCount(grid, i - 1, j, count + 1)
	return max(phi, psi, mu, nu)

def PacificAtlantic(grid):
	m, n, res = len(grid), len(grid[0]), []
	if m == 0 or n == 0:
		return - 1
	pacific_visited = [[False for _ in range(n)] for _ in range(m)]
	atlantic_visited = [[False for _ in range(n)] for _ in range(m)]
	for i in range(m):
		HelperOcean(grid, i, 0, pacific_visited)
		HelperOcean(grid, i, n - 1, atlantic_visited)
	for i in range(n):
		HelperOcean(grid, 0, i, pacific_visited)
		HelperOcean(grid, m - 1, 0, atlantic_visited)
	for i in range(m):
		for j in range(n):
			if pacific_visited[i][j] and atlantic_visited[i][j]:
				res.append([i, j])
	return res 

def HelperOcean(grid, i, j, visited):
	visited[i][j] = True 
	neighbours = ((0,1), (0,-1), (1,0), (-1,0))
	for dx, dy in neighbours:
		x = i + dx 
		y = j + dy
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[i][j] > grid[x][y]:
			continue 
		HelperOcean(grid, x, y, visited)

def Subsets(arr):
	return [[arr[i] for i in range(len(arr)) if bit & 1<<i != 0] for bit in range(1 <<len(arr))]

def Subsets2(arr):
	if len(arr) == 0:
		return -1 
	sol = [[]]
	for i in arr:
		sol += [current + [i] for current in sol]
	return sol 

def Permutations(arr):
	if len(arr) == 0:
		return -1 
	res = []
	Permutate(arr, [], res)
	return res 

def Permutate(arr, path, res):
	if not arr:
		res.append(path)
	for i in range(len(arr)):
		Permutate(arr[:i] + arr[i + 1:], path + [arr[i]], res)

def Partitions(O, P):
	if P == 1:
		return 1 
	elif P == 0 or O < 0:
		return 0 
	else:
		return Partitions(O - P, P) + Partitions(O, P - 1)

def Combinations(arr, target):
	if not arr:
		return -1 
	res = []
	Combinator(arr, 0, target, [], res)
	return res 

def Combinator(arr, index, target, path, res):
	if target < 0:
		return 
	elif target == 0:
		res.append(path)
		return 
	for i in range(index, len(arr)):
		Combinator(arr, i, target - arr[i], path + [arr[i]], res)

def CheapestFlights(Flights, src, dst, stops):
	graph, q = defaultdict(list), []
	for s, d, w in Flights: graph[s].append((d, w))
	heapq.heappush(q, (0, src, stops + 1))
	while q:
		price, city, k = heapq.heappop(q)
		if city == dst: return price 
		if k > 0 :
			for new_city, new_price in graph[city]:
				heapq.heappush(q, (price + new_price, new_city, k - 1))
	return -1 

class graph:
	def __init__(self,v):
		self.v  = v
		self.graph = [[0 for _ in range(self.v)] for _ in range(self.v)]
	def ShortestPath(self, s):
		dist = [float('inf')]*self.v
		visited = [False]*self.v 
		dist[s] = 0 
		for _ in range(self.v):
			u = self.shortestvertex(dist, visited)
			visited[u] = True
			for i in range(self.v):
				if self.graph[u][i] and visited[i] == False and dist[i] > dist[u] + self.graph[u][i]:
					dist[i] = dist[u] + self.graph[u][i]
		self.printgrid(dist)

	def shortestvertex(self, dist, visited):
		min = float('inf')
		for i in range(self.v):
			if dist[i] < min and visited[i] == False:
				min = dist[i]
				min_index = i 
		return min_index

	def printgrid(self, dist):
		for i in range(self.v):
			print(f"{i} : {dist[i]}")

def printgrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end = ' ')
		print()

class graph1:
	def __init__(self):
		self.graph = defaultdict(list)
	def append(self, s, d):
		self.graph[s].append(d)
	def bfs(self, s):
		visited = [False]*1000
		q = []
		q.append(s)
		visited[s] = True 
		while q:
			s = q.pop(0)
			print(s)
			for i in self.graph[s]:
				if visited[i] == False:
					q.append(i)
					visited[i] = True 
	def dfs(self, v):
		s = set()
		self.dfsu(s, v)
	def dfsu(self, s, v):
		s.add(v)
		print(v)
		for i in self.graph[v]:
			if i not in s:
				self.dfsu(s, i)

def Spiral(grid):
	if not grid:
		return - 1
	Top, Bottom, Left, Right, arr, max_arr = 0, len(grid) - 1, 0, len(grid[0]) - 1, [], len(grid) * len(grid[0])
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

		for i in range(Bottom, Top - 1, -1):
			if len(arr) < max_arr:
				arr.append(grid[i][Left])
		Left += 1

	return arr 

def ClosestTime(time):
	h, m = time.split(':')
	m = m[0:2]
	minutes = int(h)*60 + int(m)
	for i in range(minutes + 1, minutes + 1441):
		temp = i % 1440
		h, m = temp//60, temp % 60 
		Time = "{:02d}:{:02d}".format(h, m)
		if set(Time) <= set(time):
			if int(Time[0:2]) < 12:
				return Time + ' AM'
			else:
				return Time + ' PM'


class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def push(root, data):
	if not root:
		return node(data)
	else:
		if root.data < data:
			root.right = push(root.right, data)
		elif root.data > data:
			root.left = push(root.left, data)
		return root 

def show(root):
	if root:
		show(root.left)
		print(root.data)
		show(root.right)
	else:
		return 

def leaf(root):
	if not root:
		return 0 
	if not root.left and not root.right:
		return 1 
	else:
		return leaf(root.left) + leaf(root.right)

def sum(root):
	if not root:
		return 0 
	else:
		return root.data + sum(root.left) + sum(root.right)

def height(root):
	if not root:
		return 0 
	else:
		l = height(root.left)
		r = height(root.right)
		if l < r:
			return r + 1
		else:
			return l + 1
def subtree(root):
	if not root:
		return 0 
	res = [-9999]
	subtreeu(root, res)
	return res[0]

def subtreeu(root, res):
	if not root:
		return 0 
	else:
		cur = root.data + subtreeu(root.left, res) + subtreeu(root.right, res)
		res[0] = max(res[0], cur)
		return cur 

def levelorder(root):
	if not root:
		return 
	else:
		h = height(root)
		for i in range(h):
			levelorderu(root, i)

def levelorderu(root, l):
	if not root:
		return 
	if l == 0 :
		print(root.data)
	else:
		levelorderu(root.left, l - 1)
		levelorderu(root.right, l - 1)
def invert(root):
	if root:
		root.left, root.right = root.right, root.left
		invert(root.left)
		invert(root.right)
	else:
		return 

def search(root):
	if not root:
		return False 
	if root.data == data:
		return True 
	else:
		return search(root.left) or search(root.right)

def IsSymmetric(root):
	return IsMirror(root.left, root,right)

def IsMirror(rootl, rootr):
	q = [(rootl, rootr)]
	while q :
		x, y = q.pop()
		if not x and not y:
			continue
		if not x or not y:
			return False 
		if x.data != y.data:
			return False 
		else:
			q.append((x.left, y.right))
			q.append((x.right, y.left))
		return False 

def IsValid(root):
	return IsBst(root, float('-inf'), float('inf'))

def IsBst(root, lower, upper):
	if not root:
		return 
	else:
		if lower < root.data < right:
			IsBst(root.left, lower, root.data) and IsBst(root.right, root.data, upper)

def kthanc(root, n, k):
	if not root:
		return 
	if root.data == n or kthanc(root.left, n, k) or kthanc(root.right, n, k):
		if k[0] > 0:
			k[0] -= 1
		elif k[0] == 0:
			print(root.data)
			return None
		return root 

def PathSum(root, target):
	if not root:
		return False 
	if not root.left and not root.right and root.data == target :
		return True 
	else:
		return PathSum(root.left, target - root.data) or PathSum(root.right, target - root.data)

def Paths(root):
	if not root:
		return []
	if not root.left and not root.right:
		return [str(root.data)]
	path = []
	l = Paths(root.left)
	r = Paths(root.right)
	for i in l :
		path.append(str(root.data) + '->'+ i)
	for i in r:
		path.append(str(root.data) + '->' + i)
	return path

def PathSumpaths(root, target):
	if not root:
		return 
	res =[]
	dfs(root, target, [], res)
	return res 

def dfs(root, target, path, res):
	if not root:
		return 
	if not root.left and not root.right and root.data == target :
		path.append(root.data)
		res.append(path)
	else:
		dfs(root.left, target - root.data, path + [root.data], res)
		dfs(root.right, target - root.data, path + [root.data], res)

class solution:
	def __init__(self):
		self.max_level = 0 
	def LeftView(self, root):
		if not root:
			return 
		res = []
		self.leftviewdfs(root, 1, res)
		return res 
	def leftviewdfs(self, root, level, res):
		if not root:
			return 
		if self.max_level < level:
			res.append(root.data)
			self.max_level = level 
		self.leftviewdfs(root.left, level + 1, res)
		self.leftviewdfs(root.right, level + 1, res)

	def RightView(self, root):
		if not root:
			return 
		res = []
		self.rightviewdfs(root, 1, res)
		return res 
	def rightviewdfs(self, root, level, res):
		if not root:
			return 
		if self.max_level < level:
			res.append(root.data)
			self.max_level = level 
		self.rightviewdfs(root.right, level + 1, res)
		self.rightviewdfs(root.left, level + 1, res)

def BalanceTree(root):
	if not root:
		return - 1
	inOrder = inOrderBuilder(root)
	return Balancer(root, inOrder, 0, len(inOrder) - 1)

def inOrderBuilder(root):
	if root:
		return inOrderBuilder(root.left) + [root.data] + inOrderBuilder(root.right)
	else:
		return []

def Balancer(root, sol, l, h):
	if h < l : return 0
	mid = (l + h)//2
	root = node(sol[mid])
	root.left = Balancer(root, sol, l, mid - 1)
	root.right = Balancer(root, sol, mid + 1 , h)
	return root 

def Rotate(arr, k):
	if not arr and not k:
		return []
	start, end = 0, len(arr) - 1
	rev(arr, start, end - k)
	rev(arr, end - k + 1, end)
	rev(arr, start, end)
	return arr 

def rev(arr, i, j):
	if j < i : return 
	while j > i :
		arr[i], arr[j] = arr[j], arr[i]
		i += 1
		j -= 1






