import heapq
def Destroy(arr):
	arr = [-x for x in arr]
	heapq.heapify(arr)
	while len(arr) > 1 and arr[0] != 0:
		heapq.heappush(arr, heapq.heappop(arr) - heapq.heappop(arr))
	return -arr[0]

arr = [2,7,4,1,8,1]
print(Destroy(arr))
