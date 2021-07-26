def FindNumbers(num):
	if not num : raise ValueError 
	s = bin(num + 1)[2:]
	dp = [1, 2] + [0] * (len(s) - 2) 
	for i in range(2, len(s)):
		dp[i] = dp[i - 1] + dp[i - 2]

	ans = 0 
	flag = 0 
	for i in range(len(s)):
		if s[i] == '0' : continue 
		if flag == 1 : break 
		if i and s[i - 1] == '1': flag = 1
		ans += dp[-i-1]
	return ans 

print(FindNumbers(1))
