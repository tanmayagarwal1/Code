def KadensCircular(arr):
	if not arr : raise ValueError 
	global_max = arr[0]
	local_max = 0 
	global_min = arr[0]
	local_min = 0 
	for num in arr:
		local_max += num 
		local_min += num 
		if global_max < local_max:
			global_max = local_max 
		if global_min > local_min:
			global_min = local_min
		if local_min > 0 : local_min = 0 
		if local_max < 0 : local_max = 0
	return max(global_max, sum(arr) - global_min)  if global_max > 0 else max(arr)

arr = [5,-3,5]
print(KadensCircular(arr))