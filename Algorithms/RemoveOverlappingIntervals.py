def RemoveOverlappingIntervals(arr):
	if not arr : raise ValueError 
	arr.sort(key = lambda x : x[1]) 
	prev = float('-inf')
	count = 0 
	for i, j in arr:
		if i >= prev:
			prev = j 
		else:
			count += 1
	return count 


arr = [[1,100],[11,22],[1,11],[2,12]]
print(RemoveOverlappingIntervals(arr))