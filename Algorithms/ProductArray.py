
# Create two arrays as prefix and suffix. Prefix will have 0th index as 1 and suffix will have n - 1 index as 1. Rest is Trivial
def ProductArray(arr):
	if len(arr)  == 0:
		return - 1
	prefix, suffix, prod = [1 for _ in range(len(arr))], [1 for _ in range(len(arr))], [0 for _ in range(len(arr))]

	for i in range(1, len(arr)): # Start from 1st element
		prefix[i] = prefix[i - 1] * arr[i - 1] # Prefix stores till last but one element

	for i in range(len(arr) - 2, -1, -1): # Start from second element from last
		suffix[i] = suffix[i + 1] * arr[i + 1] # Suffix stores till 0th index (inclusive)

	for i in range(len(arr)):
		prod[i] = suffix[i] * prefix[i]

	return prod


arr = [1, 2, 3, 4]
print(ProductArray(arr))