def PlantPlants(arr, n):
	if not arr : raise ValueError 
	arr, count = [0] + arr + [0], 0
	for i in range(1, len(arr) - 1):
		if arr[i - 1] == arr[i] == arr[i + 1] == 0 :
			count += 1
			arr[i] = 1
	return count >= n 

arr = [1, 0, 0, 0, 1]
n = 2 
print(PlantPlants(arr, n))

