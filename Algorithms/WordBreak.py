def WordBreak(sti, words):
	# sti = string 
	# words = dict of words 

	if len(sti) == 0:
		return -1 
	dp = [True] + [False for _ in range(len(sti))]
	for i in range(1, len(sti) + 1):
		for word in words:
			if sti[:i].endswith(word):
				dp[i] = dp[i] | dp[i - len(word)]
	return dp[-1]

s = "applepenapple"
wordDict = ["apple","pen"]
print(WordBreak(s, wordDict))