
# Minimum operations to split given bag. Here we decide the cost of split as the seatrch space for binary search 
# Number of splits is defined by the sum of the division of each element in the array with the current mid - 1
# thta is because the mid decides what will be the penalty for each split and as the panalty = max size of ball, there cannot be more than 'mid' amount of 
# - elements in the split at a time 
# And we subtract from one becasue to lets say we have 10 as a number in array. Now to split it with penalty 4 we do it as : 4 4 2 
# The number of new bags (each element in array denotes a bag, read problem description ) does become 3 but we only split it twice. 
# ie : 10 becomes 4 and 6 first (one split) and then 6 becomes 4 and 2 ( 1 split ). hence combined they become 1 + 1 split = 2 split = ( 3 - 1 )

def NumberOfSlipts(arr, ops):
	if not arr : raise ValueError 
	l, h = 1, max(arr) 
	while h >= l : 
		mid = l + (h - l)//2
		if sum((num - 1) // mid for num in arr) > ops:
			l = mid + 1
		else:
			h = mid - 1
	return l

arr = [2, 4, 8, 2]
ops = 4 
print(NumberOfSlipts(arr, ops))
