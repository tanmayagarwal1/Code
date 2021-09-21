def BinarySearch(arr, k):
	if not arr : raise ValueError 
	l, h = 0, len(arr) - 1 
	while h >= l :
		mid = l + (h - l)//2
		if arr[mid] == k : return True 
		if arr[mid] < k : l = mid + 1 
		else : h = mid -1  
	return -1 

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
	l = max(arr)
	h = sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if Helper(arr, mid, days):
			res = mid 
			h = mid - 1 
		else:
			l = mid +1 
	return res 

class MedianInStream:
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

	def median(self):
		if len(self.small) == len(self.large):
			return (-self.small[0] + self.large[0])//2
		else:
			return self.large[0]

class KthLargestInStream:
	def __init__(self, arr):
		if not arr : raise ValueError
		pq = []
		for num in arr : heapq.heappush(pq, -num)
		while len(pq) > k : 
			heapq.heappop(pq)

	def addandExtract(self, num):
		if len(pq) < k : heapq.heappush(pq, -num)
		elif num > pq[0] : heapq.heapreplace(pq, -num)
		return heapq.heappop(pq)

def diamonds(arr, k):
	if not arr : raise ValueError 
	count = 0 
	pq = []
	for num in arr : heapq.heappush(pq, -num)
	res = 0 
	while count < k : 
		count += 1 
		x = heapq.heappop(pq)
		res += (-x)
		heapq.heappush(pq, -(-x/2))
	return res 

def JoinRopes(arr):
	if not arr : raise ValueError 
	pq = []
	for num in arr : heapq.heappush(pq, num)
	res = 0 
	while len(pq) > 1 : 
		tmp = heapq.heappop(pq) + heapq.heappop(pq)
		res += tmp 
		heapq.heappush(pq, tmp)
	return res 

def ReverseInPLace(arr):
	def Helper(arr, ele):
		if not arr:
			arr.append(ele)
			return 
		curr = arr.pop()
		Helper(arr, ele)
		arr.append(curr)
		return 

	if not arr : return 
	ele = arr.pop()
	ReverseInPLace(arr)
	Helper(arr, ele)
	return arr


arr = [1, 2, 3, 4, 5]
print(ReverseInPLace(arr))


