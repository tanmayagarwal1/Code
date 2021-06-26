def KnightDialer(N):
	x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1 
	for _ in range(N - 1):
		x1 , x2 , x3 , x4 , x5 , x6 , x7 , x8 , x9 , x0 = \
		x6 + x8, \
		x7 + x9, \
		x4 + x8, \
		x3 + x9 + x0, \
		0, \
		x1 + x7 + x0, \
		x2 + x6, \
		x1 + x3, \
		x4 + x2, \
		x4 + x6
	return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)

# Each x represents a digit on the number pad. We initialise each x to one. And then we iterate over the loop and change the value of each x based 
# On which numbers can the knight reach after starting at the given x. for instance, if the knight is at x1 ( number 1 ) it can go to x6 ( number 6 )
# or x8 ( number 8 ). Hence we do x1 = x6 + x8. Similarly from x2 we can go to x7 and x9 and hence x2 = x7 + x9 and so on 


print(KnightDialer(3131))