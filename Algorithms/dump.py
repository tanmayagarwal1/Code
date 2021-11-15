def LongestCommonSubsequence(x, y):
	m, n = len(x), len(y)
	if m == 0 or n == 0 : raise ValueError 
	dp = [[0 for _ in range(n + 1)]for _ in range(m + 1)]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] == y[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + 1 
			else:
				dp[i][j] = max(dp[i - 1][j], d[i][j - 1])
	return dp[m][n]

def LongestPalindromicSubsequence(x):
	def Helper(x, y):
		m, n = len(x), len(y)
		dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if x[i - 1] == y[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] +1 
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
		return dp[m][n]

	if not x : raise ValueError
	return Helper(x, x[::-1])

def LongestIncreasingSubsequence(x):
	def Helper(x, y):
		m, n = len(x), len(y)
		if m == 0 or n == 0 : raise ValueError
		dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if x[i - 1] == y[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + 1 
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
		return dp[m][n]

	if not x : raise ValueError
	s, q = set(), []
	for char in x : 
		if char not in s : 
			q.append(char)
			s.add(char)
		else:
			continue 
	return Helper(x, "".join(sorted(q)))

def DistinctSubsequences(x, y):
	m, n = len(x), len(y)
	if m == 0 or n == 0 : raise ValueError 
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	for i in range(n + 1):
		dp[0][i] = 1 
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] == y[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
			else:
				dp[i][j] = dp[i][j - 1]
	return dp[m][n]

def WordBreak(sti, words):
	if not sti : raise ValueError 
	dp = [True] + [False for _ in range(len(sti))]
	for i in range(1, len(sti) + 1):
		for word in words:
			if sti[:i].endswith(word):
				dp[i] = dp[i] | dp[i - len(word)]
	return dp[len(sti)]

def WordLadder(start, end, words):
	def Construct(words):
		d = {}
		for word in words:
			for i in range(len(word)):
				s = word[:i] + "*" + word[i + 1:]
				d[s] = d.get(s, []) + [word]
		return d 

	def Helper(start, end, words, d):
		q = [(start, 1)]
		visited = set()
		while q :
			word, step = q.pop(0)
			if word not in visited : visited.add(word)
			if word == end : return step 
			for i in range(len(word)):
				curr_word = word[:i] + "*" + word[i + 1:]
				neighbouring_words = d.get(curr_word, [])
				for neighbours in neighbouring_words :
					if neighbours not in visited:
						q.append((neighbours, step + 1))
		return -1 


	if not start or not end : raise ValueError 
	return Helper(start, end, words, Construct(words))

def WordLadder2(start, end, words):
	if not start or not end : raise ValueError 
	def Construct(words):
		d = {}
		for word in words:
			for i in range(len(word)):
				sti = word[:i] + "*" + word[i + 1 : ]
				d[sti] = d.get(sti, []) + [word]
		return d 

	def Helper(start, ends, words, d):
		visited = set([start])
		q = [(start, [start])]
		res = []
		while q and not res : 
			lcl = set()
			for _ in range(len(q)):
				word, path = q.pop(0)
				if word == end : res.append(path + [word])
				for i in range(len(word)):
					sti = word[:i] + "*" + word[i + 1:]
					neighbours = d.get(sti, [])
					for neighbour in neighbours:
						if neighbour not in visited:
							lcl.add(neighbour)
							q.append((neighbour, path + [neighbour]))
			visited = visited.union(lcl)
		return res 

	return Helper(start, end, words, Construct(words))

def LongestValidParanthesis(sti):
	if not sti : raise ValueError 
	dp = [0] * len(sti)
	q = []
	for i in range(len(sti)):
		if sti[i] == "(" : q.append(i)
		elif q : 
			pos = q.pop()
			dp[i] = i - pos + 1 + dp[pos - 1]
	return max(dp)

def RegularExpressionMatching(sti, pattern):
	m, n = len(sti), len(pattern)
	if m == 0 or n == 0 : raise ValueError 
	dp = [[False for _ in range(n + 1)]for _ in range(m + 1)]
	dp[0][0] = True 
	for i in range(1, n + 1):
		if pattern[i - 1] == "*":
			dp[0][i] = dp[0][i - 2]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if sti[i - 1] == pattern[j - 1] or pattern[j - 1] == ".":
				dp[i][j] = dp[i - 1][j - 1]
			elif pattern[j - 1] == "*":
				dp[i][j] = dp[i][j - 2]
				if sti[i - 1] == pattern[j - 2] or pattern[j - 2] == ".":
					dp[i][j] = dp[i][j] | dp[i - 1][j]
	return dp[m][n]

def JumpGame(arr):
	if not arr : raise ValueError 
	last = len(arr) -1  
	for i in range(len(arr) - 2, -1, -1):
		if i + arr[i] >= last :
			last = i 
	return last == 0 

def JumpGame2(arr):
	if not arr : raise ValueError 
	count = 1 
	l, r = 0, arr[0]
	while r < len(arr) - 1 : 
		count += 1 
		nxt = max([j + arr[j] for j in range(l, r + 1)])
		l, r = r, nxt
	return count 

def JumpGame3(arr, start):
	if not arr : raise ValueError 
	q = [start]
	while q:
		i = q.pop(0)
		if arr[i] == 0 : return True 
		val = arr[i]
		arr[i] = -1 
		x, y = i + val, i - val 
		if x < len(arr) and arr[x] != -1 : q.append(x)
		if y >= 0 and arr[y] != -1 : q.append(y)
	return False 

def UniquePaths(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	dp = [[1 for _ in range(n)]for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
	return dp[m - 1][n - 1]

def UniquePaths2(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[0][0] = grid[0][0] if grid[0][0] != 1 
	for i in range(1, m):
		if not grid[i][0]:
			dp[i][0] = 1 
	for i in range(1, n):
		if not grid[0][i]:
			grid[0][i] = 1

	for i in range(1, m):
		for j in range(1, n):
			if not grid[i][j]:
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
	return dp[m - 1][n - 1]

def MinimumCostPath(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[0][0] = grid[0][0]
	for i in range(1, m):
		dp[i][0] = dp[i - 1][0] + grid[i][0]
	for i in range(1, n):
		dp[0][i] = dp[0][i - 1] + grid[0][i]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
	return dp[m - 1][n - 1]

def CoinChange(ammount, coins):
	if not coins : raise ValueError
	dp = [float('inf') for _ in range(ammount + 1)]
	dp[0] = 0 
	for i in range(1, ammount + 1):
		for coin in coins:
			if dp[i - coin] >= 0 : 
				dp[i] = min(dp[i], dp[i - coin] + 1)
	return dp[ammount]
