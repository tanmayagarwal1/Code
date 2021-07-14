class MedianInStream:
	def __init__(self):
		self.small = []
		self.large = []

	def add(self, data):
		def Helper(small, large):
			if len(small) == len(large):
				heapq.heappush(small, -data)
				tmp = heapq.heappop(small)
				heapq.heappush(large, -tmp)
			else:
				heapq.heappush(large, data)
				tmp = heapq.heappop(large)
				heapq.heappush(small, -tmp)

		Helper(self.small, self.large)

	def Median(self):
		if len(self.large) == len(self.small):
			return (self.large[0] - self.small[0])//2 
		else:
			return self.large[0]

class KthLargestInStream(self):
	def __init__(self, arr, k):
		self.k = k 
		self.arr = arr 
		heapq.heapify(self.arr)
		while len(self.arr) > k:
			heapq.heappop(self.arr)

	def add_and_fetch(self, data):
		if len(self.arr) < self.k:
			heapq.heappush(self.arr, data)
		elif data > self.arr[0]:
			heapq.heapreplace(self.arr, data)
		return heaqp.heappop(self.arr)

def Diamonds(arr, k):
	if not arr : raise ValueError 
	arr = [-val for val in arr]
	heapq.heapify(arr)
	count = 0 
	res = 0 
	while count < k:
		count += 1
		tmp = -(heapq.heappop(arr))
		res += tmp 
		heapq.heappush(arr, -(tmp//2))
	return res 

def JoinRopes(arr):
	if not arr : raise ValueError 
	heapq.heapify(arr)
	while len(arr) > 1 :
		tmp = heapq.heappop(arr) + heapq.heappop(arr)
		res += tmp 
		heapq.heappush(arr, tmp)
	return res 

def Stones(arr):
	if not arr : raise ValueError 
	heapq.heapify(arr)
	while len(arr) > 1 and arr[0] != 0:
		heaqp.heappush(arr, heapq.heappop(arr) - heapq.heappop(arr))
	return heapq.heappop(arr)

def MinimumWorkers(wage, qual, k):
	if not wage or not qual : raise ValueError
	expected = sorted([(float(w/q), q) for w, q in zip(wage, qual)])
	Qsum = 0 
	pq = []
	res = float('inf')
	for r, q in expected:
		heapq.heappush(pq, -q)
		Qsum += q 
		if len(pq) > k : Qsum -= heapq.heappop(pq)
		if len(pq) == k : res = min(res, Qsum * r)
	return res 

def MaximumEfficiency(eff, speed, k):
	if not eff or not speed : raise ValueError
	expected = sorted([(e, s) for e, s in zip(eff, speed)])
	Ssum = 0 
	res = float('-inf')
	pq = []
	for e, s in expected[::-1]:
		heapq.heappush(pq, s)
		Ssum += s 
		if len(pq) > k : Ssum -= heapq.heappop(pq)
		res = max(res, Ssum * e)
	return res 

def KClosestPointsToOrigin(arr, k):
	if not arr : raise ValueError 
	pq = []
	for i, j in arr:
		dist = i * i + j * j 
		heapq.heappush(pq, (-dist, (i, j)))
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

def SortKsortedarray(arr, k):
	if not arr : raise ValueError 
	pq = arr[:k + 1]
	heapq.heapify(pq)
	idx = 0 
	for i in range(k + 1, len(arr)):
		arr[idx] = heapq.heappop(pq)
		heapq.heappush(pq, arr[i])
		idx += 1
	while pq:
		arr[idx] = heapq.heappop(pq)
		idx += 1
	return arr 




