def Cook(arr, p):
	if len(arr) == 0:
		return -1 
	l, h = 0, 1e8
	while h >= l :
		mid = (l + h)//2
		if CheckCook(arr, p, mid):
			ans = mid 
			h = mid - 1 
		else:
			l = mid + 1
	return int(ans)

def CheckCook(arr, p, global_time):
	curr_p = 0 
	for i in range(len(arr)):
		local_time = arr[i]
		j = 2
		while local_time <= global_time:
			local_time += arr[i]*j 
			curr_p += 1
			j += 1
		if curr_p >= p : return True 
	return False 

arr = [1, 2, 3, 4]
p = 10
print(Cook(arr, p))

