def Kadens(arr):
	if not arr : raise ValueError
	i = arr[0]
	j = 0 
	start, end, tmp = 0, 0, 0
	for k in range(len(arr)):
		j += arr[k]
		if i < j:
			i = j 
			start = tmp 
			end = k
		if j < 0 :
			j = 0 
			tmp = i 
	return (i, start, end)

def BubbleSort(arr):
	if not arr : raise ValueError
	for i in range(len(arr)):
		for j in range(len(arr) - i - 1):
			if arr[j + 1] < arr[j]:
				arr[j + 1], arr[j] = arr[j], arr[j + 1]
	return arr 

def MergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
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
		while i < len(l) :
			arr[k] = l[i]
			k+= 1
			i += 1
		while j < len(r):
			arr[k] = r[j]
			j += 1
			k ++ 1
		return arr 

def QuickSort(arr):
	if not arr : raise ValueError
	def partition(arr, l, h):
		if h < l : return 
		i = l - 1
		pivot = arr[h]
		for x in range(l, h):
			if arr[x] <= pivot:
				i +=1
				arr[x], arr[i] = arr[i], arr[x]
		arr[i + 1], arr[h] = arr[h], arr[i + 1]
		return i +1 

	def Helper(arr, l, h):
		if h < l : return 
		while h >= l :
			mid = partition(arr, l, h)
			Helper(arr, l, mid - 1)
			Helper(arr, mid + 1, h)
			return 

	Helper(arr, 0, len(arr) - 1)
	return arr 

