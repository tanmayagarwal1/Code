import heapq
def SellBalls(arr, orders):
	mod = (10**9) + 7 
	if sum(arr) < orders : return - 1
	if not arr : raise ValueError 
	pq = []
	for num in arr : heapq.heappush(pq, -(num % mod))
	count = 0 
	res = 0 
	while count < (orders % mod):
		count += 1
		tmp = heapq.heappop(pq)
		res += (-tmp)
		heapq.heappush(pq, tmp + 1)
	return res 

arr = [2,8,4,10,6]
orders = 20
print(SellBalls(arr, orders))

