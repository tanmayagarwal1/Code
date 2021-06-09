def SortMarks(arr):
	if len(arr) == 0:
		return -1 
	return sorted(arr, key = lambda x : (x.split(' ')[1], x.split(' ')[0]))

arr = ['A 79', 'B 76', 'C 79', 'D 45']
print(SortMarks(arr))