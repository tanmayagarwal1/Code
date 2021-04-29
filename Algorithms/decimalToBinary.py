'''
Convert decimal number to binary and change the 5th bit to 1 

'''

def convert(num):
	k=int('{0:b}'.format(num)) #Converting orinal number to binary(note that we have to explicityly typecast back to int)
	print("original number {}".format(k))
	arr=[int(i) for i in str(k)] #Converting the number into an array so that we can acess individual elements 
	if arr[4]!=1:
		arr[4]=1 
	x=[str(i) for i in arr] #converting the int array to str array so that we can join again 
	return 'Converted is {}'.format(''.join(x)) # join and return 
print(convert(22))
