def MinimumSubarray(arr, target):
	if not target or not arr : return - 1
	l, r = 0, 0 
	res, s = len(arr) + 1, 0 
	for i in range(len(arr)):
		s += arr[i]
		while s >= target:
			res = min(res, i - l + 1)
			s -= arr[l]
			l += 1
		r += 1
	return res if res < len(arr) + 1 else 0 

arr = [2,3,1,2,4,3]
target = 7 
print(Minimum(arr, target)) # 2 
