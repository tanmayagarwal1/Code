
# In this we use expanding from the center approach. For odd cases we expand from the same index (And hence i, i) and for even 
# We expand from the middle two i.e : i, i + 1
# Now we only increment j and decrement i if sti[i] == sti[j], else we return sti[i + 1:j]
# [i + 1, j] because the palindrome substring will be between i and j ( as the loops stops only when sti[i] != sti[j] and hence -
# i and j end at an index at which the strings are not equal)
def LongestPalindromicSubstring(sti):
	if len(sti) == 0 : raise ValueError
	res = ''
	def Longest(sti, i, j):
		while i >= 0 and j < len(sti) and sti[i] == sti[j]:
			i -= 1
			j += 1
		return sti[i + 1:j]
	for i in range(len(sti)):
		odd = Longest(sti, i, i)
		even = Longest(sti, i, i + 1)
		res = max(res, odd, even, key = len)
	return res 

sti = "babad"
print(LongestPalindromicSubstring(sti)) # bab 