def KadensCircular(arr):
	if not arr : raise ValueError 
	lcl_max, lcl_min, global_max, global_min = 0, 0, arr[0], arr[0]
	for num in arr:
		lcl_min += num 
		lcl_max += num 
		if global_max < lcl_max : 
			lcl_max = global_max 
		if global_min > lcl_min : 
			global_min = lcl_min 
		if lcl_max < 0 : lcl_max = 0 
		if lcl_min > 0 : lcl_min = 0 
	return max(global_max, sum(arr) - global_min) if global_max > 0 else max(arr)


def Perms(arr):
	def Helper(arr, path, res):
		if not arr : res.append(path)
		for i in range(len(arr)):
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)
	if not arr : raise ValueError 
	res = []
	Helper(arr, [], res)
	return res

def BalancedParanthesis(n):
	def Helper(Open, Close, path, res):
		if not Open and not Close:
			res.append(path)
			return 
		if Open > 0 : 
			Helper(Open - 1, Close, path + "(", res)
		if Close > Open:
			Helper(Open, Close - 1, path + ")", res)

	if not n : raise ValueError 
	res = []
	Helper(n, n, "", res)
	return res 

def Boats(arr, days):
	def Helper(arr, mid, days):
		curr_day = 1 
		curr_wt = 0 
		for i in range(len(arr)):
			curr_wt += arr[i]
			if curr_wt > mid:
				curr_wt = arr[i]
				curr_day += 1 
			if curr_day > days : return False 
		return True 
	if not arr : raise ValueError 
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if Helper(arr, mid, days):
			res = mid 
			h = mid - 1 
		else:
			l = mid + 1 
	return res 

def SubsetsEqualK(arr, k):
	if not arr : raise ValueError 
	prefix = 0 
	d = {0 : 1}
	count = 0 
	for num in arr:
		prefix += num 
		if prefix - k in d : 
			count += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1 
	return count 

def ExactlyKUnique(arr, k):
	if not arr : raise ValueError 
	def Helper(arr, k):
		l, r, count, res = 0, 0, 0, 0 
		d = {}
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1 
			if d[arr[r]] == 1 : count += 1 
			while l < r and count > k :
				d[arr[l]] -= 1 
				if d[arr[l]] == 0 : count -= 1 
				l += 1 
			res += r - l + 1 
			r += 1 
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def MaxLengthOfKUnique(arr, k):
	if not arr : raise ValueError 
	def Helper(arr, k):
		if not arr : raise ValueError 
		l, r, count, res = 0, 0, 0, 0 
		d = {}
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1 
			if d[arr[r]] == 1 : count += 1 
			while l < r and count > k : 
				d[arr[l]] -= 1 
				if d[arr[l]] == 0 : count -= 1 
				l += 1 
			res = max(res, r - l + 1)
			r += 1 
		return res 

	return Helper(arr, k)

def MinimumOpsToMakeArrIncreasing(arr):
	if not arr : raise ValueError 
	diff, res = 0, 0 
	for i in range(1, len(arr)):
		if arr[i - 1] >= arr[i]:
			diff = arr[i - 1] - arr[i] + 1 
			res += diff 
			arr[i] = arr[i - 1] +1 
	return res 

def MinLengthSubarrayEqualTarget(arr, k):
	if not arr : raise ValueError 
	l, r, prefix, res = 0, 0, 0, len(arr) + 1
	while r < len(arr):
		prefix += arr[r]
		while l < r and prefix > k :
			res = min(res, r - l + 1)
			prefix -= arr[l]
			l += 1 
		r += 1 
	return res 

