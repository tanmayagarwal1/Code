import heapq
def minCost(wage, quality, k):
	if not wage : raise ValueError
	expected = sorted([float(w/q), q] for w, q in zip(wage, quality))
	heap = []
	qsum = 0 
	res = float('inf')
	for e, q in expected:
		heapq.heappush(heap, -q)
		qsum += q 
		if len(heap) > k : qsum += heapq.heappop(heap)
		if len(heap) == k : res = min(res, qsum * e)
	return res 


wage = [70,50,30]
quality = [10,20,5]
k = 2
print(minCost(wage, quality, k))


