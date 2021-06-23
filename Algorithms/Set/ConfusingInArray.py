def BeautifulArrangement(n):
	if n == 0 : return -1 
	arr = [i for i in range(1, n + 1)]

	def Arrange(arr, path, res, idx):
		if not arr : 
			res.append(path)
			return 
		for i, num in enumerate(arr):
			if num % idx == 0 or idx % num == 0:
				Arrange(arr[:i] + arr[i + 1:], path + [arr[i]], res, idx + 1)
	res = []
	Arrange(arr, [], res, 1)
	return len(res)

def ProductArray(arr):
	if len(arr) == 0: return - 1
	res = [1]*len(arr)
	for i in range(1, len(arr)):
		res[i] = res[i - 1]* arr[i - 1]
	prod = 1
	for i in range(len(arr) - 1, - 1, -1):
		res[i] = prod * res[i]
		prod = prod * arr[i]
	return res 

def EqualsToK(arr, k):
	if len(arr) == 0 : return - 1
	d = {0 : 1}
	prefix, count = 0, 0 
	for num in arr:
		prefix += num 
		if prefix - k in d:
			count += d[prefix - k]
		d[prefix] = d.get(prefix, 0) + 1
	return count 

def DivisibleK(arr, k):
	if len(arr) == 0 : return -1 
	d = {0 : 1}
	prefix, count = 0, 0
	for num in arr:
		prefix += num 
		key = prefix % k 
		if key in d:
			count += d[key]
		d[key] = d.get(key, 0) + 1
	return count 

def TwoSum(arr, target):
	if len(arr) == 0 : return - 1
	d = dict()
	for i in range(len(arr)) :
		if target - arr[i] in d:
			return i, d[target - arr[i]]
		d[arr[i]] = i 
	return False 

def NextPermutation(arr):
	if len(arr) == 0 : return -1 
	i, j = len(arr) - 1, len(arr) - 1
	while i >= 0 and arr[i - 1] > arr[i]:
		i -= 1
	if i == 0 :
		arr.reverse()
		return arr 
	pivot = i - 1
	while arr[j] <= pivot:
		j -= 1
	arr[j], arr[pivot] = arr[pivot], arr[j]
	l, h = k + 1, len(arr) - 1
	while h >l :
		arr[h], arr[l] = arr[l], arr[h]
		h -= 1
		l += 1
	return arr 

def PeakElement(arr):
	if len(arr) == 0:
		return - 1
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
	 		if arr[mid] > arr[mid - 1] : return arr[mid] 
	 		else : return arr[mid - 1]
	return -1 

def SubarraySorts(arr):
	if len(arr) == 0 : return -1 
	i, j = 0, len(arr) - 1
	while i < len(arr) - 1 and arr[i + 1] > arr[i]:
		i += 1
	while j >= 0 and arr[j - 1] <= arr[j]:
		j -= 1
	maxi, mini = max(arr[i:j]), min(arr[i:j])
	for x in range(i + 1):
		if arr[x] > mini:
			i = x 
	for x in range(len(arr) - 1, j, -1):
		if arr[x] < maxi:
			j = x 
	return i, j

def QuickSort(arr):
	if len(arr) == 0 : return -1 

	def partition(arr, l, h):
		i = l - 1
		pivot = arr[h]
		for x in range(l, h):
			if arr[x] <= pivot:
				i += 1
				arr[x], arr[i] = arr[i], arr[x]
		arr[i + 1], arr[h] = arr[h], arr[i + 1]
		return i + 1

	def QuickSortUtil(arr, l, h):
		if h < l : return 
		if h >= l : 
			mid = partition(arr, l, h)
			QuickSortUtil(arr, l, mid - 1)
			QuickSortUtil(arr, mid + 1, h)
			return 
	QuickSortUtil(arr, 0, len(arr) - 1)

def Rotate(arr, k):
	if len(arr) == 0 :
		return -1 
	i, j = 0, len(arr) - 1
	mid = j -  k % len(arr)

	def reverse(arr, l, h):
		while h > l:
			arr[h], arr[l] = arr[l], arr[h]
			h -= 1
			l += 1

	reverse(arr, i, mid) # We do only l - mid and not low - (mid - 1) because, above we say that mid = h - k % len and h is already len(arr) - 1
	reverse(arr, mid + 1, j)
	reverse(arr, i, j)
	return arr 


# Beautiful Arrangement
n = 3 
print(BeautifulArrangement(n))

# Product Array 
arr = [1, 2, 3, 4, 5]
print(ProductArray(arr)) # [120, 60, 40, 30, 24]

# Two sum 
target = 14
arr = [2, 3, 4, 5, 6, 7, 8] # (4, 6)
print(TwoSum(arr, target))

# Subarray Sum equal to k 
arr = [1, 2, 3]
k = 3
print(EqualsToK(arr, k)) # 2

# subarray sum divisble by k 
arr = [4,5,0,-2,-3,1]
k = 5 
print(DivisibleK(arr, k)) # 7 

# Next Permutation 
arr = [1,1,5]
print(NextPermutation(arr)) # [1, 5, 1]

# Peak Element 
arr = [2, 23, 90, 67]
print(PeakElement(arr)) # 90

# Subarray Sorts the array
arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
print(SubarraySorts(arr)) # (30, 35) => Nums ; (3, 8) => Indices

# Rotate 
arr = [1,2,3,4,5,6,7]
k = 3
print(Rotate(arr, k)) # [5,6,7,1,2,3,4]

a=[123,2324,3212,32,-132,-12312,234,-213,23,232,-23,12,3123,12,-23,13,-32134324]
QuickSort(a)
print(a)
