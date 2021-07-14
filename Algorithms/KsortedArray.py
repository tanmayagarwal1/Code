def SortKSortedArray(arr, k):
	if not arr : raise ValueError 
	import heapq 
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

arr = [2, 6, 3, 12, 56, 8]
k = 3
print(SortKSortedArray(arr, k))
