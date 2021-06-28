def NiceSubarrays(arr, k):
	if len(arr) == 0 : raise ValueError 
	def Helper(arr, k):
		count = 0
		l, r = 0, 0 
		res = 0
		while r < len(arr):
			if arr[r] % 2 == 1: 
				count += 1 
			r += 1
			while l < r and  count > k:
				if arr[l] % 2 == 1 : count -= 1
				l += 1
			res += r - l 
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

arr = [2, 4, 6]
k = 1 
print(NiceSubarrays(arr, k))