import heapq 

def Kadens(arr):
	if not arr : raise ValueError 
	global_max = 0 
	local_max = 0 
	start, end, tmp = 0, 0, 0 
	for i in range(len(arr)):
		local_max += arr[i]
		if local_max > global_max:
			global_max = local_max 
			start = tmp 
			end = i 
		if local_max <= 0 :
			local_max = 0 
			tmp = i 
	return global_max, start, end

class sorts:
	def __init__(self):
		pass 

	def MergeSort(self, arr):
		if not arr : raise ValueError 
		if len(arr) > 1 :
			mid = len(arr)//2
			l = arr[:mid]
			r = arr[mid :]
			self.MergeSort(l)
			self.MergeSort(r)
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
		return arr 

	def QuickSort(self, arr):
		if not arr : raise ValueError 
		def partition(arr, l, h):
			if h < l : return 
			i = l - 1 
			pivot = arr[h]
			for j in range(l, h):
				if arr[j] <= pivot:
					i += 1 
					arr[i], arr[j] = arr[j], arr[i]
			arr[i + 1], arr[h] = arr[h], arr[i + 1]
			return i + 1

		def Helper(arr, l, h):
			if h < l : return 
			if h >= l:
				mid = partition(arr, l, h)
				Helper(arr, l, mid - 1)
				Helper(arr, mid + 1, h)
				return 

		Helper(arr, 0, len(arr) - 1)
		return arr 

	def HeapSort(self, arr):
		def Helper(arr, n, i):
			large = i 
			l = 2 * i + 1
			r = 2 * i + 2 
			if l < n and arr[large] < arr[l]:
				large = l 
			if r < n and arr[large] < arr[r]:
				large = r 
			if large != i:
				arr[i], arr[large] = arr[large], arr[i]
				Helper(arr, n, large)

		if not arr : raise ValueError 
		for i in range(len(arr)//2 - 1, -1, -1):
			Helper(arr, len(arr), i)
		for i in range(len(arr) - 1, 0, -1):
			arr[0], arr[i] = arr[i], arr[0]
			Helper(arr, i, 0)
		return arr 

	def BubbleSort(self, arr):
		if not arr : raise ValueError 
		for i in range(len(arr)):
			for j in range(i + 1, len(arr)):
				if arr[j] < arr[i]:
					arr[i], arr[j] = arr[j], arr[i]
		return arr 


def Subsets(arr):
	if not arr : raise ValueError 
	sol = [[]]
	for num in arr:
		sol += [curr + [num] for curr in sol]
	return sol 

def Perms(arr):
	def Helper(arr, path, res):
		if not arr:
			res.append(path)
			return 
		for i in range(len(arr)):
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

	if not arr : raise ValueError 
	res = []
	Helper(arr, [], res)
	return res 

def NextPerm(arr):
	if not arr : raise ValueError 
	i, j = len(arr) - 1, len(arr) - 1
	while i >= 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i == 0 : 
		arr.reverse()
		return arr 
	k = i - 1
	while arr[j] <= arr[k]:
		j -= 1
	arr[j], arr[k] = arr[k], arr[j]
	l, h = k + 1, len(arr) - 1 
	while h > l :
		arr[l], arr[h] = arr[h], arr[l]
		l += 1 
		h -= 1
	return arr 

def ProductArray(arr):
	if not arr : raise ValueError 
	res = [1] * len(arr)
	for i in range(1, len(arr)):
		res[i] = res[i - 1] * arr[i - 1]
	prod = 1 
	for i in range(len(arr) - 1, -1, -1):
		res[i] *= prod 
		prod *= arr[i]
	return res 


def PeakElement(arr):
	if not arr : raise ValueError 
	l, h = 0, len(arr) - 1
	while h >= l :
		mid = l + (h - l)//2
		if mid != 0 and mid != len(arr) - 1:
			if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
				return mid 
			if arr[mid] < arr[mid + 1]:
				l = mid + 1
			else:
				h = mid - 1 
		elif mid == 0 : 
			if arr[mid] > arr[mid + 1] : return mid 
			else : return mid + 1 
		elif mid == len(arr) - 1 :
			return mid if arr[mid] > arr[mid - 1] else mid - 1 
	return - 1

def SubarrayWhichSorts(arr):
	if not arr : raise ValueError 
	l, h = 0, len(arr) - 1 
	while l < len(arr) - 1 and arr[l + 1] >= arr[l]:
		l +=  1
	while h > 0 and arr[h - 1] <= arr[h]:
		h -= 1 
	mini, maxi = min(arr[l:h]), max(arr[l:h])
	for x in range(l):
		if arr[x] > maxi:
			i = x 
	for x in range(h, len(arr)):
		if arr[x] < mini:
			h = x 
	return l, h 

def Rotate(arr, k):
	def Reverse(arr, l, h):
		while h > l :
			arr[l], arr[h] = arr[h], arr[l]
			l += 1
			h -= 1

	if not arr : raise ValueError 
	k = k % len(arr)
	l, h = 0, len(arr) - 1 
	mid = h - k 
	Reverse(arr, l, mid)
	Reverse(arr, mid + 1, h)
	Reverse(arr, l, h)
	return arr 

def SearchInRotated(arr, target):
	if not arr : raise ValueError 
	def Helper(arr):
		l, h = 0, len(arr) - 1 
		while h >= l:
			if arr[l] <= arr[h] : return l 
			mid = l + (h - l)//2
			ne = (mid + 1) % len(arr)
			prev = (mid + len(arr) - 1) % len(arr)
			if arr[mid] < arr[ne] and arr[mid] < arr[prev]:
				return mid 
			if arr[l] <= arr[mid]:
				l = mid + 1
			if arr[mid] <= arr[h]:
				h = mid - 1
		return - 1

	def BinarySearch(arr, l, h):
		while h >= l:
			mid = l + (h - l)//2
			if arr[mid] == target:
				return mid 
			if arr[mid] < target:
				l = mid + 1 
			else:
				h = mid - 1
		return - 1

	idx = Helper(arr)
	l = BinarySearch(arr, 0, idx - 1)
	r = BinarySearch(arr, idx, len(arr) - 1)
	return l if l != -1 else r 

def AlternatingPostitivesAndNegatives(arr):
	if not arr : raise ValueError 
	def Helper(arr):
		i = - 1
		for j in range(len(arr)):
			if arr[j] < 0:
				i += 1 
				arr[i], arr[j] = arr[j], arr[i]
		return i + 1

	i = Helper(arr)
	k = 0
	while k < len(arr) and i < len(arr):
		arr[k], arr[i] = arr[i], arr[k]
		k += 2 
		i += 1
	return arr 

def DutchFlag(arr):
	if not arr : raise ValueError 
	i, h, mid = 0, len(arr) - 1, 0 
	while h >= mid:
		if arr[mid] == 0 :
			arr[i], arr[mid] = arr[mid], arr[i]
			i += 1 
			mid += 1
		elif arr[mid] == 1 :
			mid += 1
		else:
			arr[mid], arr[h] = arr[h], arr[mid]
			h -= 1 
	return arr 

def FloydsAlgo(arr):
	if not arr : raise ValueError
	slow, fast, ans = 0, 0, 0 
	while True:
		slow = arr[slow]
		fast = arr[arr[fast]]
		if slow == fast:
			break 
	while ans != slow:
		ans = arr[ans]
		slow = arr[slow]
	return ans 

def EqualPilesHeight(arr):
	if not arr : raise ValueError 
	arr.sort(reverse = True)
	steps = 0 
	for i in range(1, len(arr)):
		if arr[i - 1] != arr[i]:
			steps += i 
	return steps 

def Houses(arr, b):
	if not arr : raise ValueError 
	q = []
	for i in range(len(arr)):
		if arr[i] > b :
			continue 
		ini = arr[i]
		count = 1 
		for j in range(len(arr)):
			if i == j : continue 
			if arr[j] + ini >= b:
				ini += arr[j]
				count += 1
		q.append(count)
	res = 0
	for i in range(len(q)):
		res = max(res, q[i])
	return res 

def BeautifulArrangements(n):
	def Helper(arr, path, res, idx):
		if not arr:
			res.append(path)
			return 
		for i, num in enumerate(arr):
			if num % idx == 0 or idx % num == 0:
				Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res, idx + 1)

	if not n : raise ValueError 
	res = []
	arr = list(range(1, n + 1))
	Helper(arr, [], res, 1)
	return res 

