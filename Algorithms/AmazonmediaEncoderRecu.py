def MediaEncoder(fileSizes):
	if len(fileSizes) <= 1:
		return 0
	else:
		a = min(fileSizes)
		fileSizes.remove(a)
		b = min(fileSizes)
		fileSizes.remove(b)
		fileSizes.append(a+b)
		return a + b + MediaEncoder(fileSizes)

arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(MediaEncoder(arr))