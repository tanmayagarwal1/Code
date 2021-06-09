def SplitString(sti):
	if len(sti) == 0:
		return -1 
	count0, count1, cnt = 0, 0, 0
	for char in sti:
		if char == '0':
			count0 += 1
		elif char == '1':
			count1 += 1
		if count0 == count1:
			cnt += 1
	return cnt if cnt else -1

sti = '0111100010'
print(SplitString(sti))

