def MinOperation(arr): #Uber 1 
	window, res = [0]*len(arr), 0
	dp = [0 for _ in range(max(arr) + 2)]
	for num in arr : dp[num] = 1
	for i in range(len(dp) - len(window) + 1):
		count = 0 
		for x in range(len(window)):
			if window[x] == 1: count += 1
		res = max(res, count)
		window.pop(0)
		if i + len(window) < len(dp):
			window.append(dp[i + len(window)])
	return len(arr) - res  

arr = [6, 4, 1, 7, 10]
print(MinOperation(arr))