def PermsWithDups(arr):
	def Helper(arr, path, res):
		if not arr:
			res.append(path)
			return 
		for i in range(len(arr)):
			if i and arr[i] == arr[i - 1] : continue 
			Helper(arr, path + [arr[i]], res)

	if not arr : raise ValueError 
	res = []
	Helper(arr, [], res)
	return res 

def SquarePerms(arr):
	def isSquare(num):
		return int(num**0.5)**2 == num 

	def Helper(arr, path, res):
		if not arr:
			res.append(path)
			return 
		for i in range(len(arr)):
			if i and arr[i] == arr[i - 1] : continue 
			if path and not isSquare(path[-1] + arr[i]) : continue 
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

	if not arr : raise ValueError 
	res = []
	Helper(arr, [], res)
	return res 

def MergedIntervals(arr):
	if not arr : raise ValueError 
	merged = []
	arr.sort() # For edge cases, we have to sort
	for i in arr:
		if not merged or merged[-1][1] < i[0]:
			merged.append(i)
		elif merged[-1][1] >= i[0]:
			merged[-1][0] = min( merged[-1][0], i[0] )
			merged[-1][1] = max( merged[-1][1], i[1] )
	return merged 

def ThreeSum(arr):
	if not arr : raise ValueError 
	n, p, z = [], [], []
	res = set()
	for num in arr:
		if num > 0 : p.append(num)
		elif num < 0 : n.append(num)
		else : z.append(num)
	N, P = set(n), set(p)
	if z:
		for num in p:
			if -num in N:
				res.add((num, 0, -num))
	if len(z) >= 3 : res.add((0, 0, 0))
	for i in range(len(p)):
		for j in range(i + 1, len(p)):
			target = p[i] + p[j]
			if -target in N :
				res.add((p[i], p[j], -target))
	for i in range(len(n)):
		for j in range(i + 1, len(n)):
			target = n[i] + n[j]
			if -target in P:
				res.add((n[i], n[j], -target))
	return res 

