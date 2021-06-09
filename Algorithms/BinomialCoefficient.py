
# Fastest Binaomial Coeff sol. Time : O(1), Space : O(1)

def BinomialCoefficients(N, R):
	if R < 0 or R > N:
		return 0 
	b = 1 
	for i in range(min(R, (N - R))):
		b *= N
		b //= i + 1
		N -= 1
	return b 

print(BinomialCoefficients(5, 2))