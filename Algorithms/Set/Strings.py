# Eveery string problem ever 

def OneSwap(sti):
	if len(sti) == 0 : raise ValueError 
	i, j = 0, len(sti) - 1
	while j > i :
		if sti[i] == sti[j]:
			i += 1
			j -= 1
		else:
			one, two = sti[i:j], sti[i + 1:j + 1]
			return one == one[::-1] or two == two[::-1]
	return True

def MinSwap(sti):
	if len(sti) == 0 or not IsValid(sti):
		raise ValueError
	i, j, swaps = 0, len(sti) - 1, 0 
	sti = [i for i in sti]
	while j > i:
		if sti[i] == sti[j]:
			i += 1 
			j -= 1
		else:
			tmp = j 
			while tmp >= i and sti[tmp] != sti[i]:
				tmp -= 1
			if tmp == i :
				sti[tmp], sti[tmp + 1] = sti[tmp + 1], sti[i]
				swaps += 1 
				continue 
			for x in range(tmp, j):
				sti[x], sti[x + 1] = sti[x + 1], sti[x]
				swaps += 1
			i += 1
			j -= 1
	return swaps 

def IsValid(sti):
	d = {}
	for char in sti:
		d[char] = d.get(char, 0) + 1
	return len([i for i, j in d.items() if j & 1]) <= 1 

def FrequencySort(sti):
	if len(sti) == 0 :
		return - 1
	d = dict()
	for char in sti:
		d[char] = d.get(char, 0) + 1
	q = [i for i in d.values()]
	q.sort()
	sol = ''
	q = q[::-1]
	for freq in q:
		for char, freqq in d.items():
			if freqq == freq:
				sol += char * freq
				break 
		del d[char]
	return sol 

def AnagramGroups(arr):
	if len(arr) == 0 :
		return -1 
	d = {}
	for word in arr:
		tmp = ''.join(sorted(word))
		if tmp in d:
			d[tmp].append(word)
		else:
			d[tmp] = [word]
	return [i for i in d.values()]

def License(sti, k):
	if len(sti) == 0 : return -1 
	sti = ''.join(sti.split('-')).upper()
	i, j, res = 0, len(sti), []
	while j > i:
		if sti[j - k : j] : res.append(sti[j - k : j])
		else : res.append(sti[:j])
		j -= k 
	return '-'.join(res[::-1])

def UniqueLengthMax(arr):
	if len(arr) == 0:
		raise ValueError
	sol, res = [''], 0 
	for word in arr:
		for string in sol:
			tmp = word + string 
			if len(tmp) == len(set(tmp)):
				sol.append(tmp)
				res = max(res, len(tmp))
	return res 

def MaxDeletions(sti):
	if len(sti) == 0 :
		raise ValueError
	d = dict()
	for char in sti:
		d[char] = d.get(char, 0) + 1
	s, swaps = set(), 0
	for i in d.values():
		while i >= 0 and i not in s:
			i -= 1
			swaps += 1
		s.add(i)
	return swaps 

def StartingWith(arr, pattern):
	if len(arr) == 0 : raise ValueError
	q = []
	for word in arr:
		count = 0 
		for j in range(len(pattern)):
			if word[j] == pattern[j]:
				count += 1
			else:
				break 
			if count == len(pattern):
				q.append(word)
	return q 

def Blocks(arr, interest):
	if len(arr) == 0 : raise ValueError
	q = []
	for i in arr:
		count = 0 
		for j, k in i.items():
			for z in range(len(interest)):
				if j == interest[z] and k == True:
					count += 1
		q.append(count)
	res = q[0]
	for i in range(len(q)):
		res = max(res, q[i])
	return q.index(res) + 1

def Lcs(x, y):
	if len(x) == 0 or len(y) == 0 : raise ValueError
	m, n = len(x), len(y)
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	for i in range(1, m + 1):
	 for j in range(1, n + 1):
	 	if x[i - 1] == y[j - 1]:
	 		dp[i][j] = dp[i - 1][j - 1] + 1
	 	else:
	 		dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
	return dp[m][n]

def LongestPalindromicSub(sti):
	if len(sti) == 0 : raise ValueError
	return Lcs(sti, sti[::-1])

def LongestIncresingSubsequence(sti):
	if len(sti) == 0 : raise ValueError
	sti.sort()
	q = []
	for char in sti:
		if char not in q:
			q.append(char)
		else:
			continue
	q = ''.join(q)
	return Lcs(sti, q)

def regularexpression(sti, pattern):
	m, n = len(sti), len(pattern)
	if m == 0 or n == 0 : return -1 
	dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
	dp[0][0] = True 
	for i in range(1, n + 1):
		if pattern[i - 1] == '*':
			dp[0][i] = dp[0][i - 2]
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if sti[i - 1] == pattern[j - 1] or pattern[j - 1] == '*':
				dp[i][j] = dp[i - 1][j - 1]
			elif pattern[j - 1] == '*':
				dp[i][j] = dp[i][j - 2]
				if pattern[j - 2]== '.' or sti[i - 1] == pattern[j - 2]:
					dp[i][j] = dp[i - 1][j]
	return dp[m][n]

