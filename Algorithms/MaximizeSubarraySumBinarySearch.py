def SplitArrayToMsubarraysMinimizeSum(arr, max_subarray_count):
	# We need to split an array in 'max_subarray_count' subarrays while minimising the sum 
	# We use binary search on answer space 

	def IsValid(arr, max_sum, max_subarray_count):
		# mid is nothing but the answer search space which is the minimized sum 
		# We are basicallt checking wheter or not the array can be split into the desired 'max_subarray_count' number of subarrays by maintaining 
		# - 'mid (max_sum)' sum in each array 
		# If yes we minimise the search space (h = mid - 1) , else maximise it (l = mid + 1)

		curr_sum = 0 
		curr_subarray_count = 1
		for curr_num in arr:  # Start iterating the array. ( Basically and literally the same approach used in boats and partitions and splits )
			curr_sum += curr_num
			if curr_sum > max_sum: # If the curr_sum exceeds the max_sum, we need to increase subarray count ( As we need to make another subarray )
				curr_sum = curr_num
				curr_subarray_count += 1
			if curr_subarray_count > max_subarray_count : 

				# If curr_subarray_count id more than max_subarray_count then clearly we need more subarrays to reach our max_sum and hence we return false  
				return False 

		return True 

	if not arr : raise ValueError 
	l, h = max(arr), sum(arr)
	while h >= l:
		mid = l + (h - l)//2
		if IsValid(arr, mid, max_subarray_count):
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return res 

arr = [7,2,5,10,8]
max_subarrays_that_must_be_formed = 2 
print(SplitArrayToMsubarraysMinimizeSum(arr, max_subarrays_that_must_be_formed))