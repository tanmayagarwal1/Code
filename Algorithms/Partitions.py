def NumPartitions(O, P):
	# O = Number of objects, P = number of maximum divisions in a partition 
	if P == 1:
		return 1 
	elif P == 0 or O < 0:
		return 0 
	else:
		return NumPartitions(O, P - 1) + NumPartitions(O - P, P)

print(NumPartitions(20, 4))


