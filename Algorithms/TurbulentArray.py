def TurbulentArr(arr):
	if not arr : raise ValueError 
	best, curr = 0, 0 
	for i in range(len(arr)):
		if i >= 2 and ((arr[i - 2] < arr[i - 1] >arr[i]) or (arr[i - 2] > arr[i - 1] < arr[i])):
			curr += 1 
		elif i >= 1 and arr[i - 1] != arr[i]:
			curr = 2 
		else:
			curr = 1 
		best = max(best, curr)
	return best 

arr = [9,4,2,10,7,8,8,1,9]
