def Boats(arr, days):
	if not arr : return -1 
	l, h = max(arr), sum(arr)
	while h >= l:
		mid = l + (h - l)//2
		if IsValid(arr, days, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def IsValid(arr, days, cont):
	day, wt = 1, 0 
	for i in range(len(arr)):
		wt += arr[i]
		if wt > cont:
			wt = arr[i]
			day += 1
		if day > days : return False 
	return True 


arr = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(Boats(arr, D))