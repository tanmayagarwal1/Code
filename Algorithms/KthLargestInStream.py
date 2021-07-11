class KthLargestInAStream:
	def __init__(self, arr, k):
		self.arr = arr 
		self.k =  k 
		heapq.heapify(self.arr)
		while len(self.arr) > k:
			heapq.heappop(self.arr)

	def add_and_fetch(self, num):
		if len(self.arr) < k :
			heapq.heapush(self.arr, num)
		elif num > self.arr[0]:
			heapq.heapreplace(self.arr, num)
		return self.arr[0]

# So here the initialisation is trivial 
# But what we are doing in the add and fetch is that : At any given time the heap will contain k large elemetns. As it is the min heap : The kth largest will be the smallest
# - element in the heap which is at heap[0]
# So first we check if the length of the heap is less than k or not. If yes, just add the num 
# If it is not and the new number is greater than the kth largest, it means kth largest is not the kth largest anymore. So we need to put this in the heap
# To put the new element in the heap we just do heap replace, as we do not wanna pop out anything 

# If the number is less than kth largest, then it is does not belong to the heap anyway hence discard it. And just return the first element of the heap in any case
# again first element will be the kth largest 