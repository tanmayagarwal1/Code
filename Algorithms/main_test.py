def AnagramGroups(arr):
	if len(arr) == 0 :
		return -1 
	d = dict()
	for word in arr:
		temp = ''.join(sorted(word))
		if temp in d.keys():
			d[temp].append(word)
		else:
			d[temp] = [word]
	return [x for x in d.values()]


