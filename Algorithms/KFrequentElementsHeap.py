import heapq
def KfrequentElements(arr, k):
	if not arr : raise ValueError 
	d = {}
	for num in arr:
		d[num] = d.get(num, 0) + 1
	pq = []
	for num, freq in d.items():
		heapq.heappush(pq, (freq, num))
		if len(pq) > k : heapq.heappop(pq)
	return [i[1] for i in pq]

arr = [1,1,1,2,2,3]
k = 2
print(KfrequentElements(arr, k))