def CountSubsetsEqualK(arr, k):
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

def CountSubsetsDivisibleByK(arr, k):
	if not arr : raise ValueError
	prefix = 0 
	d = { 0 : 1 }
	count = 0 
	for num in arr:
		prefix += num 
		key = prefix % k 
		if key in d:
			count += d[key]
		d[key] = d.get(key, 0) + 1
	return count 

def TwoSum(arr, target):
	if not arr: raise ValueError
	d = {}
	for i in range(len(arr)):
		if target - arr[i] in d :
			return d[target - arr[i]], i 
		d[arr[i]] = i 
	return - 1

def PairMultiplyToK(arr, k):
	if not arr : raise ValueError
	d = {}
	for i in range(len(arr)):
		if k // arr[i] in d and k % arr[i] == 0 : return d[k // arr[i]], i 
		d[arr[i]] = i 
	return - 1 

def MinimumLengthSubarray(arr, k):
	if not arr : raise ValueError 
	l, r = 0, 0 
	prefix = 0 
	res = len(arr) + 1 
	while r < len(arr):
		prefix += arr[r]
		while l < r and prefix >= k :
			res = min(res, r - l + 1)
			prefix -= arr[l]
			l += 1
		r += 1
	return res 

def MaximumLengthSubarray(arr, k):
	if not arr : raise ValueError 
	l, r, prefix, res = 0, 0, 0, 0 
	while r < len(arr):
		prefix += arr[r]
		while l < r and prefix >= k :
			res = max(res, r - l + 1)
			prefix -= arr[l]
			l += 1
		r +=  1
	return res 

