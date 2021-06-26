# Given the number of rows of a matrix find the number of ways each cell in the matrix can be coloured such that : 
# No two adjacent cells either vertical or horizontal will be off the same colour eg : 112 is not possible as same colour for 2 cells adjacent


def ColorGrid(n):
	a121, a123 = 6, 6 
	for _ in range(n - 1):
		a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2 
	return (a121 + a123) % (10**9 + 7)

print(ColorGrid(5000))

# In this problem we find the realtion that each row can be encoded with either 2 or 3 colours beacsue we useonly one colour the - 
# the adjacent cells will not be of distinct colours. 
# Hence we initialise 3 varialbles a121 and a123 denoting colour matrix by 2 colours (a121 - 1, 2, 3 represent three colours)
# and a123 => 3 distinct colours. Now using two colours and two colours only we can fill the given row 6 ways i.e : 121, 131, 212, 232, 313, 323.
# and using only 3 colours we can fill the row 6 ways : 123, 132, 213, 231, 312, 321.. Hence initially a121 and a123 = 6 and 6 
# Now if the first row is 121 then the next row cannot be 131 and 323 beauce if we choose any of the two there will be clasing 
# Clashing means consider the following situation :
#
#    row 1 = 1 2 1 
#    row 2 = 1 3 1 
#
# Now we can see that in a col ( Vertical cells ) 1 and 1 are clasing which this is against the given constraint that no two adjacent cells must have 
# the same colour

# Hence the possible combinations are : for a121 : next rows can be either 212, 232, 313 ( 3 ways to use 2 colour ) or 213 and 312 ( 2 ways to use 3 colours )
# HENCE => a121 = a121 * 3 + a123 * 2 

# Similarly if the first row starts with three colours i.e : 123 possibilities for next row are : 212 and 232 ( 2 ways for 2 colours ) and 231, 312 
# ( 2 ways for 3 colours )
# HENCE => a123 = a121 * 2 + a123 * 2 


