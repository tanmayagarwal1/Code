from collections import defaultdict
import heapq

def Flights(flights, src, dst, stops):
	graph, q= defaultdict(list), []
	for s, d, w in flights : graph[s].append((w, d))
	heapq.heappush(q, (0, stops + 1, src))
	while q:
		price, stop, city = heapq.heappop(q)
		if city is dst : return price 
		if stop > 0 :
			for next_price, next_city in graph[city]:
				heapq.heappush(q, (next_price + price, stop - 1, next_city))
	return -1 

flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2 
k   = 0

print(Flights(flights, src, dst, k))