def SubarrayCountWithKDistinct(arr, k):
	if not arr : raise ValueError
	def Helper(arr, k):
		l, r, Count, res = 0, 0, 0, 0 
		d = {}
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1 
			if d[arr[r]] == 1 : count += 1
			while l < r and count > k :
				d[arr[l]] -= 1 
				if d[arr[l]] == 0 : count -=1 
				l += 1
			res += r - l + 1
			r += 1
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def NiceSubarrays(arr, k):
	if not arr : raise ValueError 
	def Helper(arr, k):
		l, r, count, res = 0, 0, 0, 0
		while r < len(arr):
			if arr[r] % 2 != 0 : count += 1
			while l < r and count > k:
				if arr[l] % 2 != 0 : count -= 1
				l += 1 
			res += r - l + 1 
			r += 1
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def BeautifulArrangements2(n, k):
	if not n : raise ValueError
	arr = list(range(1, n + 1)) 
	for i in range(1, k):
		arr[i:] = arr[:i -1  : - 1]
	return arr 

def MinOpsIncreaing(arr):
	if not arr : raise ValueError 
	ops = 0 
	for i in range(1, len(arr)):
		if arr[i] <= arr[i - 1]:
			diff = arr[i - 1] - arr[i] + 1 
			ops += diff 
			arr[i] = arr[i - 1] + 1
	return ops 

def MaxProductSubarray(arr):
	if not arr : raise ValueError
	rev = arr[::-1]
	for i in range(1, len(arr)):
		arr[i] = arr[i] * arr[i - 1]
		rev[i] = rev[i] * rev[i - 1]
	return max(arr + rev)

def PascalsTraingle(row):
	if not row : return 0 
	res = [1]
	for _ in range(row):
		res = [x + y for x, y in zip([0] + res, res + [0])]
	return res 

def MaxWaterContainer(arr):
	if not arr : raise ValueError 
	water = 0 
	i, j = 0, len(arr) - 1 
	while i < j :
		water = max(water, (j - i) * min(arr[i], arr[j]))
		if arr[i] < arr[j]:
			i += 1
		else:
			j -= 1
	return water 

def Boats(arr, days):
	def Helper(arr, mid, days):
		curr_day = 1 
		curr_wt = 0 
		for i in range(len(arr)):
			curr_wt += arr[i]
			if curr_wt > mid:
				curr_wt = arr[i]
				curr_day += 1
			if curr_day > days  : return False 
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
	while h >= l:
		mid = l + (h - l)//2
		if Helper(arr, mid, stu):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1 
	return res 

def LastStone(arr):
	if not arr : raise ValueError 
	heapq.heapify(arr)
	while len(arr) > 1 and arr[0] != 0:
		heapq.heappush(heapq.heappop(arr) + heapq.heappop(arr))
	return arr[0]

def Stocks(arr):
	if not arr : raise ValueError 
	max_profit = 0 
	min_price = float('inf')
	for price in arr:
		min_price = min(price, min_price)
		profit = price - min_price
		max_profit = max(max_profit, profit)
	return max_profit

def Stocks2(arr):
	return sum([tomorrow - today for today, tomorrow in zip(arr, arr[1:]) if tomorrow - today > 0])

def IsValidMountain(arr):
	if not arr : raise ValueError
	if len(arr) < 3 : return False 
	i, j = 0, len(arr) - 1 
	while i < len(arr) - 2 and arr[i + 1] > arr[i]:
		i += 1
	while j > 0 and arr[j - 1] > arr[j]:
		j -= 1
	if i == j and i != 0 : return True 
	return False 

def LongestMountainArray(arr):
	if not arr : raise ValueError 
	if len(arr) < 3 : return False 
	res = 0 
	for i in range(1, len(arr) - 1):
		if arr[i - 1] < arr[i] < arr[i + 1]:
			l = r = i 
			while l and arr[l - 1] < arr[l] : l -= 1
			while r < len(arr) - 1 and arr[r + 1] > arr[r] : r += 1 
			res = max(res, r - l + 1)
	return res 

