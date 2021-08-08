def PartitionPalindrome(sti):
	if not sti : raise ValueError 
	def isPal(l, r):
		if l >= r : return True 
		if sti[l] != sti[r] : return False 
		return isPal(l + 1, r - 1)

	def Helper(i):
		if i == len(sti) : return 0 
		ans = float('inf')
		for j in range(i, len(sti)):
			if isPal(i, j):
				ans = min(ans, Helper(j + 1) + 1)
		return ans 

	return Helper(0) - 1 



sti = "aab"
print(PartitionPalindrome(sti))