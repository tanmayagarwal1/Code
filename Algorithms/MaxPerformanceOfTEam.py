import heapq
def MaxPerformance(n, k, speed, efficiency):
	if not speed or not efficiency : raise ValueError 
	pq = []
	Speed_sum = 0 
	res = 0 
	for e, s in sorted(zip(efficiency, speed), reverse = 1):
		pq.append((e, s))
	return pq


n = 6 
k = 3 
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
print(MaxPerformance(n, k, speed, efficiency))
