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
		ans = []
		visited = set([start]) 
		q = [(start, [start])]
		while q and not ans:
			lcl_visited = set()
			for _ in range(len(q)):
				word, path = q.pop(0)
				for i in range(len(start)):
					s = word[:i] + '*' + word[i + 1:]
					neighbours = d.get(s, [])
					for neighbour in neighbours:
						if neighbour == end:
							ans.append(path + [end])
						if neighbour not in visited:
							lcl_visited.add(neighbour)
							q.append((neighbour, path + [neighbour]))
			visited = visited.union(lcl_visited)
		return ans 

			

	d = Construct(words)
	return Helper(start, end, words)


start = 'hit'
end = 'cog'
words = ["hot","dot","dog","lot","log","cog"]
print(wordLadder(start, end, words))
