def median(li1,li2):
	s=li1+li2
	s.sort()
	n=len(s)
	index=(n-1)//2

	if n%2:
		return s[index]
	else:
		return (s[index]+s[index+1])/2
print(median([1,3],[2]))