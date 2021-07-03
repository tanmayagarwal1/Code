import heapq
def StoneWeights(arr):
	if not arr : raise ValueError 
	# In this problem every next time a stone is destroyed which is of min weights 
	# Maintain a min heap 
	heapq.heapify(arr)
	while len(arr) > 1 and arr[0] != 0:
		heapq.heappush(arr, heapq.heappop(arr) - heapq.heappop(arr))
	return arr[0]

def MinWorkers(wages, quality, k):
	if not quality : raise ValueError 
	expected = sorted([float(w/q), q] for w, q in zip(wages, quality))
	pq, QSum = [], 0
	res = float('inf')
	for e, q in expected:
		heapq.heappush(pq, -q) # We need to minimise quality hence maintain max heap by using neagtive elements 
		QSum += q 
		if len(pq) > k : QSum += heapq.heappop(pq)
		if len(pq) == k : res = min(res, QSum * e)
	return res 

def MaxEfficiency(speed, efficiency, n, k):
	# Here we need to remove lower speeds and start from higher efficiencies. Hence maintain min heap for speed and sort based on efficiency first 
	if not speed or not efficiency : raise ValueError 
	iterator = sorted(([e, s] for e, s in zip(efficiency, speed)), reverse = True)
	pq = []
	Ssum = 0
	res = 0 
	for e, s in iterator:
		heapq.heappush(pq, s)
		Ssum += s 
		if len(pq) > k : Ssum -= heapq.heappop(pq)
		res = max(res, Ssum * e)
	return res 

def StockPrice(prices):
	if not prices : raise ValueError 
	min_price = float('inf')
	max_profit = 0 
	for price in prices:
		min_price = min(min_price, price)
		profit = price - min_price 
		max_profit = max(profit, max_profit)
	return max_profit 

def StockPriceNtransactions(prices):
	return sum([tomorrow - today for today, tomorrow in zip(prices, prices[1:]) if tomorrow - today > 0])

def Mountain(arr):
	if not arr : raise ValueError 
	i = 1 
	j = len(arr) - 1
	while i < len(arr) and arr[i] > arr[i - 1]:
		i += 1
	while j > 0 and arr[j - 1] > arr[j]:
		j -= 1
	if i == j and i != 0 and i != len(arr) - 1 : return True 
	return False 

def longestMountain(arr):
	if not arr : raise ValueError 
	res = 0 
	for i in range(1, len(arr) - 1):
		if arr[i - 1] < arr[i] > arr[i + 1]:
			l = r = i 
			while l > 0 and arr[l - 1] < arr[l]:
				l -= 1
			while r  < len(arr) - 1 and  arr[r + 1] < arr[r] :
				r += 1
			res = max(res, r - l + 1)
	return res 

def KClosestPoints(arr, k, x):
	if not arr : raise ValueError 
	# Here i will do this using heap 
	# Specifically, as we want higher distance points to be removes, we will be opting for max heap by using -ve distances 
	pq = []
	for num in arr:
		heapq.heappush(pq, (-abs(num - x), -num))
		if len(pq) > k : heapq.heappop(pq)
	return sorted([-i[1] for i in pq])

def KclosestPoints2(arr, k, x):
	if not arr : raise ValueError
	# Here we will be using the binary search approach O( logN )
	l = 0 
	h = len(arr) - k 
	while h > l:
		mid = l + (h - l)//2
		if abs(arr[mid + k] - x) < abs(arr[mid] - x): # Which means that the distance of the point mid + k from x is less than distance from mid to x 
			l = mid + 1
		else:
			h = mid
	return arr[l : l + k]

def KclosestPointsToOrigin(arr, k):
	if not arr : raise ValueError 
	pq = []
	# Here we will use a max heap beacuse we want to eliminate higher distances 
	for x, y in arr:
		dist = (x * x) + (y * y)
		heapq.heappush(pq, (-dist, (x, y))) # The points need not be in sorted order or anything so it does not matter how they appear in output
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

