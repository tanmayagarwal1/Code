import timeit 

def For_test():
	for i in range(0, 100000000):
		pass 


####################################
def while_test():
	i = 0 
	while i < 100000000:
		i += 1

print(timeit.timeit(For_test, number = 10))
print(timeit.timeit(while_test, number = 10))