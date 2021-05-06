def hamming(x,y):
	dx=decimal(x)
	dy=decimal(y)
	lx=len(dx)
	ly=len(dy)
	if lx != ly:
		if lx<ly:
			for i in range(ly-lx):
				dx.insert(i,0)
		elif lx>ly:
			for i in range(lx-ly):
				dy.insert(i,0)

	count=0 
	for i,j in zip(range(len(dx)),range(len(dy))):
		if dx[i]==dy[j]:
			continue
		else:
			count+=1
	return count 

def decimal(x):
	x= '{0:b}'.format(x)
	return [int(i) for i in x]

def totalHamming(arr):
	n=len(arr)
	q=[]
	if n<=1:
		return 0 
	for i in range(n):
		for j in range(i+1,n):
			q.append(hamming(arr[i],arr[j]))
	return sum(q)

print(totalHamming([]))