def TwoProduct(arr, k):
	if not arr : raise ValueError 
	d = {}
	for i in range(len(arr)):
		if k//arr[i] in d and k % arr[i] == 0 : 
			return d[k//arr[i]], i 
		d[arr[i]] = i 
	return -1 

def BeautifulArrangements(n):
	def Helper(arr, path, res, idx):
		if not arr:
			res.append(path)
			return 
		for num, i in enumerate(arr):
			if num % idx == 0 or idx % num == 0 : 
				Helper(arr[:i] + arr[i + 1:], path + [arr[i]],res, idx + 1)

	if not n : raise ValueError 
	arr = list(range(1, n + 1))
	res = []
	Helper(arr, [], res, 1)
	return len(res)

def BeautifulArrangements2(n, k):
	if not n : raise ValueError 
	arr = list(range(1, n + 1))
	for i in range(1, k):
		arr[i:] = arr[:i - 1:-1]
	return arr 

def PhoneCombinations(sti):
	def Helper(arr, d, path, res):
		if not arr : 
			res.append(path)
			return 
		for char in d[arr[0]]:
			Helper(arr[1:], d, path + char, res)

	if not sti : raise ValueError 
	d = {"2" : "abc", "3" : "def"}
	res = []
	Helper(sti, d, "", res)
	return res 

class KthLargest:
	def __init__(self, arr, k):
		self.arr = arr
		self.k = k 
		heapq.heapify(self.arr)
		while len(self.arr) > k : 
			heapq.heappop(self.arr)
	def InsertAndShow(self, num):
		if len(self.arr) < k : heapq.heappush(self.arr, num)
		elif num > self.arr[0] : heapq.heapreplace(self.arr, num)
		return heapq.heappop(self.arr)

class Median:
	def __init__(self):
		self.small = []
		self.large = []
	def add(self, num):
		def Helper(small, large):
			if len(small) == len(large):
				heapq.heappush(small, -num)
				heapq.heappush(large, -heapq.heappop(small))
			else:
				heapq.heappush(large, num)
				heapq.heappush(small, -heapq.heappop(large))
		Helper(self.small, self.large)

	def Median(self):
		if len(self.large) == len(self.small):
			return (self.large[0] + self.small[0])//2
		else:
			return self.large[0]


def Diamonds(arr, k):
	if not arr : raise ValueError 
	pq = []
	for num in arr : heapq.heappush(pq, -num)
	count = 0 
	res = 0 
	while count < k : 
		count += 1 
		tmp = (-heapq.heappop(pq))
		x += tmp 
		heapq.heappush(pq, -(tmp//2))
	return res 

import heapq

def JoinRopes(arr):
	if not arr : raise ValueError 
	pq = []
	for num in arr : heapq.heappush(pq, num)
	res = 0 
	while len(pq) > 1:
		tmp = heapq.heappop(pq) + heapq.heappop(pq)
		res += tmp 
		heapq.heappush(pq, tmp)
	return res 

def Stones(arr):
	if not arr : raise ValueError 
	pq = [-num for num in arr]
	heaq.heapify(pq)
	while len(pq) > 1 and pq[0] != 0 : 
		heapq.heappush(pq, heapq.heappop(pq) - heapq.heappop(pq))
	return -pq[0]

def MinimumWorkers(wage, qual, k):
	if not wage or not qual : raise ValueError 
	expected = sorted([((w/q), q )for w, q in zip(wage, qual)])
	Qsum = 0 
	res = float('inf')
	pq = []
	for r, q in expected:
		heapq.heappush(pq, -q)
		Qsum += q 
		if len(pq) > k : Qsum += heapq.heappop(pq)
		if len(pq) == k : res = min(res, r * Qsum)
	return res 

def MaximumTeamEfficiency(speed, eff, k):
	if not speed or not eff : raise ValueError 
	expected = sorted([(e, s) for e, s in zip(eff, speed)])
	Ssum = 0 
	pq = []
	res = 0 
	for e, s in expected[::-1]:
		heapq.heappush(pq, s)
		Ssum += s 
		if len(pq) > k : Ssum -= heapq.heappop(pq)
		res = max(res, Ssum * e)
	return res 

def KClosestPointsToOrigin(arr, k):
	if not arr : raise ValueError 
	pq = []
	for x, y in arr:
		dist = (x * x) + (y * y)
		heapq.heappush(pq, (-dist, (x, y)))
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

def SupplierProfit(arr, k):
	if not arr : raise ValueError 
	count = 0 
	pq = [-num for num in arr]
	heapq.heapify(pq)
	res = 0 
	while count < k:
		x = heapq.heappop(pq)
		res += (-x)
		heapq.heappush(pq, x + 1)
		count += 1
	return res 

def CookChef(arr, p):
	def Helper(arr, mid, p):
		curr_p = 0 
		curr_time = 0 
		for i in range(len(arr)):
			curr_time = arr[i]
			j = 2
			while curr_time <= mid:
				curr_time += arr[i] * j 
				j += 1 
				curr_p += 1 
				if curr_p >= p : return True 
		return False 
	if not arr : raise ValueError 
	l, h = 0, 1e8 
	while h >= l :
		mid = l + (h - l)//2
		if Helper(arr, mid, p):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1 
	return res 

def Partitions(arr, stu):
	def Helper(arr, mid, stu):
		curr_stu = 1 
		curr_part = 0 
		for i in range(len(arr)):
			curr_part += arr[i]
			if curr_part > mid:
				curr_part = arr[i]
				curr_stu += 1
			if curr_stu > stu : return False 
		return True 
	if not arr : raise ValueError 
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if Helper(arr, mid, stu):
			res = mid 
			h = mid -1 
		else:
			l = mid + 1 
	return res 

def sortAlmostSortedArray(arr, k):
	if not arr : raise ValueError 
	pq = arr[:k]
	heapq.heapify(pq)
	idx = 0 
	res = []
	for i in range(k, len(arr)):
		arr[idx] = heapq.heappop(pq)
		idx += 1 
		heapq.heappush(pq, arr[i])
	while pq:
		arr[idx] = heapq.heappop(pq)
		idx += 1 
	return arr 

def FirstOccurance(grid):
	def Helper(arr, l, h):
		while h >= l:
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
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
		if idx != -1 :
			break 
	return i, idx 

def stocks1(arr):
	if not arr : raise ValueError 
	min_price, max_profit = float('inf'), float('-inf')
	for price in arr:
		min_price = min(price, min_price)
		curr_profit = price - min_price
		max_profit = max(curr_profit, max_profit)
	return max_profit

def Stocks1NegativeVals(arr):
	if not arr : raise ValueError 
	lcl_max, global_max = 0, 0 
	for i in range(1, len(arr)):
		lcl_max = max(0, arr[i] - arr[i - 1])
		global_max = max(lcl_max, global_max)
	return global_max 

def Stocks2(arr):
	if not arr : raise ValueError 
	return sum([tomorrow - today for today, tomorrow in zip(arr, arr[1:]) if tomorrow - today > 0])

def isValidMountain(arr):
	if not arr : raise ValueError 
	i, j = 0, len(arr) - 1
	if len(arr) < 3 : return False 
	while i < len(arr) - 1 and arr[i + 1] > arr[i]:
		i += 1
	while j > 0 and arr[j - 1] > arr[j]:
		j -= 1 
	return i == j and (i != 0 and j != len(arr) - 1)

def MaxMountainArray(arr):
	if not arr : raise ValueError 
	if len(arr) < 3 : return False 
	res = 0 
	for i in range(1, len(arr) - 1):
		if arr[i + 1] < arr[i] > arr[i - 1]:
			l, r = i, i 
			while l > 0 and arr[l] > arr[l - 1] : l -= 1
			while r < len(arr) - 1 and arr[r] > arr[r + 1] : r += 1
			res = max(res, r - l + 1)
	return res 

def CombinationSum(arr, target):
	def Helper(arr, path, res, target):
		if target == 0 : 
			res.append(path)
			return
		if target < 0 : return  
		for i in range(len(arr)):
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res, target - arr[i])

	if not arr : raise ValueError 
	res = []
	Helper(arr, [], res, target, 0)
	return res 

def ZigZag(sti, n):
	if not sti : raise ValueError 
	inc_up = True 
	idx = 1 
	res = ["" for _ in range(n)]
	for char in sti:
		res[idx - 1] += char 
		if idx == n : inc_up = False 
		if idx == 1 : inc_up = True 
		if inc_up : idx += 1 
		else : idx -= 1
	return "".join(res)

def Subsets(arr):
	if not arr : raise ValueError 
	sol = [[]]
	for num in arr:
		sol += [curr + [num] for curr in sol]
	return sol 

def TripletsWhichSumToTarget(arr, target):
	if not arr : raise ValueError 
	for i in range(len(arr)):
		d = {}
		curr = target - arr[i]
		for j in range(i, len(arr)):
			if curr - arr[j] in d : 
				return i, j, d[curr - arr[j]]
			d[arr[j]] = j
	return - 1

def TripletsWhichFormATriangle(arr):
	if not arr : raise ValueError 
	res = 0 
	arr.sort()
	for i in range(2, len(arr)):
		l, r = 0, i - 1 
		while l < r :
			if arr[l]  + arr[r] > arr[i]:
				res += (r - l)
				r -= 1 
			else:
				l += 1
	return res 

def TripletsWhichSumToZero(arr):
	if not arr : raise ValueError 
	res = []
	for i in range(len(arr)):
		num = arr[i]
		l, r = i + 1, len(arr) - 1 
		while l < r : 
			if arr[l] + arr[r] + num == 0 :
				res.append((arr[l], arr[r], num))
				r -= 1 
				l += 1 
			elif arr[l] + arr[r] + num < 0 : l += 1 
			else : r -= 1 
	return res 

def CountAllTripletsWhichSumToTarget(arr, target):
	if not arr : raise ValueError 
	res = []
	for i in range(len(arr)):
		curr = target - arr[i]
		d = {}
		for j in range(i + 1, len(arr)):
			if curr - arr[j] in d : 
				res.append((arr[i], arr[j], curr - arr[j]))
			d[arr[j]] = j 
	return res 


def UniquePaths(m, n):
	if not m or not n : raise ValueError 
	dp = [[1 for _ in range(n)] for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
	return dp[m - 1][n - 1]

def UnquePaths2(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError
	dp = [[0 for _ in range(n)] for _ in range(m)]
	if not grid[0][0] : dp[0][0] = 1 
	for i in range(1, m):
		if not grid[i][0] : dp[i][0] = 1 
	for i in range(1, n):
		if not grid[0][i] : dp[0][i] = 1 
	for i in range(1, m):
		for j in range(1, n):
			if grid[i][j] : continue 
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

def Eggs_max(f, n):
	if not f or not n : raise ValueError 
	dp = [[0 for _ in range(n + 1)] for _ in range(f + 1)]
	for i in range(1, f + 1):
		for j in range(1, n + 1):
			dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1 
		if dp[i][j] >= f : return i 
	return - 1

def TrainTix(days, cost):
	if not days or not cost : raise ValueError 
	dp = [-1 for _ in range(366)]
	dp[0] = 0 
	for day in days : dp[day] = 0 
	for i in range(1, 366):
		if dp[i] == - 1 : dp[i] = dp[i - 1]
		else:
			dp[i] = min(dp[max(i - 1, 0)] + cost[0], dp[max(i - 7, 0)] + cost[1], dp[max(i - 30, 0)] + cost[2])
	return dp[-1]

def coinChange(ammount, coins):
	if not ammount or not coins : raise ValueError
	dp = [float('inf') for _ in range(ammount + 1)]
	dp[0] = 0 
	for i in range(1, ammount + 1):
		for coin in coins:
			if dp[i - coin] >= 0 : 
				dp[i] = min(dp[i], dp[i - coin] + 1)
	return dp[-1]

def WordBreak(sti, words):
	if not sti or not words : raise ValueError 
	dp = [False for _ in range(len(sti) + 1)]
	dp[0] = True 
	for i in range(1, len(sti) + 1):
		for word in words:
			if sti[:i].endswith(word):
				dp[i] = dp[i] | dp[i - len(word)]
	return dp[len(sti)]

def RegularExpression(sti, patter):
	if not sti or not pattern : raise ValueError 
	m, n = len(sti), len(pattern)
	dp = [[False for _ in range(n + 1)] for _ in range(len(m + 1))]
	for i in range(1, n + 1):
		if dp[0][i] == "*":
			dp[0][i] = dp[0][i - 2]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if pattern[j - 1] == "." or sti[i - 1] == pattern[j - 1]:
				dp[i][j] = dp[i - 1][j - 1]
			elif pattern[j - 1] == "*":
				dp[i][j] = dp[i][j - 2]
				if pattern[j - 2] == "." or sti[i - 1] == pattern[j - 2]:
					dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
	return dp[m][n]

def Lcs(x, y):
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

def LongestPalindromicSubstring(sti):
	def Helper(sti, i, j):
		while i >= 0 and j < len(sti) and sti[i] == sti[j]:
			i -= 1 
			j += 1
		return sti[i + 1: j]
	if not sti : raise ValueError 
	res = ""
	for i in range(len(sti)):
		left = Helper(sti, i, i)
		right = Helper(sti, i, i + 1)
		res = max(res, left, right, key = len)
	return res 

def MaximumProductSubarray(arr):
	if not arr : raise ValueError 
	b = arr[::-1]
	for i in range(1, len(arr)):
		arr[i] *= arr[i - 1]
		b[i] *= b[i - 1]
	return max(arr + b)

def JumpGame(arr):
	if not arr : raise ValueError 
	last = len(arr) - 1 
	for i in range(len(arr) - 2, -1, -1):
		if i + arr[i] >= last:
			last = i 
	return last == 0 

def JumpGame2(arr):
	if not arr : raise ValueError 
	l, r = 0, arr[0]
	while r < len(arr) - 1 :
		count += 1 
		next_jump = max([j + arr[j] for j in range(l, r + 1)])
		l, r = r, next_jump 
	return count
def JumpGame3(arr, start):
	if not arr : raise ValueError 
	q = [(start)]
	while q : 
		i = q.pop(0)
		if arr[i] == 0 : return True
		x, y = i + arr[i], i - arr[i]
		arr[i] = - 1 
		if x < len(arr):
			if arr[x] != -1 : q.append(x)
		if y >= 0:
			if arr[y] != -1  : q.append(y)
	return False

def RegularExpression(sti, pattern):
	m, n =len(sti), len(pattern)
	if m == 0 or n == 0 : raise ValueError
	dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
	dp[0] = True 
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
					dp[i][j] = dp[i - 1][j]
	return dp[m][n]

def MaximumProductSubarray(arr):
	if not arr : raise ValueError 
	tmp = arr[::-1]
	for i in range(1, len(arr)):
		tmp[i] *= tmp[i - 1]
		arr[i] *= arr[i - 1]
	return max(arr + tmp)

def ZigZag2(sti, n):
	if not sti : raise ValueError 
	res = ["" for _ in range(n)]
	idx = 0 
	up = True 
	for char in sti:
		res[idx] += char 
		if up : idx += 1 
		else : 	idx -= 1 
		if idx == n - 1 : up = False 
		elif idx == 0 : up = True 
	return "".join(res)

def LongestValidParanthesis(sti):
	if not sti : raise ValueError 
	dp = [0 for _ in range(len(sti))]
	q = []
	for i in range(len(sti)):
		if sti[i] == "(":
			q.append(i)
		elif q:
			pos = q.pop()
			dp[i] = i - pos + 1 + dp[pos - 1]
	return max(dp)

def PalindromePartitioning(sti):
	def isPal(sti):
		return sti == sti[::-1]

	def Helper(sti, path, res):
		if not sti:
			res.append(path)
			return 
		for i in range(1, len(sti) + 1):
			if isPal(sti[:i]):
				Helper(sti[i:], path + [sti[:i]], res)
	if not sti : raise ValueError 
	res = []
	Helper(sti, [], res)
	return res 

def OrderOflargestPlusSign(n, mines):
	if not n : raise ValueError
	dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
	mine = {(i, j) for i, j in mines}
	res = 0 
	for i in range(n):
		for j in range(n):
			if (i, j) not in mine:
				dp[i][j][0] = (dp[i - 1][j][0] + 1) if i - 1 >= 0 else 1 
				dp[i][j][1] = (dp[i][j - 1][1] + 1) if j - 1 >= 0 else 1 
	for i in range(n - 1, -1, -1):
		for j in range(n - 1, -1, -1):
			if (i, j) not in mine:
				dp[i][j][2] = (dp[i + 1][j][2] + 1) if i + 1 < n else 1 
				dp[i][j][3] = (dp[i][j + 1][3] + 1) if j + 1 < n else 1 
			res = max(res, min(dp[i][j]))
	return res 
			

def LongestPalindromicSubstring(sti):
	def Helper(sti, i, j):
		while i >= 0 and j < len(sti) and sti[i] == sti[j]:
			i -= 1 
			j += 1 
		return sti[i + 1 : j]
	if not sti : raise ValueError 
	res = ""
	for i in range(len(sti)):
		left = Helper(sti, i, i)
		Right = Helper(sti, i, i + 1)
		res = max(res, left, Right, key = len)
	return res 

n = 5 
mines = [[4, 2]]
sti = "bcababade"
print(LongestPalindromicSubstring(sti))
#print(OrderOflargestPlusSign(n, mines))
#print(PalindromePartitioning("aab"))


