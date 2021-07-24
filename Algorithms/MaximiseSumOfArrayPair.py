def MaximiseArrayPair(arr):
	if not arr : raise ValueError 
	Sum = 0 
	arr.sort()
	for i in range(0, len(arr), 2):
		Sum += arr[i]
	return Sum 

arr = [1, 4, 3, 2]
print(MaximiseArrayPair(arr))