def Boats(arr, day):
	if not arr : return 
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if IsValid(arr, day, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def IsValid(arr, day, const):
	max_wt, days = 0, 1 
	for i in range(len(arr)):
		max_wt += arr[i]
		if max_wt > const:
			max_wt = arr[i]
			days += 1 
		if days > day : return False 
	return True 

arr = [1,2,3,4,5,6,7,8,9,10]
arr2 = [1,2,3,1,1]
D = 5
D2 = 4
print(Boats(arr, D))
print(Boats(arr2, D2))