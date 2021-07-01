def LongestCommonPrefix(arr):
	if not arr : raise ValueError 
	shortest = min(arr, key = len)
	for i, char in enumerate(shortest):
		for other in arr:
			if other[i] != char:
				return shortest[:i]
	return shortest

arr = ['flights', 'flow', 'flew']
print(LongestCommonPrefix(arr))
