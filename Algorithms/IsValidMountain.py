def MountainArray(arr):
	if not arr : raise ValueError 
	if len(arr) < 3 : return False 
	i = 0 
	j = len(arr) - 1
	while arr[i + 1] > arr[i] and i < len(arr):
		i += 1
	while arr[j - 1] > arr[j] and j >= 0:
		j -= 1
	if i ==j  and i != 0: return True
	return False 
	 

arr = [9,8,7,6,5,4,3,2,1,0]
print(MountainArray(arr))