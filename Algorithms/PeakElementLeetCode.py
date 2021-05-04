def peakelements(arr):
	n=max(arr)
	q=[]
	q.append(arr.index(n))
	for i in range(1,arr.index(n)):
		if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
			q.append(i)
	return q 

print(peakelements([1,2,3,4,2,1,5]))
