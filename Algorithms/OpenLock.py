def OpenLock(deadlocks, target, sti = '0000'):
	if not deadlocks or not sti : raise ValueError 
	deadset = set(deadlocks)
	if sti in deadset : return -1 
	q = [sti]
	steps = -1
	seen = set(sti)
	while q:
		steps += 1
		for _ in range(len(q)):
			curr = q.pop(0)
			if curr == target:
				return steps 
			if curr in deadset:
				continue 
			for i in range(4):
				digit = int(curr[i])
				for move in [-1, 1]:
					newdigit = (digit + move) % 10 
					new_combination = curr[:i] + str(newdigit) + curr[i + 1:]
					if new_combination not in seen:
						q.append(new_combination)
						seen.add(new_combination)
	return -1 

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(OpenLock(deadends, target))


