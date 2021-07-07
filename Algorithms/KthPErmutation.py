def KthPermutation(n, k):
	if not n : raise ValueError 
	arr = [i for i in range(1, k + 1)]
	res = []
	from math import factorial 
	fact = factorial(n - 1)
	k -= 1 # Out index begins from 0 hence do k - 1 
	for i in range(n - 1, 0, -1): # leave one element in the array 
		idx = int(k //fact)
		k = k % fact
		res.append(str(arr[idx]))
		arr.pop(idx)
		fact = fact / i 
	res.append(str(arr[0]))
	return ''.join(res)

n = 4 
k = 9 
print(KthPermutation(n, k))
