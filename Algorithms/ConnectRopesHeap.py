import heapq
def ConnectRopes(arr):
	if not arr : raise ValueError
	pq = arr 
	res = 0 
	heapq.heapify(pq)
	while len(pq) > 1:
		tmp = heapq.heappop(pq) + heapq.heappop(pq)
		res += tmp
		heapq.heappush(pq, tmp)
	return res 

arr = [2, 3, 4, 6]
print(ConnectRopes(arr))
