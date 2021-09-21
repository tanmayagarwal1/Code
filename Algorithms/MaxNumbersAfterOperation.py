def MinOpsIncrement(m, n, ops):
	if not m or not n : raise ValueError 
	if not ops : return m * n 
	return min(x[0] for x in ops) * min(y[1] for y in ops)

	