def LcsArrays(arr):
	if not arr : raise ValueError 
	d = {}
	for row in arr:
		for num in row:
			d[num] = d.get(num, 0) + 1 
	res = []
	for num, freq in d.items():
		if freq == len(arr):
			res.append(num)
	return res 

def CombinationsSum(arr, target):
	def Helper(arr, target, path, res, idx):
		if target < 0 : return 
		if target == 0 : 
			res.append(path)
			return 
		for i in range(idx, len(arr)):
			Helper(arr, target - arr[i], path + [arr[i]], res, i)

	if not arr : raise ValueError 
	res = []
	Helper(arr, target, [], res, 0)
	return res 

def DeArrangementCount(arr):
	if not arr : raise ValueError 
	def Helper(arr):
		if not arr : return -1 
		if len(arr) == 1 : return 0 
		if len(arr) == 2 : return 1 
		return (n - 1) * (Helper(n - 1) + Helper(n - 2))

	return Helper(arr)

def WorkersMinimum(wage, qual, k):
	if not wage or not qual : raise ValueError 
	expected = sorted([(w/q), q] for w, q in zip(wage, qual))
	Qsum = 0 
	pq = []
	res = float('inf')
	for r, q in expected:
		heapq.heappush(pq, -q)
		Qsum += q 
		if len(pq) > k : Qsum += heapq.heappop(pq)
		if len(pq) == k : res = min(res, Qsum * r)
	return res 

def MaxTeamPerformance(speed, eff, k):
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

def MonotonicArray(num):
	if not num : raise ValueError 
	tmp = num 
	arr = [int(i) for i in str(tmp)[::-1]]
	idx = - 1
	for i in range(1, len(arr)):
		if arr[i - 1] < arr[i] or (idx != -1 and arr[i] == arr[i - 1]):
			idx = i 
	if idx == - 1 : return tmp 
	for i in range(idx):
		arr[i] = 9 
	arr[idx] -= 1 
	return ''.join([str(x) for x in arr[::-1]])

def KclosestPoints(arr, x, k):
	if not arr : raise ValueError 
	l, h = 0, len(arr) - k 
	while h >= l :
		mid = l + (h - l)//2
		if abs(arr[mid + k] - x) < abs(arr[mid] - x):
			l = mid + 1 
		else:
			h = mid - 1
	return arr[l : l + k]

def ClosestToOrigin(arr, k):
	if not arr : raise ValueError
	pq = []
	for i, j in arr:
		dist = i * i + j * j 
		heapq.heappush(pq, (-dist, (i, j)))
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

def KFrequentElements(arr, k):
	if not arr : raise ValueError 
	d = {}
	for i in arr:
		d[i] = d.get(i, 0) + 1 
	pq = []
	for num, freq in d.items():
		heapq.heappush(pq, (freq, num))
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

def KthLargest(arr, k):
	if not arr : raise ValueError 
	def partition(arr, l, h):
		if h < l : return 
		i = l - 1 
		pivot = arr[h]
		for x in range(l, h):
			if arr[x] <= pivot:
				i += 1
				arr[i], arr[x] = arr[x], arr[i]
		arr[i + 1], arr[h] = arr[h], arr[i + 1]
		return i + 1

	def Helper(arr, k):
		if arr:
			mid = partition(arr, 0, len(arr) - 1)
			if k > mid + 1 :
				return Helper(arr[mid + 1 : ], k - mid - 1)
			elif k < mid + 1:
				return Helper(arr[:mid], k)
			else:
				return arr[mid]

	return Helper(arr, len(arr) - k + 1)

def ValidBraces(n):
	def Helper(Open, Close, path, res):
		if not Open and not Close:
			res.append(path)
			return 
		if Open > 0:
			Helper(Open - 1, Close, path + '(', res)
		if Close > Open:
			Helper(Open, Close - 1, path + ')', res)

	if not n : raise ValueError 
	res = []
	Helper(n, n, '', res)
	return res 

