def FirstOccurance(grid):
	if len(grid) == 0:
		return - 1
	for i in range(len(grid)):
		index = OptimisedBinary(grid[i], 0, len(grid[0]) - 1)
		if index : break
	return i, index 

def OptimisedBinary(arr, l, h):
	if h < l : return 0 
	while h >= l :
		mid = (l + h)//2
		if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
			return mid 
		elif arr[mid] == 0:
			l = mid + 1
		else:
			h = mid - 1
	return 0 

grid = [[0,0,0],[0,1,1],[1,1,1]]
print(FirstOccurance(grid))