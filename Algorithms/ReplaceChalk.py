def ReplaceChalk(arr, k):
	if not arr : return
	Sum = sum(arr)
	tmp = k % Sum 
	for idx, num in enumerate(arr):
		if tmp < num : return idx 
		tmp -= num 
	return -1 

arr = [3, 4, 1, 2]
print(ReplaceChalk(arr, 25)) 