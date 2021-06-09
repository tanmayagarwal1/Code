def Sting(boxList):
	new_gen, old_gen = [], []
	for box in boxList:
		char = box.split(' ')[1]
		if char.isnumeric():
			new_gen.append(box)
		else:
			old_gen.append(box)
	return old_gen
	old_gen.sort(key = lambda x : (x.split(' ')[1:], x.split(' ')[0]))
	old_gen.extend(new_gen)
	return old_gen





arr = ['ykc 82 01', 'eo first qpx', '09z cat ham', '06f 12 25 6', 'az0 first qpx', '236 cat dog rabbit']
print(Sting(arr))