'''
In this problem we need to calculate the number of ways to reach a desired stair. To do this
we just need to return the fibonocci numver of the input(n)+1. 

NOTE : In the loop we used n>0. This is done so that we can get the fib of n+1. If we want the 
actual fib value of the input just use n>1
'''

def stairs(n):
	i=0 
	j=1 
	while n>0:
		t=i+j
		i=j 
		j=t 
		n-=1
	return j 

print(stairs(2))