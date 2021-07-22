def PartitionDisjoint(arr):
	if not arr : raise ValueError 
	Right = [0] * len(arr)
	Right[len(arr) - 1] = arr[len(arr) - 1]
	for i in range(len(arr) - 2, -1, -1):
		Right[i] = min(arr[i], Right[i + 1])
	return Right
	Left = arr[0]
	for i in range(1, len(arr)):
		if Left <= Right[i]:
			return i 
		Left = max(Left, arr[i])

arr = [5,0,3,8,6]
print(PartitionDisjoint(arr))
