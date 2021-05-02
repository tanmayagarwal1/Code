def atoi(sti):
	arr=sti.split(' ')
	if len(arr)==1 and arr[0]=='':
		return 0
	if arr[0]=='':
		i=0 
		while i<len(arr):
			if arr[i]=='':
				i+=1
			else:
				break 
		if i==len(arr):
			return 0 
		x=arr[i]
	else:
		x=arr[0]
	if x[0]=='.':
		return 0
	for i in range(len(x)):
		if x[i]=='.':
			x=x[0:i]
			break 	
	y=0 
	if x[0]=='-':
		count=0 
		for q in range(1,len(x)):
			if x[q].isnumeric():
				count+=1
			else:
				break 
		if count != 0:
			y=int(x[1:count+1])
		else:
			return 0 
		if y!=0:
			if -2147483648<= -y:
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
			y=int(x[1:count+1])
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
			if x[q].isnumeric():
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