def DecodeWays(sti):
	if not sti : raise ValueError 
	d = {'' : 1}
	def Helper(sti):
		if sti in d : return d[sti]
		if sti[0] == '0' : return 0 
		single_split = Helper(sti[1:])
		two_split = Helper(sti[2:]) if int(sti[:2]) <= 26 and len(sti[:2]) == 2 else 0 
		d[sti] = single_split + two_split 
		return d[sti]
	return Helper(sti)

sti = '12'
print(DecodeWays(sti))