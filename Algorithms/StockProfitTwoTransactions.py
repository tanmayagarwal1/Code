def MaxProfit(arr):
	if len(arr) == 0 : return - 1
	profit = 0 
	for i in range(1, len(arr)):
		if arr[i] == arr[i - 1] : continue 
		curr_pro = arr[i] - arr[i - 1]
		if curr_pro > 0 : profit += curr_pro
	return profit 


arr = [7,6,4,3,1]
print(MaxProfit(arr))