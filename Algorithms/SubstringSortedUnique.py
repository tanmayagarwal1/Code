def SortedUniqueSubstrings(sti):
	if len(sti) == 0:
		return -1 
	res = []
	for i in range(len(sti)):
		for j in range(i + 1, len(sti)):
			res.append(sti[i:j])
	return sorted(list(set(res)))


string = 'abcabc'
print(SortedUniqueSubstrings(string))
