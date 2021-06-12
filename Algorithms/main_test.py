def ChefCook(arr, p):
	if not arr or not p : return 
	l, h = 0 , 1e8 
	while h >= l :
		mid = l + (h - l)//2
		if IsValid(arr, p, mid):
			res = mid
			h = mid - 1
		else:
			l = mid + 1
	return int(res)

def IsValid(arr, p, time):
	curr_p = 0 
	for i in range(len(arr)):
		loc_time = arr[i]
		j = 2
		while loc_time <= time:
			loc_time += arr[i]*j 
			j += 1
			curr_p += 1
		if curr_p >= p : return True 
	return False 

def Boats(arr, day):
	if not arr or not day : return 
	l, h = max(arr), sum(arr)
	while h >= l :
		mid = l + (h - l)//2
		if IsValidWeight(arr, day, mid):
			res = mid
			h = mid - 1
		else:
			l = mid + 1
	return int(res)

def IsValidWeight(arr, day, mxWeight):
	curr_day, curr_wt = 1, 0 
	for i in range(len(arr)):
		curr_wt += arr[i]
		if curr_wt >= mxWeight:
			curr_day += 1
			curr_wt = arr[i]
		if curr_day > day : return False 
	return True 

def BookDistribution(arr, students):
	if not arr or not students : return - 1
	l, h = max(arr), sum(arr)
	while h >= l : 
		mid = l + (h - l)//2
		if IsValidDist(arr, students, mid):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def IsValidDist(arr, students, mid):
	curr_s, curr_p = 1, 0
	for i in range(len(arr)):
		curr_p += arr[i]
		if curr_p > mid:
			curr_s += 1
			curr_p = arr[i]
		if curr_s > students : return False 
	return True 

''' OBSERVATION BASED ON ABOVE BINARY SEARCH PROBELMS : If we take the example of boats : If have two constraints to out IsValid 
	func : problem given = days and user given = max_wt. Now in the IsValid func we decalre to variable : curr_day = 1 (problem
	based) and curr_wt (user based). While looping we increment the user based var and check if it breaks the user constraint.
	If it does, the user based var is given a reset and the problem based constraint var is incremented. after the loop temrin-
	ation, we check the problem constarint values to return our answer.
	This is the trend for such problems ''' 

arr = [15, 17, 20]
k = 2 
print(BookDistribution(arr, k))


