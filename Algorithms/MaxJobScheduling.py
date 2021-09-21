import itertools 
import heapq
def MaxJobScheduling(start, end, profit):
	if not start or not profit or not end : raise ValueError 
	arr = sorted(zip(start, itertools.repeat(1), end, profit))
	res = 0 
	while arr:
		tmp = heapq.heappop(arr)
		if tmp[1]:
			heapq.heappush(arr, (tmp[2], 0, res + tmp[3]))
		else : res = max(res, tmp[2])
	return res 

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(MaxJobScheduling(startTime, endTime, profit))