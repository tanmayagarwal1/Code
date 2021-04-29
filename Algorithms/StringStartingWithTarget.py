def out(arr,target):   
	q=[]       #BOTH are strings 
	for i in arr: 
		z=0
		count=0 
		while z<len(target):
			if i[z]==target[z] :
				count+=1
				z+=1
			else:
				break 
			if y==len(target):
				q.append(i)
	return q 
print(out(['dog','dark','cage','door','dodge'],'do'))

	
