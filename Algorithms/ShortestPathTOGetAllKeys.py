def ShortestPathToGetAllKeys(grid):
	m, n = len(grid), len(grid[0])
	if m == 0 or n == 0 : raise ValueError 
	q = []
	key_count = 0 
	for i in range(m):
		for j in range(n):
			if grid[i][j] == '@':
				start = (i, j)
			elif grid[i][j] in 'abcdef':
				key_count += 1
	i, j = start
	q.append((i, j, ''))
	step = 0
	seen = set() 
	while q:
		step += 1 
		for _ in range(len(q)):
			i, j, key = q.pop(0)
			if (i, j, key) in seen : continue 
			if len(key) == key_count : return step - 1 # We do a -1 as the step should be incremented after the bfs call, but as we do it before : we use a -1
			seen.add((i, j, key))
			neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
			for dx, dy in neighbours:
				x = i + dx 
				y = j + dy 
				if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '#':
					continue 

				val = grid[x][y] # Now val can either be an empty cell (.) or a key (lower case letter) or a lock (Upper case letter)
				# We need to set all the cases for each possible value of val 

				if val in 'ABCDEF' and val.lower() in key: # If we are on a lock and we also have its corresponding key 
					q.append((x, y, key))

				elif val in '.@': # We are on an empty cell or the start point itself ( start point is arbitrary and hence there is a chance we visit it again during BFS )
					q.append((x, y, key))

				elif val in 'abcdef': # We are on a key 
					if val not in key:
						q.append((x, y, key + val))
					else:
						q.append((x, y, val))
	return - 1


#grid = ["@.a.#","###.#","b.A.B"]
grid = ["@fedcbBCDEFaA"]
print(ShortestPathToGetAllKeys(grid))