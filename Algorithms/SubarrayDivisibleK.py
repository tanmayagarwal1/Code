def SubarrayDivisibleK(arr, k):
	if not arr : return -1 
	sums = {0 : 1}
	ans, prefix= 0, 0 
	for num in arr:
		prefix += num 
		key = prefix % k 
		if key in sums:
			ans += sums[key]
			sums[key] += 1
			continue 
		sums[key] = 1
	return ans 

arr = [4,5,0,-2,-3,1]
k = 5 
print(SubarrayDivisibleK(arr, k))
