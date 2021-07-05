import heapq
def Diamonds(arr, k):
	if not arr : raise ValueError 
	pq = []
	for num in arr: heapq.heappush(pq, -num)
	count = 0
	diamonds = 0 
	while count < k:
		count += 1
		x = heapq.heappop(pq)
		heapq.heappush(pq, -(-x//2))
		diamonds += -(x)
	return diamonds

arr = [2, 1, 7, 4, 2]
k = 3
print(Diamonds(arr, k)) 




