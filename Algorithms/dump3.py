# Binary Search 

def BinarySearch(arr, k):
	if not arr : raise ValueError 
	l, h = 0, len(arr) - 1
	while h >= l :
		mid = l + (h - l)//2
		if arr[mid] == k :
			return mid 
		elif arr[mid] < target:
			l = mid + 1
		else:
			h = mid - 1
	return - 1

def PeakElement(arr):
	if not arr : raise ValueError
	l, h = 0, len(arr) - 1
	while h >= l :
		mid = l + (h - l)//2
		if mid != 0 and mid != len(arr) - 1:
			if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
				return mid 
			elif arr[mid - 1] > arr[mid]:
				h = mid - 1
			else:
				l = mid + 1
		elif mid == len(arr) - 1:
			if arr[mid] > arr[mid - 1] : return mid 
			else : return mid - 1
		else:
			if arr[mid] > arr[mid + 1] : return mid 
			else : return mid + 1
	return - 1

def FirstOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return - 1
		while h >= l :
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid ==0):
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
		if idx != -1:
			break 
	return i, idx 

def MaxOccurance(grid):
	def Helper(arr, l, h):
		if h < l : return 
		while h >= l :
			mid = l + (h - l)//2
			if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
				return mid 
			elif arr[mid] == 0 :
				l = mid + 1
			else:
				h = mid - 1
		return - 1

	m, n, res = len(grid), len(grid[0]), 0
	if m == 0 or n == 0 : raise ValueError
	for i in range(m):
		idx = Helper(grid[i], 0, n - 1)
		if idx != -1 :
			count = n - idx 
			if count > res:
				res = count 
				my_idx = i 
	return res, my_idx 

def CookChef(arr, p):
	def Helper(arr, mid, p):
		curr_p = 0 
		curr_time = 0 
		for i in range(len(arr)):
			curr_time += arr[i]
			j = 2 
			while curr_time <= mid:
				curr_time += arr[i] * j 
				j += 2 
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

def Partition(arr, stu):
	def Helper(arr, mid, stu):
		curr_stu = 1
		curr_part = 0 
		for i in range(len(arr)):
			curr_part += arr[i]
			if curr_part > mid:
				curr_part = arr[i]
				curr_stu += 1 
			if curr_stu > curr_part : return False 
		return True 

	if not arr : raise ValueError 
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if Helper(arr, mid, stu):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def Rotate(arr, k):
	def reverse(arr, l, h):
		if h < l : return 
		while h > l :
			arr[l], arr[h] = arr[h], arr[l]
			l += 1
			h -= 1

	if not arr : raise ValueError 
	l, h = 0, len(arr) - 1
	k = k % len(arr)
	mid = h - k 
	reverse(arr, l, mid)
	reverse(arr, mid + 1, h)
	reverse(arr, l, h)
	return arr 

def Minimum(arr):
	if not arr : raise ValueError 
	l, h = 0, len(arr) - 1
	while h >= l :
		if arr[l] <= arr[h]:
			return l 
		mid = l + (h - l)//2
		ne = (mid + 1) % len(arr)
		prev = (mid + len(arr) - 1) % len(arr)
		if arr[mid] < arr[ne] and arr[mid] < arr[prev]:
			return mid 
		elif arr[l] <= arr[mid]:
			l = mid + 1
		elif arr[mid] <= arr[h]:
			h = mid - 1
	return None 

def Search(arr, target):
	def Helper(arr, l, h):
		if h < l : return -1
		while h >= l:
			mid = l + (h - l)//2
			if arr[mid] == target:
				return mid 
			elif arr[mid]  <target:
				l = mid + 1
			else:
				h = mid - 1
		return - 1

	if not arr : raise ValueError 
	idx = Minimum(arr)
	left = Helper(arr, 0, idx - 1)
	right = Helper(arr, idx, len(arr) - 1)
	return left if left != -1 else right

def Split(arr, maxOps):
	if not arr : raise ValueError 
	l, h = 0, max(arr)
	while h >= l :
		mid = l + (h - l)//2
		if sum([(val - 1)//mid for val in arr]) <= maxOps:
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def Sqrt(x):
	if not x : raise ValueError
	l, h = 0, x + 1
	while h >= l:
		mid = l + (h - l)//2
		if mid * mid > x:
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return (res - 1)**2

import heapq
def ConnectRopes(arr):
	if not arr : raise ValueError
	pq = arr 
	res = 0 
	heapq.heapify(pq)
	while len(pq) > 1:
		tmp = heapq.heappop(pq) + heapq.heappop(pq)
		res += tmp
		heapq.heappush(pq, tmp)
	return res 

def SecondLargest(arr):
	large = arr[0]
	large1 = 0 
	if len(arr) < 2 : raise ValueError
	for num in arr[1:]:
		if num > large:
			large1 = large 
			large = num 
	return large1

def CircularProblem(num):
	if not num : raise ValueError

	# 1. Find the largest power to the given num -> largest_pow => Helper()
	# 2. num = largest_pow + y where y = num - laregst_pow => Solver()
	# 3. result = 2 * y + 1 => main function call 

	def Helper(num):
		if not num : return 0 
		res = 0 
		for i in range(int(num**0.5)):
			tmp = 1<<i 
			if tmp > num:
				break 
			res = tmp
		return res 

	def Solver(num, _pow):
		return num - _pow 

	largest_pow = Helper(num)
	y = Solver(num, largest_pow)
	return 2 * y + 1


print(CircularProblem(41))






