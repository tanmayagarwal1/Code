# Break Palindrome to lexicographically smallest

def breakPalindrome(sti):
	if not sti : raise ValueError 
	for i in range(len(sti)//2):
		if sti[i] != "a":
			return sti[:i] + "a" + sti[i + 1:]
	return sti[:-1] + "b" if sti[:-1] else ""

sti = "abccba"
print(breakPalindrome(sti))