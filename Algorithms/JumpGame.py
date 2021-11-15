def JumpGame(arr):
	if not arr : raise ValueError 
	max_dist = 0 
	for idx, dist in enumerate(arr):
		if idx > max_dist : return False 
		max_dist = max(max_dist, idx + dist)
	return True 

arr = [2,3,1,1,4]
print(JumpGame(arr))