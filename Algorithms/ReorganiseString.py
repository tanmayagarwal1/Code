def ReorganizeString(sti):
	if len(sti) == 0 : raise ValueError 
	d = {}
	for char in sti:
		d[char] = d.get(char, 0) + 1
	pq = []
	for char, val in d.items():
		heapq.heappush(pq, (-val, char))
	res = ''
	while len(pq) > 1:
		x = heapq.heappop(pq)
		y = heapq.heappop(pq)
		res += x[1]
		res += y[1]
		if x[0] < -1:
			heapq.heappush(pq,(x[0] + 1, x[1]))
		if y[0] < -1:
			heapq.heappush(pq, (y[0] + 1, y[1]))
	if pq:
		if pq[0][0] <-1:
			return False 
		res += pq[0][1]
	return res 

sti = 'aaab'
print(ReorganizeString(sti))