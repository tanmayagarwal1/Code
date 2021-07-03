def KFrequentElements(arr, k):
	if not arr : raise ValueError 
	d = dict()
	for num in arr:
		d[num] = d.get(num, 0) + 1
	buckets = [[] for _ in range(len(arr))]
	for num, freq in d.items() : buckets[freq].append(num)
	res = []
	for i in range(len(buckets) - 1, -1, -1):
		bucket = buckets[i]
		if bucket:
			for num in bucket :
				res.append(num)
	return res[:k]

# We solve this probelm using bucket sort 
# This gives us O(n) compared to O(nlogk)[ Heap ] but uses O(n) memory too
# In this the main idea is : the maximum freq of a number will not be greater than the size of the array 
# Hence we create a buckets array with blank arrays representing a freq bucket 
# eg : buckets[1] => comprises of a list which contains elements with freq 1 ( Initially empty )
# eg : buckets[3] => comprises of a list which contains elements with freq 2 ( Initially empty )
# Now we store freq in a dict 
# for every freq in the dict we use the corresponding freq bucket and store the num => buckets[freq].append(num) 
# Now our buckets is a list of list. We need to flatten it 
# So we iterate over our 2D buckets list from the end ( As the end contains elements with the highest freq. (Highest freq buckets start from end))
# For every bucket in bucket(s), if bucket is not empty, we append the element in the res array ( Order does not matter )
# Finally we return [:k] from our res as the numbers are sorted based on freq in descending order 

arr = [1,1,1,2,2,3]
k = 2
print(KFrequentElements(arr, k))