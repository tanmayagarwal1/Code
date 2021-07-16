def TripletWhichSumToZero(arr):
	res = []
	if not arr : raise ValueError 
	for i in range(len(arr)):
		s = set() # As we are printing all the triplets, declare hashset inside to avoide dups 
		for j in range(i + 1, len(arr)):
			target = -(arr[i] + arr[j])
			if target in s :
				res.append((target, arr[i], arr[j])) 
			s.add(arr[j])
	return res if len(res) >= 1 else False 



def TripletsWhichSumToZeroWithIndex(arr):
	if not arr : raise ValueError 
	res = []
	for i in range(len(arr)):
		d = {}
		for j in range(i + 1, len(arr)):
			target = -(arr[i] + arr[j])
			if target in d:
				res.append((d[target], i, j))
			d[arr[j]] = j 
	return res if len(res) >= 1 else False 

def TripletWhichSumToZeroOptimised(arr):
	# This uses O(1) space 
	if not arr : raise ValueError 
	arr.sort()
	res = []
	for i in range(len(arr)):
		num = arr[i]
		l = i + 1
		r = len(arr) - 1
		while l < r :
			if arr[l] + arr[r] + num == 0 :
				res.append((arr[l], arr[r], num))
				l += 1
				r -= 1
			elif arr[l] + arr[r] + num < 0:
				l += 1
			else:
				r -= 1
	return res 

arr = [0, -1, 2, -3, 1]
print(TripletWhichSumToZeroOptimised(arr))