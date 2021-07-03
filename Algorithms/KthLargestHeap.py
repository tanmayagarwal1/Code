import heapq
def KthLargestElement(arr, k):
	if not arr : raise ValueError 
	pq = []
	for num in arr:
		heapq.heappush(pq, num)
		if len(pq) > k : heapq.heappop(pq)
	return heapq.heappop(pq)

arr = [3,2,3,1,2,4,5,5,6]
k = 4
print(KthLargestElement(arr, k))