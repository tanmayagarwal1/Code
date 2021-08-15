def MinWindowSubstring(sti, target):
	if not sti or not target : raise ValueError 
	d = {}
	for char in target:
		d[char] = d.get(char, 0) + 1 
	i, j = 0, 0 
	req = len(target)
	res = len(sti) + 1 
	while j < len(sti):
		if sti[j] in d:
			if d[sti[j]] > 0 : req -= 1
			d[sti[j]] -= 1 
		while req == 0 : 
			res = min(res, j - i + 1)
			output = sti[i:j + 1]
			if sti[i] in d:
				d[sti[i]] += 1 
				if d[sti[i]] > 0 : req +=1  
			i += 1 
		j += 1 

	return "" if res == len(sti) + 1 else output 

s = "ADOBECODEBANC"
t = "ABC"
print(MinWindowSubstring(s, t))
