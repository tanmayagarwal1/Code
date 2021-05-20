def anagramgroup(arr):
	if len(arr) == 0:
		return - 1
	d = dict()
	for word in arr:
		temp = ''.join(sorted(word))
		if temp not in d.keys():
			d[temp] = [word]
		else:
			d[temp].append(word)
	return [words  for words in d.values()]
print(anagramgroup(["eat","tea","tan","ate","nat","bat"]))
