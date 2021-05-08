def StairClimber(n):
	temp1 = 0 
	temp2 = 1
	while n>0:
		temp=temp1 + temp2 
		temp1 = temp2 
		temp2 = temp 
		n -= 1
	return temp2

print(StairClimber(4))