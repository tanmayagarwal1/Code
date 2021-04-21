x=[1,2,3,4]
y=[2,3,4,432,12]
q=[]
i=j=k=0 
while i<len(x) and j<len(y):
	q.append(x[i]+y[j])
	i+=1
	j+=1
while i<len(x):
	q.append(x[i])
	i+=1
while j<len(y):
	q.append(y[j])
	j+=1
print(q)

