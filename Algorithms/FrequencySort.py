def FrequencySort(sti):
	dic = {}
	for i in sti:
		if i not in dic.keys():
			dic[i] = 1
		else:
			dic[i] += 1
	q = [i for i in dic.values()]
	q.sort()
	q = q[::-1]
	results = []
	for i in q:
		for j, k in dic.items():
			if i == k:
				results.append(i*j)
				break 
		del dic[j]
	return ''.join(results)

print(FrequencySort("Aabb"))