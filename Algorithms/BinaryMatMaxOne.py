def FirstOccurance(grid):
	if len(grid) == 0:
		return - 1
	res = 0
	for i in range(len(grid)):
		index = OptimisedBinary(grid[i], 0, len(grid[0]) - 1)
		if index == -1 : continue
		Number_occu = len(grid[0]) - index
		if res < Number_occu:
			res = Number_occu
			my_idx = i
	return res, my_idx

def OptimisedBinary(arr, l, h):
	if h < l : return -1 
	while h >= l :
		mid = (l + h)//2
		if arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0):
			return mid 
		elif arr[mid] == 0:
			l = mid + 1
		else:
			h = mid - 1
	return -1

grid = [[0,0,0],[0,1,1],[1,1,1]]
print(FirstOccurance(grid))