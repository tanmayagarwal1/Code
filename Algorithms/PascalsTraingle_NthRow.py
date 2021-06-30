def PascalTraingle(row):
	if not row : raise ValueError 
	my_row = [1]
	for _ in range(row):
		my_row = [x + y for x, y in zip([0] + my_row, my_row + [0])]
	return my_row

print(PascalTraingle(3))