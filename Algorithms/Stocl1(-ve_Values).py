# Maxium Profit in one transaction give negative values too

def Stocks1(arr):
	if len(arr) == 0 : raise ValueError 
	curr_max= 0
	global_max = 0 
	for k in range(1, len(arr)):
		curr_max= max(0, arr[k] - arr[k - 1])
		global_max = max(curr_max, global_max )
	return global_max 


arr = [7, 6, 4, 3, 1]
print(Stocks1(arr))