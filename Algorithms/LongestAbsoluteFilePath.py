def LongestAbsoluteFilepath(sti):
	if not sti : raise ValueError 
	list = sti.split('\n')
	d = {}
	res = 0 
	for line in list:
		if '.' not in line:
			key = line.count('\t')
			val = len(line.replace('\t', ''))
			d[key] = val
		else:
			key = line.count('\t')
			length = len(line.replace('\t', '')) + key + sum(d[x] for x in d.keys() if x < key)
			res = max(res, length)
	return res 

sti = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(LongestAbsoluteFilepath(sti))