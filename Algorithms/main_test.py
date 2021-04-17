####KADEN ALGO 
def maxk(arr):
	n=len(arr)
	i=arr[0]
	j=0 
	for k in range(n):
		j=j+arr[k]
		if i<j:
			i=j
		if j<0:
			j=0 
	return i 
a=[1,21,312,-210,3,24,123,-2,3]
print(maxk(a))		