def MinAddsToMakeBalanceParanthesis(sti):
	if len(sti) == 0 : raise ValueError
	Insert_closed, Insert_open = 0, 0 # Insert_closed is the driver (usually) as many strings start with an open brace 
	for char in sti:
		if char == '(':
			Insert_closed += 1
		elif Insert_closed == 0 and char == ')':
			Insert_open += 1

		else:
			Insert_closed -= 1
	return Insert_open + Insert_closed

sti = '()))(('
print(MinAddsToMakeBalanceParanthesis(sti)) # 4 