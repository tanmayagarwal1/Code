def BeautifulArray(n):
	if not n : raise ValueError 
	return sorted(range(1, n + 1), key = lambda x : bin(x)[:1:-1])

n = 5 
print(BeautifulArray(5))