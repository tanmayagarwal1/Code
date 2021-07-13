class MedianInStream:
	def __init__(self):
		self.small_heap = [] # This will be a max heap 
		self.large_heap = [] # This will be a min heap 

	def add(self, x):
		def Helper(small_heap, large_heap):
			if len(small_heap) == len(large_heap):
				heapq.heappush(small_heap, -x)
				tmp = heapq.heappop(small_heap)
				heapq.heappush(large_heap, -(tmp))
			else:
				heapq.heappush(large_heap, x)
				tmp = -heapq.heappop(large_heap)
				heapq.heappush(small_heap, tmp)

		Helper(self.small_heap, self.large_heap)

	def Median(self):
		def Helper(small_heap, large_heap):
			if len(small_heap) == len(large_heap):
				return (large_heap[0] - small_heap[0]) / 2
			else:
				return large_heap[0]

# We maintain two heaps to store two halfs of thr\e stream. The small_heap will store the first half of the stream and the large will store the next half of the stream 
# The biggest from small heap and smallest from large heap form the middle element(s)
# When we see that both the lengths are equal ( That means that the stream has even numbers ), and we need to add to the stream, We first add the element to the small heap
# - then pick the maximum element from the small heap and add that to the max heap. This will maintain consistency ( Consistency in the sense that all the elements in small 
# - heap will be less than those of the large_heap)
# Now if they are not of equal lengths, first add the elemetn to the large heap, pick out the minimum element from the large and put it in small for consistency 

# Now to find the median, if lenghts are equal means there are even digits and hence pick one from both ( The smallest from large_heap and biggest from small_heap ) 
# - and divide by 2 
# If they are uneuqal just return the one from the big 
