def ExpressiveWords(sti, words):
	if not sti : raise ValueError 
	def Helper(sti, word):
		i, j, dx, dy = 0, 0, 0, 0 
		m, n = len(sti), len(word)
		while i < m and j < n :
			if sti[i] != word[j] : return False 
			while dx < m and sti[i] == sti[dx] : dx += 1 
			while dy < n and word[j] == word[dy] : dy += 1 
			if dx - i != dy - j and dx - i < max(3, dy - j) : return False 
			i, j = dx, dy 
		return i == m and j == n # The pointers must reach the end of both strings 

	return sum([Helper(sti, word) for word in words])

s = "zzzzzyyyyy"
words = ["zzyy","zy","zyy"]
s1 = 'abcd'
words2 = ['abc']
print(ExpressiveWords(s1, words2))