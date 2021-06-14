def QuickSort(arr):
	if len(arr) == 0 :
		return -1 
	return QuickSortUtil(arr, 0, len(arr) - 1)

def QuickSortUtil(arr, l, h):
	if h < l : return 
	if h >= l:
		mid = partition(arr, l, h)
		QuickSortUtil(arr, l, mid - 1)
		QuickSortUtil(arr, mid + 1, h)
	return 

def partition(arr, l, h):
	i = l - 1
	pivot = arr[h]
	for j in range(l, h):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[h] = arr[h], arr[i + 1]
	return i + 1

def Heapsort(arr):
	if len(arr) == 0 : return - 1
	for i in range(len(arr) - 1//2, -1, -1):
		Heapify(arr, len(arr), i)
	for i in range(len(arr) - 1, 0, - 1):
		arr[i], arr[0] = arr[0], arr[i]
		Heapify(arr, i, 0)

def Heapify(arr, n, i):
	large = i 
	l = 2 * i + 1
	r = 2 * i + 2
	if l < n and arr[large] < arr[l]:
		large = l 
	if r < n and arr[large] < arr[r]:
		large = r 
	if large != i :
		arr[i], arr[large] = arr[large], arr[i]
		Heapify(arr, n, large)

def Mergesort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		l = arr[:mid]
		r = arr[mid:]
		Mergesort(l)
		Mergesort(r)
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

def NextPartition(arr):
	if len(arr) == 0 : return - 1
	i, j = len(arr) - 1, len(arr) - 1
	while i >= 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i == 0:
		arr.reverse()
		return arr 
	k = i - 1
	while arr[j] <= arr[k]:
		j -= 1
	arr[k], arr[j] = arr[j], arr[k]
	l, h = k + 1, len(arr) - 1
	while h > l :
		arr[l], arr[h] = arr[h], arr[l]
		l += 1
		h -= 1
	return 

def MergeIntervals(arr):
	if len(arr) == 0 :
		return - 1
	merged = []
	for sch in arr:
		if not merged or merged[-1][1] < sch[0]:
			merged.append(sch)
		elif merged[-1][1] > sch[0]:
			merged[-1][0] = min(merged[-1][0], sch[0])
			merged[-1][1] = max(merged[-1][0], sch[1])
	return merged 

def CookChef(arr, p):
	if len(arr) == 0 : return - 1
	l, h = 0, 1e8 
	while h >= l:
		mid = l + (h - l)//2
		if IsValid(arr, p, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return int(res)

def IsValid(arr, p, time):
	curr_p = 0
	for i in range(len(arr)):
		curr_time = arr[i]
		j = 2
		while curr_time <= time :
			curr_time += arr[i]*j
			j += 1
			curr_p += 1
		if curr_p >= p : return True 
	return False 

def Boats(arr, days):
	if len(arr) == 0 :
		return - 1
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if IsValidBoat(arr, days, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def IsValidBoat(arr, day, max_wt):
	curr_wt, curr_day = 0, 1 
	for i in range(len(arr)):
		curr_wt += arr[i]
		if curr_wt > max_wt:
			curr_day += 1
			curr_wt = arr[i]
		if curr_day > day : return False 
	return True 

def PagePartition(arr, stu):
	if len(arr) == 0 :
		return -1 
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if IsValidPartition(arr, stu, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def IsValidPartition(arr, stu, max_part):
	curr_stu, curr_part = 1, 0 
	for i in range(len(arr)):
		curr_part += arr[i]
		if curr_part > max_part:
			curr_part = arr[i]
			curr_stu += 1
		if curr_stu > stu : return False 
	return True 

def Subsets(arr):
	return [[arr[i] for i in range(len(arr)) if bit & 1 <<i != 0] for bit in range(1<<len(arr))]

def Subsets2(arr):
	if len(arr) == 0 : return -1 
	sol = [[]]
	for num in arr:
		sol += [current + [num] for current in sol]
	return sol 

def Permutations(arr):
	if len(arr) == 0 :
		return  -1 
	res = []
	Permutate(arr, [], res)
	return res 

def Permutate(arr, path, res):
	if not arr:
		res.append(path)
	for i in range(len(arr)):
		Permutate(arr[:i] + arr[i + 1:], path + [arr[i]], res)

def CombinationSum(arr, target):
	if len(arr) == 0 : return - 1
	res = []
	Combine(arr, target, 0, [], res)
	return res 

def Combine(arr, target, idx, path, res):
	if target < 0 : return 
	if target == 0:
		res.append(path)
		return 
	for i in range(idx, len(arr)):
		Combine(arr, target - arr[i], i, path + [arr[i]], res)

def Partitions(O, P):
	if P == 1:
		return 1
	if P == 0 or O < 0 :
		return 0 
	return Partitions(O - P, P) + Partitions(O, P - 1)


def TScheduler(schedule, process):
	if not schedule or not process : return [False]
	dp = [0 for _ in range(1441)]
	for i, j in schedule:
		dx = time(i) # Integer conversion to minutes
		dy = time(j)
		for itr in range(dx, dy + 1):
			dp[itr] = 1 
	res = []
	for i, j in process:
		dx = time(i)
		dy = time(j)
		flag = 0 
		for tmp in range(dx + 1, dy + 1):
			if dp[tmp] == 1: flag = 1
		if not flag : 
			res.append(True)
			for tmp in range(dx, dy + 1):
				dp[tmp] = 1
		else:
			res.append(False)
	return res


def time(sti):
	h, m = sti.split(':')
	m = m[:2]
	minutes = int(h)*60 + int(m)
	return minutes % 1440


def Knapsack(arr, val, max_wt):
	if not wt or not val : return - 1
	return KnapsackUtil(arr, val, max_wt, len(arr))

def KnapsackUtil(arr, val, max_wt, n):
	if not n or not max_wt : return 0 
	if arr[n - 1] <= max_wt:
		return max(val[n - 1] + KnapsackUtil(arr, val, max_wt - arr[n - 1], n - 1), KnapsackUtil(arr, val, max_wt, n - 1))
	else:
		return KnapsackUtil(arr, val, max_wt, n - 1)

def KnapsackDp(arr, val, max_wt):
	if not max_wt or not val : return -1 
	dp = [[0 for _ in range(max_wt + 1)] for _ in range(len(arr) + 1)]
	for i in range(1, len(arr) + 1):
		for j in range(max_wt + 1):
			if arr[i - 1] <= j :
				dp[i][j] = max(val[i - 1] + dp[i - 1][j - arr[i - 1]], dp[i - 1][j])
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[len(arr)][max_wt]

def SumSubset(arr, target):
	if not arr or not target : return -1 
	return SumSubsetUtil(arr, target, len(arr))

def SumSubsetUtil(arr, target, n):
	if not n and target : return False 
	if not target and n : return True 
	if arr[n - 1] <= target :
		return SumSubsetUtil(arr, target - arr[n - 1], n - 1) or SumSubsetUtil(arr, target, n - 1)
	else:
		return SumSubsetUtil(arr, target, n - 1)

def EqualSubset(arr):
	if not arr : return - 1
	target = sum(arr)
	if target & 1 : return False 
	target >>= 1
	return SumSubsetUtil(arr, target, len(arr))

def CountSubsets(arr, target):
	if not arr : return -1 
	return CountSubsetsUtil(arr, target, len(arr))

def CountSubsetsUtil(arr, target, n):
	if not n and target : return 0 
	if not target and n : return 1 
	if arr[n - 1] <= target:
		return CountSubsetsUtil(arr, target - arr[n - 1], n - 1) + CountSubsetsUtil(arr, target, n - 1)
	else:
		return CountSubsetsUtil(arr, target, n - 1)



