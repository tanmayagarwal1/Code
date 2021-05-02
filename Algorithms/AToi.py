def atoi(sti):
	arr=sti.split(' ')
	if len(arr)==1 and arr[0]=='': #If the length is one and array itself is blank 
		return 0
	if arr[0]=='': # If first elemet is blank 
		i=0 
		while i<len(arr):
			if arr[i]=='':
				i+=1
			else:
				break 
		if i==len(arr): #If the array is filled with nothing but blanks 
			return 0 
		x=arr[i] #x starts from where the number starts 
	else:
		x=arr[0] #if not blank x will be the first element itself
	if x[0]=='.': #If the first letter is a decimal
		return 0  #return zero because we dont consider 
	for i in range(len(x)):
		if x[i]=='.': #If the first letter is not decimal, find where the decimal point is and cut the array 
			x=x[0:i] #out number output should be before the decimal point 
			break 	#Ypu have to break else i keeps on incrementing
	y=0 
	if x[0]=='-': #Now if the first elemet is minus.(Signs cshould be placed in start only in the input itself)
		count=0  
		for q in range(1,len(x)): #We start from 1 as 0th is the - sign 
			if x[q].isnumeric():
				count+=1      # We find till where we have numbers in a row 
			else:
				break # we need numbers in continous fashion hence the break 
		if count != 0:
			y=int(x[1:count+1]) #If count!=0, means that there are one or more numbers and hence we asign y to the sliced x string 
		else: # Notice we use count+1 in top line for signed case and only count in unsigned case 
			return 0 # IF no numbers then zero 
		if y!=0: 
			if -2147483648<= -y: # Lower bound for y. We need to add the sign explicitly while comparing cause the input's - sign has been discarded in the slice 
				return -int(y)
			else:
				return -2147483648
	elif x[0]=='+':
		count=0 
		for q in range(1,len(x)):
			if x[q].isnumeric():
				count+=1
			else:
				break 
		if count != 0:
			y=int(x[1:count+1]) # Same logic for +
		else:
			return 0 
		if y!=0:
			if y<2147483648:
				return int(y)
			else:
				return 2147483647
		else:
			return 0 
	else:
		count=0 
		for q in range(0,len(x)):
			if x[q].isnumeric():     #Same logic for no sign but here we start from 0 as no sign 
				count+=1
			else:
				break 
		if count != 0:
			y=int(x[0:count])
		else:
			return 0
		if int(y)<2147483648:
			return int(y)
		else:
			return 2147483647

print(atoi("  +0a32"))