def ContainerWithMostWater(arr):
	if not arr : raise ValueError 
	i, j = 0, len(arr) - 1
	water = 0 
	while i < j :
		water = max(water, (j - i) * min(arr[i], arr[j]))
		if arr[i] <= arr[j]:
			i += 1
		else:
			j -= 1
	return water 

arr = [1,8,6,2,5,4,8,3,7]
print(ContainerWithMostWater(arr))