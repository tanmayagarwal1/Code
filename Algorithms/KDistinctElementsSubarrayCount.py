def SubarrayWithKDistinctelements(arr, k):
	if len(arr) == 0: raise ValueError 
	def Helper(arr, k):
		d = {}
		l, r, count, res = 0, 0, 0, 0 
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1
			if d[arr[r]] == 1 : count +=  1 # ! distinct element 
			r += 1
			while l < r and count > k:
				d[arr[l]] -= 1
				if d[arr[l]] == 0 : count -= 1 
				l += 1
			res += r - l 
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

arr = [1, 2, 1, 2, 3]
k = 2
print(SubarrayWithKDistinctelements(arr, k))