import heapq
def Subsets(arr):
	if not arr : raise ValueError 
	sol = [[]]
	for num in sol:
		sol += [curr + [num] for curr in sol]
	return sol 

def subsets2(arr):
	return [[arr[i] for i in range(len(arr)) if bit & 1<<i != 0] for bit in range(1<<len(arr))]

def NextGreatest(arr):
	if not arr : raise ValueError 
	i, j = len(arr) - 1, len(arr) - 1
	while i >= 0 and arr[i - 1] >= arr[i]:
		i -=1 
	if i == 0 :
		arr.reverse()
		return arr 
	while arr[j] <= arr[k]:
		j -= 1
	arr[k], arr[j] = arr[j], arr[k]
	l, h = k + 1, len(arr) - 1
	while h >= l :
		arr[l], arr[h] = arr[h], arr[l]
		h -= 1
		l += 1
	return arr 

def ProductArray(arr):
	if not arr:
		raise ValueError
	res = [1]* len(arr)
	for i in range(1, len(arr)):
		res[i] = res[i - 1] * arr[i - 1]
	prod = 1 
	for i in range(len(arr) - 1, -1, -1):
		res[i] = res[i] * prod 
		prod = prod * arr[i]
	return res 

def MonotonicArray(num):
	if not num : raise ValueError
	arr = [int(i) for i in num[::-1]]
	idx = -1
	for i in range(1, len(arr)):
		if arr[i] > arr[i - 1] or (idx != -1 and arr[idx] == arr[i]):
			idx = i 
	if idx == - 1: return num 
	for j in range(idx):
		arr[j] = 9 
	arr[idx] -= 1
	return int(''.join(str(i) for i in arr[::-1]))
def LongestValidMountain(arr):
	if not arr : raise ValueError 
	res = 0 
	for i in range(1, len(arr) - 1):
		if arr[i - 1] < arr[i] > arr[i + 1]:
			l = r = i
			while l > 0 and arr[l - 1] < arr[l]:
				l -= 1
			while r + 1 < len(arr) - 1 and arr[r + 1] < arr[r]:
				r += 1
			res = max(res, r - l + 1)  
	return res 


def MinWorkers(wages, qual, k):
	if not wages or not qual : raise ValueError
	expected = sorted([float(w/q), q] for w, q in zip(wages, qual))
	pq = []
	Qsum = 0
	res = float('inf')
	for r, q in expected:
		heapq.heappush(pq, -q)
		Qsum += q 
		if len(pq) > k : Qsum += heapq.heappop(pq)
		if len(pq) == k : res = min(res, Qsum * r)
	return res 

def MaximumEfficiency(s, e, k):
	if not s and e : raise ValueError
	arr = sorted([[eff, spee]  for eff, spee in zip(e, s)], reverse = True)
	Ssum = 0 
	pq = []
	res = 0
	for effi, speed in arr:
		heapq.heappush(pq, speed)
		Ssum += speed
		if len(pq) > k : Ssum -= heapq.heappop(pq)
		res = max(res, Ssum * effi)
	return res 

n = 6 
k = 3 
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
print(MaximumEfficiency(speed, efficiency, k))



