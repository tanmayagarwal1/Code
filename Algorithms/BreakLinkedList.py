def BreakLinkedList(head, k):
	if not head : raise ValueError 
	curr, length = head, 0 
	while curr:
		length += 1
		curr = curr.next 

	chunk_size = length // k 
	large_chunks = length % k 
	res = [chunk_size + 1] * large_chunks + [chunk_size] * (k - large_chunks)
	prev, curr = None, head 
	for idx, num in enumerate(res):
		if prev:
			prev.next = None 
		res[idx] = curr 
		for _ in range(num):
			prev = curr 
			curr = curr.next 
	return res 


