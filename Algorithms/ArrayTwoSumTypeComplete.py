def phoneCombinations(digits):
	def Helper(arr, d, path, res):
		if not arr:
			res.append(path)
			return 
		for char in d[arr[0]]:
			Helper(arr[1:], d, path + char, res)
	if not digits : raise ValueError 
	d = {"2" : "abc", "3" : "def"}
	res = []
	Helper(digits, d, "", res)
	return res 

def BeauifulArrangements2(n, k):
	if not n : raise ValueError 
	arr = list(range(1, n + 1))
	for i in range(1, k):
		arr[i : ] = arr[:i - 1:-1]
	return arr 

def TwoSum(arr, k):
	if not arr : raise ValueError 
	d = {}
	for i in range(len(arr)):
		if k - arr[i] in d : 
			return d[k - arr[i]], i 
		d[arr[i]] = i 
	return -1  

def TwoProduct(arr, k):
	if not arr : raise ValueError 
	d = {}
	for i in range(len(arr)):
		if k // arr[i] in d  and k % arr[i] == 0 : 
			return d[k//arr[i]], i 
		d[arr[i]] = i 
	return -1 

def MinimumLengthSubarrayEqualToTarget(arr, k):
	if not arr : raise ValueError 
	l, r, prefix = 0, 0, 0 
	while r < len(arr):
		prefix += arr[r]
		while l < r and prefix >= k : 
			res = min(res, r - l + 1)
			prefix -= arr[l]
			l += 1 
		r += 1 
	return res if res < len(arr) + 1 else -1 

def MaximumLengthSubarray(arr, k):
	if not arr : raise ValueError 
	l, r, prefix, res = 0, 0, 0, 0 
	while r < len(arr):
		prefix += arr[r]
		while l < r and prefix >= k:
			res = max(res, r - l + 1)
			prefix -= arr[l]
			l += 1 
		r += 1 
	return res 

def MinimumOpsToMakeArrayIncreasing(arr):
	if not arr : raise ValueError 
	ops = 0 
	for i in range(1, len(arr)):
		if arr[i] <= arr[i - 1]:
			diff = arr[i - 1] - arr[i] + 1 
			ops += diff 
			arr[i] = arr[i - 1] + 1 
	return ops 

def countSubsetsEqualK(arr, k):
	if not arr : raise ValueError 
	d = { 0 : 1 }
	prefix = 0 
	count = 0 
	for i in range(len(arr)):
		prefix += arr[i]
		if prefix - k in d :
			count += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1 
	return count 

def CountSubsetsDivisibleByK(arr, k):
	if not arr : raise ValueError 
	d = { 0 : 1 }
	prefix, count = 0, 0 
	for i in range(len(arr)):
		prefix += arr[i]
		key = prefix % k 
		if key in d :
			count += d[key]
		d[key] = d.get(key, 0) + 1 
	return count 

def SubarrayCountWithKDistinctElements(arr, k):
	if not arr : raise ValueError 
	def Helper(arr, k):
		l, r, res, count = 0, 0, 0, 0 
		d = { }
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1 
			if d[arr[r]] == 1 : count += 1 
			while l < r and count > k : 
				d[arr[l]] -= 1 
				if d[arr[l]] == 0 : count -=1 
				l += 1 
			res += r - l + 1 
			r += 1 
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def Nicesubarrays(arr, k):
	if not arr : raise ValueError 
	def Helper(arr, k):
		l, r, res, count = 0, 0, 0, 0 
		while r < len(arr):
			if arr[r] % 2 != 0 : count += 1 
			while l < r and count > k :
				if arr[l] % 2 != 0 : count -= 1 
				l += 1 
			res += r - l + 1 
			r += 1 
		return res 

	return Helper(arr, k) - Helper(arr, k - 1)

def ContiguousArray(arr):
	if not arr : raise ValueError 
	Sum = 0 
	res = 0 
	d = { 0 : - 1 }
	for i in range(len(arr)):
		if arr[i] == 0 : Sum -= 1 
		else : Sum += 1
		if Sum in d : res = max(res, i - d[Sum])
		else : d[Sum] = i 
	return res 

def MaximumLengthSubstringWithKDistinctElements(sti, k):
	def Helper(arr, k):
		l, r, count, res = 0, 0, 0, 0 
		d = { }
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1 
			if d[arr[r]] == 1 : count += 1 
			while l < r and count > k : 
				d[arr[l]] -= 1 
				if d[arr[l]] == 0 : count -= 1
				l += 1 
			res = max(res, r - l + 1)
			r += 1 
		return res 
	if not sti : raise ValueError 
	return Helper(sti, k)



