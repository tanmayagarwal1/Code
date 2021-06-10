def NextPermutation(arr):
	if len(arr) == 0 : return -1 
	i, j = len(arr) - 1, len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]: # Reach till the first element of subarray
		i -= 1
	k = i - 1 # pivot
	while arr[j] <= arr[k]:
		j -= k # Stop at the first element greater than the pivot
	arr[k], arr[j] = arr[j], arr[k] # swap pivot and j
	l, h = k + 1, len(arr) - 1 # Start the reverse process of the subarray ( The subarray starts from i or k + 1)
	while h > l :
		arr[l], arr[h] = arr[h], arr[l]
		l += 1
		h -= 1
	return arr

''' In this problem we start from the last index and find a suffix array which is in an decresing order. That means in the given 
    array find a shortest subarray from the end(hence suffix array) from which the elements start to decrease. Eg : [1, 2, 4, 3, 2].
    In that example the elements start decresing from 4. That is 5 the 3 then 2. This is our shortest decresing subarrray. Now
    if the shortest decresing subarray is the entore array itself, just reverse the array and return. Else, pick the element one
    less than the starting element of our subarray as pivot(In our case as k). Now again in the subarray find the first element 
    greater than the pivot. In our subarray([4, 3, 2]) and pivot being - 2, that number will be 3. swap the two numbers. hence now 
    our sub array is [4, 3, 3], and then reverse ths subarray to get the final answer '''

arr = [1,1,5]
print(NextPermutation(arr))

