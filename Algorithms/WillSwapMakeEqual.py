def WillSwapMakeEqual(sti1, sti2):
	if not sti1 or not sti2 : raise ValueError 
	diff = [[x, y] for x, y in zip(sti1, sti2) if x != y]
	return diff
	if not diff or len(diff) == 2 and diff[0][::-1] == diff[1]:
		return True 
	return False 

sti1 = "bank"
sti2 = 'kanb'
print(WillSwapMakeEqual(sti1, sti2))