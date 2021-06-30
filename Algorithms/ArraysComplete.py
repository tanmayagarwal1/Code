import heapq 
def Kadens(arr):
	if len(arr) == 0 : return - 1
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
			tmp = k 
	return i, start, end 

def QuickSort(arr):
	if len(arr) == 0 : return - 1

	def partition(arr, l, h):
		if h < l : return 
		i = l - 1 
		pivot = arr[h]
		for x in range(l, h):
			if arr[x] <= pivot:
				i += 1
				arr[x], arr[i] = arr[i], arr[x]
		arr[i + 1], arr[h] = arr[h], arr[i + 1]
		return i + 1

	def QuickSortUtil(arr, l, h):
		if h < l : return 
		if h >= l :
			mid = partition(arr, l, h)
			QuickSortUtil(arr, l, mid - 1)
			QuickSortUtil(arr, l, mid + 1)

	QuickSortUtil(arr, 0, len(arr) - 1)
	return arr 

def HeapSort(arr):
	if len(arr) == 0 : return -1 

	def Heapify(arr, n, i):
		large = i 
		l = 2 * i + 1
		r = 2 * i + 2 
		if l < n and arr[large] < arr[l]:
			i = l 
		if r < n and arr[large] < arr[r]:
			large = r 
		if large != i :
			arr[i], arr[large] = arr[large], arr[i]
			Heapify(arr, n, large)

	for i in range(len(arr) - 1//2, -1, -1):
		Heapify(arr, len(arr), i)
	for i in range(len(arr) - 1, 0 , -1):
		arr[0], arr[i] = arr[i], arr[0]
		Heapify(arr, i, 0) 
	return arr 

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
		return arr 

def BubbleSort(arr):
	if len(arr) == 0 : return -1 
	for i in range(len(arr)):
		for j in range(len(arr) - i - 1):
			if arr[j + 1] < arr[j]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr 

def Subsets(arr):
	return [[arr[i] for i in range(len(arr)) if bit & 1<<i != 0]for bit in range(1<<len(arr))]

def Subsets2(arr):
	if len(arr) == 0  : return -1 
	sol = [[]]
	for num in arr:
		sol += [curr + [num]for curr in sol]
	return sol 

def Permutations(arr):
	if len(arr) == 0 :
		return - 1
	res = []
	Permutate(arr, [], res)
	return res 

def Permutate(arr, path, res):
	if not arr : 
		res.append(path)
		return 
	for i in range(len(arr)):
		Permutate(arr[:i] + arr[i + 1:], path + [arr[i]], res)

def NextPermutation(arr):
	if not arr : return 0 
	i = j = len(arr) - 1
	while i >= 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i == 0:
		arr.reverse()
		return arr 
	pivot = i - 1
	while arr[j] <= arr[pivot]:
		j -= 1
	arr[pivot], arr[j] = arr[j], arr[pivot]
	l, h = pivot + 1, len(arr) - 1
	while h > l :
		arr[h], arr[l] = arr[l], arr[h]
		l += 1
		h -= 1
	return arr 

def KthLeagrest(arr, k):
	if len(arr) == 0 : raise ValueError
	heapq.heapify(arr)
	return arr[-k]

def Beautifularrangements(n):
	if not n : raise ValueError
	arr = [i for i in range(1, n + 1)]
	res = []

	def Helper(arr, path, res, idx):
		if not arr:
			res.append(path)
			return 
		for j, num in enumerate(arr):
			if num % idx == 0 or idx % num == 0 :
				Helper(arr[:j] + arr[j + 1:], path + [arr[j]], res, idx + 1)

	Helper(arr, [], res, 1)
	return len(res)

def ProductArray(arr):
	if not arr : return -1 
	res = [1]*len(arr)
	for i in range(1, len(arr)):
		res[i] = arr[i - 1] * res[i - 1]
	prod = 1 
	for i in range(len(arr) - 1, -1, -1):
		res[i] = res[i] * prod 
		prod = prod * arr[i]
	return res 

def EqualToK(arr, k):
	if not arr : return - 1
	d = {0 : 1}
	prefix, count = 0, 0 
	for num in arr:
		prefix += num 
		if prefix - k in d:
			count += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1
	return count 

def DivisibleK(arr, k):
	if not k : raise ValueError
	d = {0 : 1}
	prefix, count = 0, 0 
	for num in arr:
		prefix += num 
		key = prefix % k 
		if key in d:
			count += d[key]
		d[key] = d.get(key, 0) + 1
	return count 

def TwoSum(arr, target):
	if not arr : raise ValueError
	d = {}
	for num in arr:
		if target - num in d:
			return d[target - num], arr.index(num)
		d[num] = arr.index(num)
	return -1 

def PeakElement(arr):
	if not arr : return - 1
	l, h = 0, len(arr) - 1
	while h >= l :
		mid = l + (h - l)//2
		if mid != 0 and mid != len(arr) - 1:
			if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
				return [mid]
			elif arr[mid - 1] > arr[mid] : h = mid - 1
			else: l = mid + 1
		elif mid == 0 :
			if arr[mid] >arr[mid + 1] : return arr[mid]
			else: return arr[mid + 1]
		elif mid == len(arr) - 1:
			if arr[mid] > arr[mid - 1] : return arr[mid]
			else: return arr[mid - 1]
	return - 1

def SubarraySorts(arr):
	if len(arr) == 0 : return - 1
	i, j = 0, len(arr) - 1
	while i < len(arr) and arr[i + 1] > arr[i]:
		i += 1
	while j >= 0 and arr[j] > arr[j - 1]:
		j -= 1
	mini, maxi = min(arr[i:j]), max(arr[i:j])
	for x in range(0, i):
		if arr[x] > maxi:
			i = x 
	for x in range(j, len(arr)):
		if arr[x] < mini:
			j = x 
	return i, j 

def Product(arr, target):
	if not arr : raise ValueError
	d = {}
	for num in d:
		if target //num in d and taregt % num == 0 :
			return True 
		d[num] = num 
	return False 

def AlternatePositiveAndNegative(arr):
	if len(arr) == 0 : return -1 

	def Helper(arr):
		l, h = 0, len(arr) - 1
		while l <= h :
			while arr[l] >= 0 :
				l += 1
			while arr[h] < 0 : 
				h -= 1
			arr[l], arr[h] = arr[h], arr[l]
		return arr, l 

	arr, i = Helper(arr)
	j = 0 
	while i < len(arr):
		arr[j], arr[i] = arr[i], arr[j]
		j += 2 
		i += 1
	return arr 

def DutchFlag(arr):
	if not arr : return 
	l, mid, h = 0, 0, len(arr) - 1

	def swap(arr, l, h):
		arr[l], arr[h] = arr[h], arr[l]
		return 

	while h >= mid:
		if arr[mid] == 0:
			swap(arr, l, mid)
			l += 1 
			mid += 1
		elif arr[mid] == 1:
			mid += 1
		else:
			swap(arr, h, mid)
			h -= 1
	return arr

def Floyd(arr):
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

def Boats(arr, days):
	if not arr : return -1 
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if IsValid(arr, days, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def IsValid(arr, days, mid):
	curr_wt = 0 
	day = 1 
	for i in range(len(arr)):
		curr_wt += arr[i]
		if curr_wt > mid:
			curr_wt = arr[i]
			day += 1
		if day > days : return False 
	return True 

def CookChef(arr, p):
	if not arr : return -1 
	l, h = 0, 1e8

	def Cook(arr, p, mid):
		curr_p = 1 
		for i in range(len(arr)):
			time = arr[i]
			j = 2 
			while time <= mid:
				time += arr[i]*j 
				j += 1 
				curr_p += 1
			if curr_p >= p : return True 
		return False 

	while h >= l :
		mid = l + (h - l)//2
		if Cook(arr, p, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def Partition(arr, stu):
	if len(arr) == 0 : return -1 
	l, h = max(arr), sum(arr)

	def Part(arr, stu, mid):
		curr_stu = 1 
		part = 0 
		for i in range(len(arr)) :
			part += arr[i]
			if part > mid:
				part = arr[i]
				curr_stu += 1
			if curr_stu > stu : return False 
		return True 

	while h >= l :
		mid = l + (h - l)//2
		if Part(arr, stu, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def MinimumLengthSubarray(arr, target):
	if not arr : raise ValueError
	prefix, l, res, r = 0, 0, len(arr) + 1, 0 
	for i in range(len(arr)):
		prefix += arr[i]
		while prefix >= target:
			res = min(res, i - l + 1)
			prefix -= arr[l]
			l += 1
		r += 1
	return res if res < len(arr) + 1 else 0 

def MinimumOpsIncreasing(arr):
	if not arr : return - 1
	count = 0 
	for i in range(1, len(arr)):
		if arr[i] <= arr[i - 1]:
			diff = arr[i - 1] - arr[i] + 1
			count += diff
			arr[i] = arr[i - 1] + 1
	return count 

def Houses(arr, b):
	if not arr : return 0 
	q = []
	for i in range(len(arr)):
		if arr[i] > b : continue 
		ini = arr[i]
		count = 1
		for j in range(len(arr)):
			if i == j : continue 
			if arr[j] + ini <= b:
				ini += arr[j]
				count += 1
		q.append(count)
	res = q[0]
	for i in range(len(q)):
		res = max(res, q[i])
	return res 

def PilesHeight(arr):
	arr.sort(reverse = True)
	count =0 
	for i in range(1, len(arr)):
		if arr[i] != arr[i - 1]:
			count += i 
	return count 

def Trips(arr):
	if not arr : return - 1
	arr.sort()
	for i in range(len(arr) - 1, 1, -1):
		j = 0 
		k = i - 1
		while j < k :
			if arr[j] + arr[k] == arr[i]:
				return True 
			else:
				if arr[j] + arr[k] < arr[i]:
					j += 1
				else:
					k -= 1
		return True 

def Rotate(arr, k):
	if not arr : return - 1
	k = k % len(arr)
	l, h = 0, len(arr) - 1
	mid = h - k - 1

	def Reverse(arr, l, h):
		if h < l : reuturn 
		while h > l :
			arr[h], arr[l] = arr[l], arr[h]
			h -= 1
			l += 1

	Reverse(arr, l, mid)
	Reverse(arr, mid + 1, h)
	Reverse(arr, l, h)
	return arr 

def Combinations(arr, target):
	if not arr : return - 1

	def combine(arr, target, idx, path, res):
		if target < 0 : return 
		if target == 0 :
			res.append(path)
			return 
		for i in range(idx, len(arr)):
			combine(arr, target - arr[i], i, path + [arr[i]], res)

	res = []
	combine(arr, target, 0, [], res)
	return res 

def Partitions(O, P):
	if P == 1 : return 1 
	if P == 0 or O < 0 : return 0 
	return Partitions(O - P, P) + Partitions(O, P - 1)

def MaxProdcutSubarray(arr):
	arr2 = arr[::-1]
	for i in range(1, len(arr)):
		arr[i] *= arr[i - 1] or 1 
		arr2[i] *= arr2[i -1] or 1 
	return max(arr + arr2)

def KDistinctElementsSubarrayCount(arr, k):
	if not arr : raise ValueError 
	def Helper(arr, k):
		l, r, count, res = 0, 0, 0, 0
		d = {}
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1
			if d[arr[r]] == 1: count += 1
			r += 1
			while l < r and count > k :
				d[arr[l]] -= 1
				if d[arr[l]] == 1 :
					count -=1 
				l += 1
			res += r - l 
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def ThreeSum(arr):
	res = set()
	if not arr : raise ValueError 
	n, p, z = [], [], []
	for num in arr:
		if num < 0 : n.append(num)
		elif num > 0 : p.append(num)
		else: z.append(num)

	N, P = set(n), set(p)
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	if len(z) >= 3 : res.add((0, 0, 0))
	for i in range(len(p)):
		for j in range(i + 1, len(p)):
			target = -1 * (p[i] + p[j])
			if target in N :
				res.add(tuple(sorted([p[i], p[j], target])))

	for i in range(len(n)):
		for j in range(i + 1, len(n)):
			target = -1*(n[i] + n[j])
			if target in P:
				res.add(tuple(sorted([n[i], n[j], target])))
	return res 

def MaxLengthSubarrayWithKDistinctelements(arr, k):
	if not arr : raise ValueError
	def Helper(arr , k):
		l, r, count, res = 0, 0, 0, 0
		d = {}
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0 ) + 1
			if d[arr[r]] == 1 : count += 1
			r += 1
			while l < r and count > k:
				d[arr[l]] -= 1
				if d[arr[l]] == 1: count -=1 
				l += 1
			res = max(res, r - l)
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def MaximumWaterContainer(arr):
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

def PasaclasTraingleNthRow(row):
	if not row : raise ValueError
	my_row = []
	for i in range(row):
		my_row = [x + y for x, y in zip([0] + my_row, my_row + [0])]
	return my_row 

def PermuatationwithDups(arr):
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

def SquarePerms(arr):
	def IsSquare(x):
		return int(x**0.5)**2 == x 
	def Helper(arr, path, res):
		if not arr:
			res.append(path)
			return 
		for i in range(len(arr)):
			if i < 0 and arr[i - 1] == arr[i]:
				continue 
			elif path and not IsSquare(arr[i] + path[-1]):
				continue
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

	if not arr : raise ValueError 
	res = []
	Helper(arr, [], res)
	return res 

'''
# Normal Permuatations 
print(Permutations([1,2,3]))

# Combinations
print(Combinations([2,3,4], 7))

# Subsets 
print(Subsets2([1,2,3]))

# Subsets with bitmask 
print(Subsets([1,2, 3]))

# Partitions 
print(Partitions(5, 3))

# Beautiful Arrangement 
print(Beautifularrangements(6)) # 36 

# Two sum 
target = 14
arr = [2, 3, 4, 5, 6, 7, 8] # (4, 6)
print(TwoSum(arr, target))

# Subarray Sum equal to k 
arr = [1, 2, 3]
k = 3
print(EqualToK(arr, k)) # 2

# subarray sum divisble by k 
arr = [4,5,0,-2,-3,1]
k = 5 
print(DivisibleK(arr, k)) # 7 

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
print(Partition(arr, k)) # 32

# Next Permutation 
arr = [1,1,5]
print(NextPermutation(arr)) # [1, 5, 1]

# Peak Element 
arr = [2, 23, 90, 67]
print(PeakElement(arr)) # 90

# Subarray Sorts the array
arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
print(SubarraySorts(arr)) # (30, 35) => Nums ; (3, 8) => Indices

# Piles 
print(PilesHeight([5, 2, 1]))

# Min operations to make array strictly increasing 
arr = [1, 1, 1]
print(MinimumOpsIncreasing(arr))  # 3

# Product Search 
arr = [2, 3, 4, 5, 6]
target = 20
print(Product(arr, target)) # (2, 3)

# Alternating Negative and Positive 
arr = [1, 2, 3, -4, -1, 4]
print(AlternatePositiveAndNegative(arr)) # [-1, 2, -4, 4, 1, 3]

# Kth Largest 
arr = [2, 4, 3, 1, 5, 7, 6]
print(KthLeagrest(arr, 3))

#Dutch Flag 
arr = [0, 1, 2, 1, 1, 0, 0, 2, 1, 1, 0, 1, 2, 1]
print(DutchFlag(arr))

# Floyds
arr = [1, 3, 2, 5, 4, 1, 6]
print(Floyd(arr))

# Minimum Length Subarrau
arr = [2,3,1,2,4,3]
target = 7 
print(MinimumLengthSubarray(arr, target)) # 2 

# TRIPS
a=[1,2,3,4,5,6,7,8,9]
print(Trips(a)) # True 

# Maximum Product Subarray 
arr = [2,3,-2,4]
print(MaxProdcutSubarray(arr)) # 6 

#Three Sum 
arr = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(ThreeSum(arr)) # {(-3, -1, 4), (-1, 0, 1), (-4, 1, 3), (-1, -1, 2), (-3, 1, 2), (-3, 0, 3), (-4, 0, 4), (-2, -1, 3), (-2, 0, 2)}

# K distinct elements subarray count 
arr = [1, 2, 1, 2, 3]
k = 2
print(KDistinctElementsSubarrayCount(arr, k)) # 13 

# Maximum length subarray with k distinct elements 
arr = [1, 2, 1, 2, 3]
k = 2
print(MaxLengthSubarrayWithKDistinctelements(arr, k)) # 3 

# Square Permuatations 
arr = [1, 17, 8]
print(SquarePerms(arr)) # [[1, 8, 17], [17, 8, 1]]

# Permutation with Duplicates 
arr = [1, 1, 2]
print(PermuatationwithDups(arr)) # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

# Max Water Container
arr = [1,8,6,2,5,4,8,3,7]
print(MaximumWaterContainer(arr)) # 49


'''



