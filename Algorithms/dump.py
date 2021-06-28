def Permutations(arr):
	def Helper(arr, path, res):
		if not arr : 
			res.append(path)
			return 
		for i in range(len(arr)):
			Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res) 
	if len(arr) == 0 : raise ValueError 
	res = []
	Helper(arr, [], res)
	return res 

def Combine(arr, target):
	def Helper(arr, target, path, res, idx):
		if target < 0 : raise ValueError
		if target == 0 : 
			res.append(path)
			return 
		for i in range(idx, len(arr)):
			Helper(arr, target - arr[i], path + [arr[i]], res, idx)
	res = []
	Helper(arr, target, [], res, 0)
	return res 

def Subsets(arr):
	return [[arr[i] for i in range(len(arr)) if bit & 1 <<i != 0] for bit in range(1<<len(arr))]

def Subsets2(arr):
	if not arr : raise ValueError
	sol = [[]]
	for num in arr:
		sol += [current + [num] for current in sol]
	return sol 

def Partitions(O, P):
	if P == 1 : return 1 
	if P == 0 or O < 0 : return 0 
	return Partitions(O - P, P) + Partitions(O, P - 1)

def Beautifularrangements(n):
	arr = [i for i in range(1, n + 1)]
	res = []
	def Helper(arr, path, res, idx):
		if not arr:
			res.append(path)
			return 
		for i, num in enumerate(arr):
			if num % idx == 0 or idx % num == 0 :
				Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res, idx + 1)
	Helper(arr, [], res, 1)
	return res 

def TwoSum(arr, target):
	if not arr : raise ValueError
	d = dict()
	for i in range(len(arr)):
		if target - arr[i] in d:
			return d[target - arr[i]], i 
		d[arr[i]] = i 
	return -1 

def EqualToK(arr, k):
	if not arr : raise ValueError
	d = {0 : 1}
	count = 0 
	prefix = 0 
	for num in arr:
		prefix += num 
		if prefix - k in d:
			count += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1
	return count 

def DivisibleByK(arr, k):
	if not arr : raise ValueError
	d = {0 : 1}
	count, prefix = 0, 0 
	for num in arr:
		prefix += num 
		key = prefix % k 
		if key in d:
			count += d[key]
		d[key] = d.get(key, 0) + 1
	return count 

def IsMultipleValaible(arr, k):
	if not arr : raise ValueError
	d = dict()
	for i in range(len(arr)):
		if k // num[i] in d and k % num[i] == 0 :
			return d[k // num[i]], i 
		d[num[i]] = i 
	return -1 

def ProductArray(arr):
	if not arr : raise ValueError
	res = [1]*len(arr)
	for i in range(1, len(arr)):
		res[i] = res[i - 1] * arr[i - 1]
	prod = 1
	for i in range(len(arr) - 1, - 1, -1):
		res[i] = res[i] * prod 
		prod = prod * arr[i]
	return res 

def MaximumProductSubarray(arr):
	if not arr : raise ValueError
	arr2 = arr.reverse()
	for i in range(1, len(arr)):
		arr[i] *= arr[i - 1] or 1 
		arr2[i] *= arr2[i - 1] or 1 
	return max(arr + arr2)

def NextPermutations(arr):
	if len(arr) == 0 : raise ValueError
	i, j = len(arr - 1), len(arr) - 1
	while i >=0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i == 0 : 
		arr.reverse()
		return arr 
	k = i - 1
	while arr[j] <= arr[k]:
		j -= 1
	arr[k], arr[j] = arr[j], arr[k]
	l, h = k + 1, len(arr) - 1
	while h > l :
		arr[l], arr[h] = arr[h], arr[l]
		l += 1
		h -= 1
	return arr 

def PeakElement(arr):
	if len(arr) == 0 : raise ValueError
	l, h = 0, len(arr) - 1
	while h >= l:
		mid = l + (h - l)//2
		if mid != 0 and mid != len(arr) - 1:
			if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
				return arr[mid]
			elif arr[mid - 1] > arr[mid]:
				h = mid - 1
			else:
				l = mid + 1
		elif mid == 0 : 
			if arr[mid] > arr[mid + 1] : return arr[mid]
			else: return arr[mid + 1]
		elif mid == len(arr) - 1:
			if arr[mid] > arr[mid - 1]:
				return arr[mid]
			else : return arr[mid - 1]
	return -1 

def SortArray(arr):
	if len(arr) == 0 : raise ValueError
	i, j = 0, len(arr) - 1
	while i < len(arr) and arr[i + 1] >= arr[i]:
		i += 1
	while j >= 0 and arr[j - 1] <= arr[j]:
		j -= 1
	maxi, mini = max(arr[i + 1 : j]), min(arr[i + 1:j])
	for x in range(0, i):
		if arr[x] > maxi:
			i = x 
	for x in range(j, len(arr)):
		if arr[x] < mini:
			j = x 
	return i, j

def MinOpsToIncrease(arr):
	if len(arr) == 0 : raise ValueError
	count = 0 
	for i in range(1, len(arr)):
		if arr[i - 1] >= arr[i]:
			diff = arr[i - 1] - arr[i] + 1
			count += diff 
			arr[i] = arr[i - 1] + 1
	return count 

def AlternatingNegsAndPos(arr):
	if len(arr) == 0 : raise ValueError
	def Helper(arr):
		i, j = 0, len(arr) - 1
		while i <= j :
			while i < len(arr) and arr[i] >= 0 :
				i += 1
			while j >= 0 and arr[j] < 0 :
				j -= 1
			arr[j], arr[i] = arr[i], arr[j]
			j -= 1
			i += 1
		return i, arr 
	i, arr = Helper(arr)
	k = 1 
	while i < len(arrr):
		arr[k], arr[i] = arr[i], arr[k]
		k += 2 
		i += 1
	return arr 

def MinimumLengthSubarray(arr, target):
	if len(arr) == 0 : raise ValueError 
	res = len(arr) + 1
	l, r = 0, 0 
	prefix = 0 
	while r < len(arr):
		prefix += arr[r]
		while prefix <= target:
			prefix -= arr[l]
			res = min(res, r - l + 1)
			l += 1
		r += 1
	return res 

def SubarrayWithKdistinctElements(arr, k):
	if not arr : raise ValueError
	def Helper(arr, k):
		l, r, count, d = 0, 0, 0, {}
		res = 0 
		while r < len(arr):
			d[arr[r]] = d.get(arr[r], 0) + 1
			if d[arr[r]] == 1 : count += 1
			r += 1
			while count > k:
				d[arr[l]] -= 1
				if d[arr[l]] == 0 : count -= 1
				l += 1
			res = r - l 
		return res 
	return Helper(arr, k) - Helper(arr, k - 1)

