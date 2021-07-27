def Rankelements(arr):
	if not arr : raise ValueError 
	new = arr[:]
	new.sort()
	d = {}
	rank = 1 
	res = []
	for num in new:
		if num not in d:
			d[num] = rank 
			rank += 1
	for num in arr:
		res.append(d[num])
	return res 

arr = [37,12,28,9,100,56,80,5,12]
print(Rankelements(arr))