def maxSum(arr,k):
	n=len(arr)
	window=sum(arr[:k])
	max_sum=0
	for i in range(n-k):
		window=window-arr[i]+arr[i+k]
		max_sum=max(max_sum,window)
	return max_sum

def maxelement(arr,k):
	n=len(arr)
	if k>n:
		return 0 
	q=[]
	for i in range(k):
		q.append(arr[i])
	maximum=float('-inf')
	for j in range((n-k)+1):
		for i in range(k):
			maximum=max(maximum,q[i])
		q.pop(0)
		if j+k<n:
			q.append(arr[j+k])
	return [maximum]
res=(maxelement([1,2,3,4,5,6,7,8,9,10,11],3))
print(res)

