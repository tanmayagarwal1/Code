import heapq
def Supplier(arr, k):
	if not arr : raise ValueError 
	pq = []
	for num in arr:
		heapq.heappush(pq, -num)
	Profit, count = 0, 0 
	while count < k :
		x = heapq.heappop(pq)
		heapq.heappush(pq, x + 1)
		Profit += -(x)
		count += 1
	return Profit 

arr = [1, 2, 3]
k = 2
print(Supplier(arr, k))