def SubStrings(sti):
	if len(sti) == 0 : raise ValueError
	res = []
	for i in range(len(sti)):
		for j in range(i + 1, len(sti) + 1):
			res.append(sti[i : j])
	return set(sorted(res))

def HtmlParser(sti):
	if len(sti) == 0 : raise ValueError
	d = {"&quot;":'"',"&apos;":"'","&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
	keywords, outputs, Mode = [], [], False
	for char in sti:
		if char == '&':
			keywords.append(char)
			Mode = True 
		elif Mode:
			keywords.append(char)
			if char == ';':
				keywords = ''.join(keywords)
				outputs.append(d.get(keywords,keywords))
				keywords = []
				Mode = False 
		else:
			outputs.append(char)
	if Mode:
		outputs.append(keywords)
	return ''.join(outputs)

def WordBreak(sti, words):
	if len(sti) == 0 :
		raise ValueError
	dp = [True] + [False for _ in range(len(sti))]
	for i in range(1, len(sti) + 1):
		for word in words:
			if sti[:i].endswith(word):
				dp[i] = dp[i] or dp[i - len(word)]
	return dp[len(sti)]

def Specialrev(sti):
	if len(sti) == 0 : raise ValueError
	j = 0 
	sti = [i for i in sti]
	for i in range(len(sti) - 1, len(sti)//2, - 1):
		if sti[i].isalpha():
			while j < i:
				if sti[j].isalpha():
					sti[i], sti[j] = sti[j], sti[i]
					j += 1 
					break 
				else:
					j += 1
	return ''.join(sti)

def HtmlValidator(sti):
	if len(sti) == 0 : raise ValueError
	start, end, open_br, i = [], [], ['<', '>', '/'], 0 
	while i < len(sti):
		if sti[i] == open_br[0] and sti[i + 1] != open_br[2]:
			while sti[i] != open_br[1]:
				start.append(sti[i])
				i += 1
		elif sti[i] == open_br[0] and sti[i + 1] == open_br[2]:
			while sti[i] != open_br[1]:
				if sti[i] == open_br[2]:
					i += 1
					continue 
				end.append(sti[i])
				i += 1
		else:
			i += 1
	return sorted(start) == sorted(end)


try :
	# Anagram Groups 
	print(AnagramGroups(["eat","tea","tan","ate","nat","bat"])) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

	# String Starting With 
	print(StartingWith(['tanmay','shivika','tanuuuu'],'tan')) # ['tanmay', 'tanuuuu']

	# License Plate 
	print(License("3R-34213-3213D", 5)) # 3R-34213-3213D

	# One swap palindrome 
	print(OneSwap('abc')) # False 

	# Min Swap Palindrome 
	print(MinSwap('ntiin')) # 1 

	# Unique Length Max 
	arr = ["cha","r","act","ers"]  
	print(UniqueLengthMax(arr)) # 6 

	# Frequency Sort 
	print(FrequencySort("Aabb")) # bbAa

	# Max deletions
	print(MaxDeletions("hogdheejnglfmaidocafjngkf")) # 39

	#BLOCKS 
	arr=[{'gym':False,'school':True,'store':False},  \
	   {'gym':True,'school':False,'store':False},  \
	     {'gym':True,'school':True,'store':False},   \
	     {'gym':False,'school':True,'store':False},  \
	     {'gym':False,'school':True,'store':True},]
	interests=['gym','store']
	print(Blocks(arr,interests)) # 2

	#REGULAR EXPRESSION 
	print(regularexpression("c","a*c")) # True

	# LCS
	print(Lcs('tanmay','shivika')) # 1 

	# Lonest Palindromic Subsequence 
	print(LongestPalindromicSub('agbcba')) # 5 

	# Unique Substrings
	print(SubStrings('abcd')) # {'a', 'c', 'b', 'abcd', 'bc', 'cd', 'bcd', 'd', 'abc', 'ab'}

	# Html Parser
	text = "&amp; is an HTML entity but &ambassador; is not."
	text_2 = "x &gt; y &amp;&amp; x &lt; y is always false"
	print(HtmlParser(text))   # & is an HTML entity but &ambassador; is not.
	print(HtmlParser(text_2)) # x > y && x < y is always false

	# Word Break 
	s = "applepenapple"
	wordDict = ["apple","pen"]
	print(WordBreak(s, wordDict)) # True 

	# Html Validator 
	print(HtmlValidator("<head><head> This is a Html headline </head></head>")) # True
	
	# Special Reverse
	print(Specialrev('abc&^def')) # fed&^cba

except ValueError:
	print("exception caught")