def MonotonicArray(x):
	# Given interger return highest increasing int 
	# Find the index from which the anomoaly(descresing) occured 
	# If Dups, find the first occurance 
	# Truncate the entire number after the idx to 9 
	# decrement the anomaly idx by 1 
	# To make our lives easier we search from start instead of searching from the end by reversing the number 
	if not x : raise ValueError 
	n = x 
	idx = -1 
	arr = [int(i) for i in str(n)[::-1]]
	for i in range(1, len(arr)):
		if arr[i] > arr[i - 1] or (idx != -1 and arr[idx] == arr[i]):
			idx = i 
	if idx == - 1: return n 
	for j in range(idx):
		arr[j] = 9 
	arr[idx] -= 1
	return int(''.join([str(i) for i in arr[::-1]]))

def greycode(n):
	if not n : raise ValueError 
	res = [0]
	for i in range(1, 2**n):
		res.append(res[-1] ^ (i & ~i + 1))
	return res 

def KfrequentElementsHeap(arr, k):
	if not arr : raise ValueError 
	pq = []
	d = {}
	for num in arr:
		d[num] = d.get(num, 0) + 1
	for num, freq in d.items():
		heapq.heappush(pq, (freq, num))
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

def KFrequentElementsBuckets(arr, k):
	if not arr : raise ValueError
	buckets = [[] for _ in range(len(arr))]
	d = {}
	for num in arr:
		d[num] = d.get(num, 0) + 1
	for num, freq in d.items() : buckets[freq].append(num)
	res = []
	for i in range(len(buckets) - 1, -1, -1):
		bucket = buckets[i]
		if bucket:
			for num in bucket:
				res.append(num)
	return res[:k]

def KthLargest(arr, k):
	if not arr : raise ValueError
	pq = []
	for num in arr:
		heapq.heappush(pq, num)
		if len(pq) > k : heapq.heappop(pq)
	return heapq.heappop(pq)

def KthLargestQuckSelect(arr, k):
	def partition(arr, l, h):
		i = l - 1
		pivot = arr[h]
		for j in range(l, h):
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i + 1], arr[h] = arr[h], arr[i + 1]
		return i + 1

	def Helper(arr, k):
		if arr:
			mid = partition(arr, 0, len(arr) - 1)
			if k > mid + 1:
				return Helper(arr[mid + 1 :], k - mid - 1)
			elif k < mid + 1:
				return Helper(arr[:mid], k)
			else:
				return arr[mid]
	if not arr : raise ValueError
	return Helper(arr, len(arr) - k + 1)


# Stone Weight
arr = [2,7,4,1,8,1]
print(StoneWeights(arr)) # 1 

# Min Wokrkers 
wage = [70,50,30]
quality = [10,20,5]
k = 2
print(MinWorkers(wage, quality, k)) # 105

# Max Efficiency 
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
n = 6 
k = 3 
print(MaxEfficiency(speed, efficiency, n, k)) # 68

# Stocsk1
arr = [7,1,5,3,6,4]
print(StockPrice(arr)) # 5

# Stocks2
arr = [7,1,5,3,6,4]
print(StockPriceNtransactions(arr)) # 7 

# Monotonic Array 
print(MonotonicArray(332)) # 299

# Mountain 
arr = [9,8,7,6,5,4,3,2,1,0]
print(Mountain(arr)) # False 

# Longest Mountain 
arr = [2,1,4,7,3,2,5]
print(longestMountain(arr)) # 5 

# K Closest Points 
arr = [1,2,3,4,4,4,4,5,5]
k = 3
x = 3
print(KClosestPoints(arr, k, x)) # [2, 3, 4]

# K Closest Points 2
arr = [1,2,3,4,4,4,4,5,5]
k = 3
x = 3
print(KclosestPoints2(arr, k, x)) # [2, 3, 4]

# Kclosest Points to origin 
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(KclosestPointsToOrigin(points, k)) # [(-2, 4), (3, 3)]

# Grey Code 
n = 3
print(greycode(n)) # [0, 1, 3, 2, 6, 7, 5, 4]

# K frequent elements Heap 
arr = [1,1,1,2,2,3]
k = 2
print(KfrequentElementsHeap(arr, k)) # [2, 1]

# K frequent elements buckets 
arr = [1,1,1,2,2,3]
k = 2
print(KFrequentElementsBuckets(arr, k)) # [1, 2]

# Kth Largest Heap 
arr = [3,2,3,1,2,4,5,5,6]
k = 4
print(KthLargest(arr, k)) # 4 

# Kth Largest QucikSelect 
arr = [3,2,3,1,2,4,5,5,6]
k = 4
print(KthLargestQuckSelect(arr, k)) # 4 


				
