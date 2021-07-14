def Sqrt(x):
	if not x : raise ValueError
	l, h = 0, x + 1
	while h >= l:
		mid = l + (h - l)//2
		if mid * mid > x:
			res = mid 
			h = mid - 1
		else:
			l = mid + 1
	return (res - 1)**2


	return res 

print(Sqrt(8))