# given a number check if the digits are incresing. If not return the largest monotonic number 
def MonotonicArray(x):
	if not x : raise ValueError 
	n = x 
	arr = [int(i) for i in str(n)[::-1]] # Trun the number into an array in reverse order ( We wanna go from lsb to msb )
	idx = -1 
	for i in range(1, len(arr)):
		if arr[i] > arr[i - 1] or (idx != -1 and arr[idx] == arr[i]) :
			idx = i 
	if idx == -1 : return n 
	for i in range(idx):
		arr[i] = 9 
	arr[idx] -= 1
	return int(''.join([str(i) for i in arr[::-1]]))


print(MonotonicArray(342))