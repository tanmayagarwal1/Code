import heapq
def SortString(order, sti):
	if not sti : raise ValueError 
	d, res = {}, ''
	for idx, char in enumerate(order):
		d[char] = idx 
	pq = []
	for char in sti:
		heapq.heappush(pq, (d.get(char, float('inf')), char))
	while pq:
		_, tmp = heapq.heappop(pq)
		res += tmp 
	return res 

order = "cba"
sti = "abcd"
print(SortString(order, sti))