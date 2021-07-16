def SubarraySumExists(arr, target):
	if not arr : raise ValueError 
	d = {}
	prefix = 0 
	for i in range(len(arr)):
		prefix += arr[i]
		if target:
			prefix = prefix % target
		if prefix in d :
			if abs(d[prefix] - i) > 1 :
				return True
		d[prefix] = i
	return False 

arr = [23,2,4,6,7]
target =  6
print(SubarraySumExists(arr, target))