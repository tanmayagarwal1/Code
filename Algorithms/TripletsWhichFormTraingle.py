def TripletsWhichFormATraingle(arr):
	# Condition for triangle : sum of any two side > third side ( (a + b > c) or (a + c > b) or (c + b > a) )
	
	if not arr : raise ValueError 
	arr.sort()
	count = 0 
	l, r = 0, 0 
	for i in range(2, len(arr)):
		l, r = 0, i - 1
		target = arr[i]
		while l < r :
			if arr[l] + arr[r] > target:
				count += (r - l)
				r -= 1
			else:
				l += 1
	return count 

arr = [4,2,3,4]
arr2 = [0, 1, 0]
print(TripletsWhichFormATraingle(arr))