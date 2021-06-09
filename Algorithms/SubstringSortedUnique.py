def SortedUniqueSubstrings(sti):
	if len(sti) == 0:
		return -1 
	res = []
	for i in range(len(sti)):
		for j in range(i + 1, len(sti)):
			res.append(sti[i:j])
	return sorted(list(set(res)))

def RepeatedSubstring(sti): # To check if a given string van be formed using its substrings
	my_sti = ''.join((sti[1:], sti[:-1]))
	return my_sti


string = 'abcabc'
print(RepeatedSubstring(string))
print(SortedUniqueSubstrings(string))
