import heapq
def MaxPerformance(n, k, speed, efficiency):
	if not speed or not efficiency : raise ValueError 
	pq = []
	Speed_sum = 0 
	res = 0 
	for e, s in sorted(zip(efficiency, speed), reverse = 1):
		heapq.heappush(pq, s)
		Speed_sum += s 
		if len(pq) > k : Speed_sum -= heapq.heappop(pq)
		res = max(res, Speed_sum * e)
	return res 


n = 6 
k = 3 
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
print(MaxPerformance(n, k, speed, efficiency))
