def tribonocci(n):
	if n<=0:
		return 0 
	t1=0 
	t2=1
	t3=1
	while n>2:
		t=t1+t2+t3
		t1,t2=t2,t3
		t3=t
		n-=1
	return t3 
print(tribonocci(1))