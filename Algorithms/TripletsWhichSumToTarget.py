def TripletsWhichSumToValue(arr, target): # Without index we use a hashset 
	if not arr : raise ValueError
	curr_sum = 0 
	s = set()
	for i in range(len(arr)):
		curr_sum = target - arr[i]
		for j in range(i + 1, len(arr)):
			if curr_sum - arr[j] in s :
				return True, arr[i], arr[j], curr_sum - arr[j]
			s.add(arr[j])
	return False 


def TripletSumWithIndex(arr, target): # With Index we use a hashmap 
	if not arr : raise ValueError 
	d = {}
	for i in range(len(arr)):
		curr_target = target - arr[i]
		for j in range(i + 1, len(arr)):
			if curr_target - arr[j] in d:
				return i, j, d[curr_target - arr[j]]
				return True 
			d[arr[j]] = j 
	return - 1


arr = [1, 2, 3, 4, 5, 100]
target = 109
print(TripletsWhichSumToValue(arr, target))
print(TripletSumWithIndex(arr, target))