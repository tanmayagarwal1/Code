
# In this problem, given an array we need to find all the subarrays of length three that sum up to zero 
def ThreeSum(arr):
	res = set() # Declare res as set to avoide dups
	if len(arr) == 0 : raise ValueError 
	n, p, z = [], [], [] # List for negative, positives and zeros 
	for num in arr:
		if num > 0 : p.append(num)
		elif num < 0 : n.append(num)
		else: z.append(num)
	N, P = set(n), set(p) # Create set of negs and pos for O(1) lookup
	if z: # If there is atleast one zero 
		for num in P: # Check for conjugate in N i.e : if 2 exists in positives check for -2 in negatives 
			if -1*num in N:
				res.add((-1*num, 0, num)) # If esists add to res 
	if len(z) >= 3:
		res.add((0, 0, 0)) # If there are three zeros : add 3 zeros

	for i in range(len(n)):  # For each pair in n 
		for j in range(i + 1, len(n)):
			target  = -1* (n[i] + n[j]) # Find if there is a conjuagte of the pair sum. If yes add
			if target in P:
				res.add(tuple(sorted([n[i], n[j], target])))
	
	for i in range(len(p)): # Same for positive pairs 
		for j in range(i + 1, len(p)):
			target = -1 * (p[i] + p[j])
			if target in N:
				res.add(tuple(sorted([p[i], p[j], target])))

	return res

arr = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(ThreeSum(arr))