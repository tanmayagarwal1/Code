def MaxProductPair(arr):
	if not arr : raise ValueError 
	big1, big2, neg1, neg2 = 0, 0, 0, 0
	for i in range(len(arr)):
		if arr[i] > big1:
			big2 = big1 
			big1 = arr[i]
		elif arr[i] > big2:
			big2 = arr[i]
		elif arr[i] < 0 and abs(arr[i]) > neg1:
			neg2 = neg1
			neg1 = arr[i]
		elif arr[i] < 0 and abs(arr[i]) > neg2:
			neg2 = arr[i]

	return (big1, big2) if big2 * big1 > neg1 * neg2 else (neg1, neg2)



arr = [-1, -3, -4, 2, 0, -5]
print(MaxProductPair(arr))

