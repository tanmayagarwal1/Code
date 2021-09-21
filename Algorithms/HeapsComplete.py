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

def MinimumWorker(wage, qual, k):
	if not wage or not qual : raise ValueError 
	expected = sorted([(wage/qual, qual) for wage, qual in zip(wage, qual)])
	Qsum = 0 
	res = 0 
	pq = []
	for r, q in expected:
		heapq.heappush(pq, -q)
		Qsum += q 
		if len(pq) > k : Qsum += heapq.heappop(pq)
		if len(pq) == k : res = max(res, Qsum * r)
	return res 

def TeamPerformance(speed, eff, k):
	if not speed or not eff : raise ValueError 
	expected = sorted([(s, e) for s, e in zip(speed, eff)])
	Ssum = 0 
	pq, res = [], 0 
	for s, e in expected:
		heapq.heappush(pq, s)
		Ssum += s 
		if len(pq) > k : Ssum -= heapq.heappop(pq)
		res = max(res, Ssum * e)
	return res 

def KClosestToOrigin(arr, k):
	if not arr : raise ValueError 
	pq=  []
	for i, j in arr:
		dist = i * i + j * j 
		heapq.heappush(pq, (-dist, (i, j)))
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

def KFrequentElements(sti, k):
	if not sti : raise ValueError 
	d = {}
	for char in sti:
		d[char] = d.get(char, 0) + 1 
	pq = []
	for num, freq in d.items():
		heapq.heappush(pq, (freq, num))
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

def SupplierProfit(arr, k):
	if not arr : raise ValueError 
	pq = []
	for num in arr : heapq.heappush(pq, -num)
	count, res = 0, 0 
	while count < k : 
		count +=1 
		tmp = heapq.heappop(pq)
		res += (-tmp)
		heapq.heappush(pq, tmp +1 )
	return res 

def LastStoneWeigth(arr):
	if not arr : raise ValueError 
	pq = []
	for num in arr : heapq.heappush(pq, -num)
	while len(pq) > 1 and pq[0] != 0 : 
		heapq.heappush(pq, heapq.heappop(pq) - heapq.heappop(pq))
	return -heapq.heappop(pq)

def SortKSortedArray(arr, k):
	if not arr : raise ValueError 
	idx = 0 
	pq = arr[:k]
	heapq.heapify(pq)
	for i in range(k, len(arr)):
		arr[idx] = heapq.heappop(pq)
		heapq.heappush(pq, arr[i])
		idx +=  1
	while pq:
		arr[idx] = heaqp.heappop(pq)
		idx += 1 
	return arr 




