def unique(sti):
	s=set()
	n=len(sti)
	for i in range(n-1,0,-1):
		j=0 
		while j<i:
			if sti[j]==sti[i]:
				s.add(sti[j])
				j+=1
			j+=1
	for i in range(n):
		if sti[i] not in s:
			print(sti[i])
print(unique('tanmay'))	