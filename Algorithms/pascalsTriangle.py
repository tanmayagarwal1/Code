from math import factorial 
def triangle(n):
	for i in range(n):
		for j in range(i+1):
			print(factorial(i)//factorial(i-j)*factorial(j),end=" ")
		print()
triangle(5)