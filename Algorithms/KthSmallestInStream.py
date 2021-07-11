class KthSmallestInStream:
	def __init__(self, arr, k):
		self.arr = arr
		self.k = k 
		self.arr = [-i for i in self.arr]
		heapq.heapify(self.arr)
		while len(self.arr) > k:
			heapq.heappop(self.arr)

	def Add_and_fetch(self, num):
		if len(self.arr) < k:
			heapq.heappush(self.arr, -num)
		elif num < self.arr[0]:
			heapq.heapreplace(self.arr, -num)
		return self.arr[0]

# Reverse implmentation of kth - largest in stream. Check docs 