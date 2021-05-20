def MinStepsFoeEqualHeight(heights):
	n = len(heights)
	heights.sort()
	a, steps = heights[::-1], 0 
	for i in range(1, len(a)):
		steps += i if a[i-1] != a[i] else 0 
	return steps 
print(MinStepsFoeEqualHeight([5, 2, 1]))