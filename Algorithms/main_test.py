def houses(arr,budget):
	n=len(arr)
	q=[]
	for i in range(n-1,-1,-1):
		if arr[i]>budget:
			continue 
		initial=arr[i]
		count=1
		for j in range(n):
			if j==i:
				continue 
			if initial+arr[j]<=budget:
				initial=initial+arr[j]
				count +=1
		q.append(count)
	if not q:
		return 0 
	res=q[0]
	for i in range(len(q)):
		res=max(res,q[i])
	return res 


print(houses([999,999,999],300))

		 
