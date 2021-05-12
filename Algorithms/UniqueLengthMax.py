def maxLength(arr):
	n=len(arr)
	Solution= ['']
	maxlength = 0 
	for word in arr:
		for strings in Solution:
			temp = word + strings
			if isvalid(temp):
				Solution.append(temp)
				maxlength = max(maxlength, len(temp))
				
	return maxlength, Solution # Returns not only the unique max length, but also the entore unique combinations
def isvalid(s):
	return len(s) == len(set(s))

arr = ["cha","r","act","ers"]
print(maxLength(arr))