def HeapSort(arr):
	def Heapify(arr, n, i):
		large = i 
		l = 2 * i + 1
		r = 2 * i + 2
		if l < n and arr[large] < arr[l]:
			large = l 
		if r < n and arr[large] < arr[r]:
			large = r 
		if large != i:
			arr[large], arr[i] = arr[i], arr[large]
			Heapify(arr, n, large)
	if not arr : raise ValueError
	for i in range(len(arr) - 1//2, -1, -1):
		Heapify(arr, len(arr), i)
	for i in range(len(arr) -1 , 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		Heapify(arr, i, 0)
	return arr 

def Subsets(arr):
	if not arr : raise ValueError 
	sol = [[]]
	for num in arr:
		sol += [current + [num] for current in sol]
	return sol 

def Subsets2(arr):
	return [[arr[i] for i in range(len(arr)) if bit & 1 << i != 0] for bit in range(1<<len(arr))]

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

def NextGreatestPerm(arr):
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
	arr[k], arr[j] = arr[j], arr[k]
	l, h = k + 1, len(arr) - 1
	while h >l :
		arr[l], arr[h] = arr[h], arr[l]
		l += 1 
		h -= 1
	return arr 

def ProductArray(arr):
	if not arr : raise ValueError 
	res = [1]*len(arr)
	for i in range(1, len(arr)):
		res[i] = res[i - 1] * arr[i - 1]
	prod = 1 
	for i in range(len(arr) - 1, -1, -1):
		res[i] = res[i] * prod 
		prod = prod * arr[i]
	return res 

def PeakElement(arr):
	if not arr : raise ValueError 
	l, h = 0, len(arr) - 1
	while h >= l:
		mid = l + (h - l)//2
		if mid != 0 and mid != len(arr) - 1:
			if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
				return mid 
			elif arr[mid - 1] > arr[mid]:
				h = mid - 1
			else:
				l = mid + 1
		elif mid == 0 :
			if arr[mid] > arr[mid + 1] : return mid 
			else : return mid + 1 
		elif mid == len(arr) - 1:
			if arr[mid - 1] < arr[mid] : return mid 
			else: return mid -1 

	return -1

def SubarrayWhichSorts(arr):
	if not arr : raise ValueError
	l, h = 0, len(arr) - 1
	while l < len(arr) - 1 and arr[l + 1] >= arr[l] :
	 	l += 1
	while h >= 0 and arr[h - 1] <= arr[h]:
	 	h -= 1
	mini, maxi = min(arr[l  + 1: h]), max(arr[l + 1: h])
	for x in range(0, l):
	 if arr[x] > maxi:
	 	l = x 
	for x in range(h, len(arr)):
	 if arr[x] < mini :
	 	h = x 
	return l, h 

def Rotate(arr, k):
	def reverse(arr, l, h):
		while h > l :
			arr[h], arr[l] = arr[l], arr[h]
			h -= 1
			l += 1

	if not arr : raise ValueError
	l, h = 0 , len(arr) - 1
	k = k % len(arr)
	mid = h - k 
	reverse(arr, l, mid)
	reverse(arr, mid + 1, h)
	reverse(arr, l, h)
	return arr

def AlternatingPosAndNegs(arr):
	if not arr : raise ValueError
	def Helper(arr):
		i, j = 0, len(arr) - 1
		while i <= j:
			while arr[i] >= 0 : i += 1
			while arr[j] < 0 : j -= 1
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1
		return i, arr 

	i, arr = Helper(arr)
	k = 1 
	while i < len(arr):
		arr[k], arr[i] = arr[i], arr[k]
		k += 2 
		i += 1
	return arr 

def DutchFlag(arr):
	def swap(arr, l, h):
		arr[l], arr[h] = arr[h], arr[l]

	if not arr : raise ValueError 
	l, mid, h = 0, 0 , len(arr) - 1
	while mid <= h:
		if arr[mid] == 0 :
			swap(arr, l, mid)
			l += 1
			mid += 1
		if arr[mid] == 1:
			mid += 1
		else:
			swap(arr, h, mid)
			h -= 1
	return arr 

def Floyds(arr):
	if not arr : raise ValueError
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

def EqualPilesHeight(arr):
	if not arr : raise ValueError
	arr.sort(reverse = True)
	count = 0 
	for i in range(1, len(arr)):
		if arr[i - 1] != arr[i]:
			count += i 
	return count 

def Houses(arr):
	if not arr : raise ValueError 
	q = []
	for i in range(len(arr)):
		if arr[i] > b:
			continue 
		ini = arr[i]
		count = 1
		for j in range(len(arr)):
			if i == j :
				continue 
			if arr[j] + ini <= b:
				ini += arr[j]
				count += 1
		q.append(count)
	res = q[0]
	for i in range(len(q)):
		res = max(res, q[i])
	return res 

def BA(n):
	def Helper(arr, path, res, idx):
		if not arr:
			res.append(path)
			return 
		for j, num in enumerate(arr):
			if num % idx == 0 or idx % num == 0 :
				Helper(arr[:j] + arr[j + 1:], path + [arr[j]], res, idx + 1)

	if not n : raise ValueError
	arr = [i for i in range(1, n + 1)]
	idx = 1 
	res = []
	Helper(arr, [], res, idx)
	return len(res)

def SquarePerms(arr):
	def isSq(x):
		return int(x**0.5)**2 == x 

	def Helper(arr, path, res):
		if not arr :
			res.append(path)
			return 
		for i in range(len(arr)):
			if i > 0 and arr[i - 1] == arr[i]:
				continue 
			if path and not isSq(path[-1] + arr[i]):
				continue 
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)
	if not arr : raise ValueError
	res = []
	Helper(arr, path, res)
	return res 

def dupsperms(arr):
	def Helper(arr, path, res):
		if not arr:
			res.append(path)
			return 
		for i in range(len(arr)):
			if i > 0 and arr[i - 1] == arr[i]:
				continue 
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

	if not arr : raise ValueError 
	res = []
	Helper(arr, [], res)
	return res 

def MergedIntervals(arr):
	if not arr : raise ValueError 
	arr = sorted(arr)
	merged = []
	for i in arr:
		if not merged or merged[-1][1] < i[0]:
			merged.append(i)
		else:
			merged[-1][1] = max(merged[-1][1], i[1])
	return merged 

def ThreeSum(arr):
	if not arr : raise ValueError 
	n, p, z = [], [], []
	for num in arr:
		if num < 0 : n.append(num)
		elif num > 0 : p.append(num)
		else : z.append(num)
	res = set()
	N, P = set(n), set(P)
	if z :
		for num in p:
			if -num in N:
				res.add((num, 0, -num))
	if len(z) >= 3 : res.add((0, 0, 0))
	for i in range(len(p)):
		for j in range(i + 1, len(p)):
			target = p[i] + p[j]
			if -target in N:
				res.add(tuple(sorted([p[i], p[j], target])))

	for i in range(len(n)):
		for j in range(i + 1, len(n)):
			target = n[i] + n[j]
			if -target in P:
				res.add(tuple(sorted([n[i], n[j], target])))
	return res 

def SubsetsEqualK(arr, k):
	if not arr : raise ValueError
	prefix = 0 
	count = 0 
	d = {0 : 1}
	for num in arr:
		prefix += num 
		if prefix - k in d:
			count += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1
	return count 

def DivisibleByK(arr, k):
	if not arr : raise ValueError
	prefix = 0 
	count = 0 
	d = {0 : 1}
	for num in arr:
		prefix += num 
		key = prefix % k 
		if key in d:
			count += d[key]
		d[key] = d.get(key, 0) + 1
	return count 

def PairEqualSum(arr, target):
	if not arr : raise ValueError
	d = {}
	for i in range(len(arr)):
		if target - arr[i] in d:
			return d[target - arr[i]], i 
		d[arr[i]] = i 
	return -1 

def pairMultiplyToTarget(arr, target):
	if not arr : raise ValueError
	d = {}
	for i in range(len(arr)):
		if target //arr[i] in d and target % arr[i] == 0 : return d[target // arr[i]], i 
		d[arr[i]] = i 
	return -1 

def MinimumLengthSubarray(arr, target):
	if not arr : raise ValueError
	l, r, res, prefix = 0, 0, len(arr) + 1, 0 
	while r < len(arr):
		prefix += arr[r]
		while prefix > target:
			prefix -= arr[l]
			res = min(res, r - l + 1)
			l += 1 
		r += 1
	return res 

def BeautifulArrangements2(n, k):
	if not n : raise ValueError
	arr = [i for i in range(1, n + 1)]
	for i in range(1, k):
		arr[i : ] = arr[:i - 1: -1 ]
	return arr

def MinOpsincreasing(arr):
	if not arr : raise ValueError
	count = 0 
	for i in range(1, len(arr)):
		if arr[i - 1] >= arr[i]:
			diff = arr[i - 1] - arr[i] + 1
			count += diff 
			arr[i] = arr[i - 1] + 1
	return count 

def MaximumProductArray(arr):
	if not arr : raise ValueError
	rev_arr = arr[::-1]
	for i in range(1, len(arr)):
		arr[i] *= arr[i - 1] or 1 
		rev_arr[i] *= rev_arr[i - 1] or 1 
	return max(arr + rev_arr)

def SubarrayCountWithKdistinctElements(arr, k):
	if not arr : raise ValueError
	def Helper(arr, k):
		l, r, count, res = 0, 0, 0, 0
		d = {}
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1
			if d[arr[r]] == 1: count += 1
			while l < r and count > k:
				d[arr[l]] -= 1 
				if d[arr[l]] == 0 : count -=1 
				l += 1
			res += r - l 
			r += 1
		return res

	return Helper(arr, k) - Helper(arr, k - 1) 

def NiceSubarrays(arr, k):
	if not arr : raise ValueError
	def Helper(arr, k):
		r, l, count, res = 0, 0, 0, 0
		while r < len(arr) : 
			if arr[r] % 2 == 1 : count += 1
			while l < r and count > k:
				if arr[l] % 2 == 1: count -=1 
				l += 1
			res += r - l 
			r += 1
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def PascalsTraingle(arr, row):
	if not arr : raise ValueError
	my_row = [1]
	for _ in range(row):
		my_row = [x + y for x, y in zip(my_row + [0], [0] + my_row)]
	return my_row 

def MaxWaterContainer(arr):
	if not arr : raise ValueError
	water = 0 
	i, j = 0, len(arr) - 1
	while i < j :
		water = max(water, (j - i) * min(arr[i], arr[j]))
		if arr[i] < arr[j]:
			i += 1
		else:
			j -=1 
	return water 

def Boats(arr, day):
	def Helper(arr, day, mid):
		curr_wt = 0 
		curr_day = 1 
		for i in range(len(arr)):
			curr_wt += arr[i]
			if curr_wt > mid:
				curr_wt = arr[i]
				curr_day += 1
			if curr_day > day : return False 
		return True 

	if not arr : raise ValueError
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2 
		if Helper(arr, day, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def PaintersPartition(arr, stu):
	def Helper(arr, stu, mid):
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
		if Helper(arr, stu, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def CookChef(arr, p):
	def Helper(arr, p, mid):
		curr_p = 1 
		for i in range(len(arr)):
			time = arr[i]
			j = 2 
			while time <= mid:
				time += arr[i] * j 
				j += 1 
				curr_p += 1
			if curr_p >= p : return True 
		return False 

	if not arr : raise ValueError
	l, h = 0, 1e8
	while h >= l :
		mid = l + (h - l)//2 
		if Helper(arr, p, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

import heapq
def LastStoneWeight(arr):
	if not arr : raise ValueError
	arr = [-x for x in arr]
	heapq.heapify(arr)
	while len(arr) > 1 and arr[0] != 0:
		heapq.heappush(arr, heapq.heappop(arr) - heapq.heappop(arr))
	return -arr[0]

def Stocks1(arr):
	if not arr : raise ValueError
	profit = 0 
	res = float('inf')
	for price in arr:
		min_price = min(price, min_price)
		profit = price - min_price
		res = max(res, profit)
	return res 

def Stocks2(arr):
	if not arr : raise ValueError
	return sum([tomorrow - today for today, tomorrow in zip(arr, arr[1:]) if tomorrow - today > 0])

def IsValidMountain(arr):
	if not arr : raise ValueError
	i, j = 0, len(arr) - 1
	while arr[i + 1] > arr[i] and i < len(arr) - 1:
		i += 1
	while arr[j - 1] > arr[j] and j > 0 :
		j -= 1
	if i == j and i != 0 : return True 
	return False 

def LongestMountain(arr):
	if not arr : raise ValueError
	res = 0 
	for i in range(1, len(arr) - 1):
		if arr[i - 1] < arr[i] > arr[i + 1]:
			l = r = i 
			while l and arr[l - 1] < arr[l] : l -= 1
			while r + 1 < len(arr) and arr[r] < arr[r + 1] : r += 1
			if r - l + 1 > res : res = r - l + 1
	return res 

def GreyCode(n):
	if not n : raise ValueError 
	res = [1]
	for i in range(n):
		res.append(res[i] ^ [i & ~i + 1])
	return res 


'''

#KADENS 
a=[123,2324,3212,32,-132,-12312,234,-213,23,232,-23,12,3123,12,-23,13,-32134324]
print(Kadens(a)) # (5691, 0, 3)

arr = [123,2324,3212,32,-132,-12312,234,-213,23,232,-23,12,3123,12,-23,13,-32134324]
print(BubbleSort(arr))
print(HeapSort(arr))
print(MergeSort(arr))
print(QuickSort(arr))

# Subsets with bitmask 
print(Subsets([1,2, 3]))

# Subsets 
print(Subsets2([1,2,3]))

# Permutations
print(Perms([1,2,3]))

# Max Product Subarray 
arr = [2,3,-2,4]
print(MaximumProductArray(arr)) # 6


# Beautiful Arrangement 
print(BA(6)) # 36 

# Beautiful arrangeent 2 
print(BeautifulArrangements2(3, 2)) # [1, 3, 2]

# Two sum 
target = 14
arr = [2, 3, 4, 5, 6, 7, 8] # (4, 6)
print(PairEqualSum(arr, target))

# Subarray Sum equal to k 
arr = [1, 2, 3]
k = 3
print(SubsetsEqualK(arr, k)) # 2

# subarray sum divisble by k 
arr = [4,5,0,-2,-3,1]
k = 5 
print(DivisibleByK(arr, k)) # 7 

# Product Array 
arr = [1, 2, 3, 4, 5]
print(ProductArray(arr)) # [120, 60, 40, 30, 24]


# Rotate 
arr = [1,2,3,4,5,6,7]
k = 3
print(Rotate(arr, k)) # [5,6,7,1,2,3,4]

# Cook Chef 
arr = [1, 2, 3, 4]
p = 10
print(CookChef(arr, p)) # 12 

# Boats 
arr = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(Boats(arr, D)) # 15

# Painters 
arr = [15, 17, 20]
k = 2 
print(PaintersPartition(arr, k)) # 32

# Next Permutation 
arr = [1,1,5]
print(NextGreatestPerm(arr)) # [1, 5, 1]

# Peak Element 
arr = [2, 23, 90, 67]
print(PeakElement(arr)) # 90

# Subarray Sorts the array
arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
print(SubarrayWhichSorts(arr)) # (30, 35) => Nums ; (3, 8) => Indices

# Piles 
print(EqualPilesHeight([5, 2, 1]))

# Min operations to make array strictly increasing 
arr = [1, 1, 1]
print(MinOpsincreasing(arr))  # 3

# Product Search 
arr = [2, 3, 4, 5, 6]
target = 20
print(pairMultiplyToTarget(arr, target)) # (2, 3)

# Alternating Negative and Positive 
arr = [1, 2, 3, -4, -1, 4]
print(AlternatingPosAndNegs(arr)) # [-1, 2, -4, 4, 1, 3]

#Dutch Flag 
arr = [0, 1, 2, 1, 1, 0, 0, 2, 1, 1, 0, 1, 2, 1]
print(DutchFlag(arr))

# Floyds
arr = [1, 3, 2, 5, 4, 1, 6]
print(Floyds(arr)) # 1 


'''
