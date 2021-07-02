import heapq
def KClosestToOrigin(points, k):
	if not points : raise ValueError 
	pq = []
	for x, y in points : 
		dist = (x * x) + (y * y)
		heapq.heappush(pq, (-dist, (x, y)))
		if len(pq) > k:
			heapq.heappop(pq)
	return [point[1] for point in pq]

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(KClosestToOrigin(points, k))