def SubarrayLArgest(arr, k):
	if not arr : raise ValueError 
	l, r = 0, 0 
	prefix = 0 
	res = 0 
	while r < len(arr):
		prefix += arr[r]
		while l < r and prefix >= k:
			res = max(res, r - l + 1)
			prefix -= arr[l]
			l += 1
		r += 1
	return res 

def KDistinctElements(arr, k):
	if not arr : raise ValueError
	def Helper(arr, k):
		l, r, res, count = 0, 0, 0, 0 
		d = {}
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1
			if d[arr[r]] == 1 : count += 1
			while l < r and count > k:
				d[arr[l]] -= 1
				if d[arr[l]] == 0 : count -= 1
				l += 1
			res += r - l + 1
			r += 1
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def NumberOfSubarraysToK(arr, k):
	if not arr : raise ValueError
	count = 0 
	prefix = 0 
	d = {0 : 1}
	for num in arr:
		prefix += num 
		if prefix - k in d :
			count += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1
	return count 

def ContinguousSubarray(arr):
	if not arr : raise ValueError
	Sum, res= 0, 0
	d = {0 : -1}
	for i in range(len(arr)):
		if arr[i] == 0 : Sum -= 1
		else : Sum += 1
		if Sum in d:
			res = max(res, i - d[Sum])
		else:
			d[Sum] = i 
	return res 

def NumOfSplits(arr, maxOps):
	if not arr : raise ValueError
	l, h = 1, maz(arr)
	while h >= l :
		mid = l + (h - l)//2
		if sum([n - 1//mid for n un arr]) <= maxOps:
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def Boats(arr, days):
	def Helper(arr, mid, days):
		curr_day = 1
		curr_wt = 0 
		for num in arr:
			curr_wt += num 
			if curr_wt > mid:
				curr_wt = num 
				curr_day += 1
			if curr_day > days : return False 
		return True 

	if not arr : raise ValueError
	l, h = max(arr), sum(arr)
	while h >= l:
		mid = l + (h - l)//2
		if Helper(arr, mid, days):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

def CookChef(arr, p):
	def Helper(arr, mid, p):
		curr_p = 0 
		curr_time = 0 
		for i in range(len(arr)):
			curr_time = arr[i]
			j = 2 
			while curr_time <= mid:
				curr_time += arr[i] * j 
				j += 1
				curr_p += 1
			if curr_p >= p : return True 
		return False 

	if not arr : raise ValueError 
	l, h = 0, 1e8 
	while h >= l:
		mid = l + (h - l)//2
		if Helper(arr, mid, p):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 



