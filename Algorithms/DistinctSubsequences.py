def DistinctSubsequences(sti, pattern): # Make the pattern as the column for ease 
	m, n = len(sti), len(pattern)
	if m == 0 or n == 0 : raise ValueError 
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	for i in range(len(dp[0])):
		dp[0][i] = 1 
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if sti[i - 1] == pattern[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
			else:
				dp[i][j] = dp[i][j - 1]
	return dp[m][n]

sti = 'bag'
pattern = 'babgbag'
print(DistinctSubsequences(sti, pattern))

# Here the relation is if there is a match the current cell value will be equal to previous cell value + diagonal cell value 
# Else it will be the diagonal cell value ony 
# If ever we get stck please refer : https://leetcode.com/problems/distinct-subsequences/discuss/572192/Understand-DP-through-question-115-explanation-with-pictures