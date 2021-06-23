def ProductSearch(arr, target):
	if len(arr) == 0 : return -1 
	d = dict()
	for i in range(len(arr)):
		if target // arr[i] in d and target % arr[i] == 0 and target % arr[d[target // arr[i]]] == 0 :
			return d[target // arr[i]], i 
		d[arr[i]] = i 

arr = [2, 3, 4, 5, 6]
target = 20
print(ProductSearch(arr, target)) # (2, 3)