def AnagramGroup(arr):
	if len(arr) == 0:
		return -1 
	d = dict()
	for word in arr:
		temp = ''.join(sorted(word))
		if temp not in d.keys():
			d[temp] = [word]
		else:
			d[temp].append(word)
	return [word for word in d.values()]

print(AnagramGroup(["eat","tea","tan","ate","nat","bat"]))

