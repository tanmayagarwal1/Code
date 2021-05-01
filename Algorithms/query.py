#two indexes i and j 
def query(arr,li):
	n=len(arr)
	res=[]
	for i in li:
		q=[]
		if i[0]==i[1]:
			res.append(arr[i])
		for j in range(i[0]-1,i[1]):
			q.append(arr[j])
		count=q[0]
		for k in range(len(q)):
			count=min(count,q[k])
		res.append(count)
	return res 
	

print(query([2,3,4,5,4,1,1,3],[(2,6),(3,5),(6,8)]))
