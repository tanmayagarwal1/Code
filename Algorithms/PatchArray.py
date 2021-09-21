def PathArray(arr, n):
	if not arr : raise ValueError 
	res = 0
	covered = 0 
	for num in arr:
		if num > covered + 1 :
			res += 1 
			covered = covered * 2 + 1 
			if covered >= n : return res 
		covered += num 
		if covered >= n : return res 
	while covered < n :
		res += 1 
		covered = covered * 2 + 1 
	return res 

arr = [1,5,10]
n = 20
print(PathArray(arr, n))
