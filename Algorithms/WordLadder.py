def wordLadder(start, end, words):
	if not start or not end or not words : raise ValueError 

	def Construct(words):
		d = {}
		for word in words:
			for i in range(len(word)):
				s = word[:i] + '*' + word[i + 1:]
				d[s] = d.get(s, []) + [word]
		return d 

	def Helper(start, end, words):
		# In this word is the modified dict 
		q = [(start, 1)] # word and step tuple 
		visited = set()
		while q:
			word, steps = q.pop(0)
			if word not in visited : visited.add(word)
			if word == end : return steps 
			for i in range(len(word)):
				s = word[:i] + '*' + word[i + 1:]
				neighbouring_words = d.get(s, [])
				for neighbour in neighbouring_words:
					if neighbour not in visited:
						q.append((neighbour, steps + 1))
		return 0 

	d = Construct(words)
	return Helper(start, end, d)

start = 'hit'
end = 'cog'
words = ["hot","dot","dog","lot","log","cog"]
print(wordLadder(start, end, words))