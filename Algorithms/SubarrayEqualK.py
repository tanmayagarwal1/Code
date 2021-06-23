def SubarrayEqualK(arr, k):
	if not arr : return -1 
	d = {0 : 1}
	ans, prefix= 0, 0 
	for num in arr:
		prefix += num 
		if prefix - k in d:
			ans += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1
	return ans 

arr = [1, 2, 3]
k = 3
print(SubarrayEqualK(arr, k))