def PhoneCombinations(digits):
	def Helper(arr, d, path, res):
		if not arr:
			res.append(path)
			return 
		for char in d[arr[0]]:
			Helper(arr[1:], d, path + char, res)

	if not digits : raise ValueError 
	d = {'1' : 'abc', '2' : 'def'}
	res = []
	Helper(digits, d, '', res)
	return res 

def Diamonds(arr, mins):
	if not arr : raise ValueError
	pq = []
	for num in arr : heapq.heappush(pq, -num)
	res = 0 
	count = 0 
	while count < mins:
		count += 1
		tmp = heapq.heappop(pq)
		res += (-tmp)
		tmp = (-tmp)//2
		heapq.heappush(pq, -tmp)
	return res 

def MaximumCommonSubarray(x, y):
	if not x or not y : raise ValueError 
	m, n = len(x), len(y)
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	res = 0 
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] == y[j - 1] : dp[i][j] = dp[i - 1][j - 1] + 1 
			res = max(res, dp[i][j])
	return res 

def NumSplits(arr, maxOps):
	if not arr : raise ValueError 
	l, h = 1, max(arr)
	while h >= l :
		mid = l + (h - l)//2
		if sum([num - 1//mid for num in arr]) <= maxOps:
			res = mid 
			h = mid - 1 
		else:
			l = mid + 1 
	return res 

class MedianInStream:
	def __init__(self):
		self.small = []
		self.large = []

	def Add(self, num):
		def Helper(small, large):
			if len(small) == len(large):
				heapq.heappush(small, -num)
				heaqp.heappush(large, -heaqp.heappop(small))
			else:
				heaqp.heappush(large, num)
				heaqp.heappush(small, -heapq.heappop(large))
		Helper(self.small, self.large)

	def median(self):
		if len(self.large) == len(self.small):
			return (self.large[0] + -self.small[0])//2
		else:
			return self.large[0]

class LargestInStream:
	def __init__(self, arr, k):
		self.arr = arr
		self.k = k 
		heapq.heapify(self.arr)
		while len(self.arr) > k:
			heapq.heappop(self.arr)
	
	def AddAndExtract(self, num):
		if len(self.arr) < k : heapq.heappush(self.arr, num)
		else:
			if num > self.arr[0]:
				heapq.heapreplace(self.arr, num)
		return self.arr[0]

def ReverseStackInPlace(arr):
	def Helper(arr, ele):
		if not arr:
			arr.append(ele)
			return 
		curr = arr.pop()
		Helper(arr, ele)
		arr.append(curr)
		return 

	if not arr:
		return 
	ele = arr.pop()
	ReverseStackInPlace(arr)
	Helper(arr, ele)
	return arr 

def ContiguosArray(arr):
	if not arr : raise ValueError 
	Sum = 0 
	res = 0 
	d = {0 : - 1}
	for i in range(len(arr)):
		if arr[i] == 0 : Sum -= 1 
		else : Sum += 1 
		if Sum in d : res = max(res, i - d[Sum])
		else : d[Sum] = i 
	return res 

def SortKSortedArray(arr, k):
	if not arr : raise ValueError 
	idx = 0 
	pq = arr[:k]
	heapq.heapify(pq)
	for i in range(k, len(arr)):
		arr[idx] = heapq.heappop(pq)
		heapq.heappush(pq, arr[i])
		idx +=1 
	while pq:
		arr[idx] = heapq.heappop(pq)
		idx +=1 
	return arr 

def MaximiseSubarraySum(arr, subs):
	def Helper(arr, mid, subs):
		curr_sub = 1 
		curr_sum = 0 
		for  i in range(len(arr)):
			curr_sum += arr[i]
			if curr_sum > mid:
				curr_sum = arr[i]
				curr_sub += 1 
			if curr_sub > subs : return False 
		return True 
	if not arr : raise ValueError
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if Helper(arr, mid, subs):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 



