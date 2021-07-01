def PartitionLabels(sti):
	if len(sti) == 0 : raise ValueError 
	ends = {c : i for i, c in enumerate(sti)}
	start = 0 
	out = [0]
	string = []
	while start < len(sti):
		end = ends[sti[start]]
		res = ''
		while start <= end:
			symb = sti[start]
			res += symb # For the string itself 
			end = max(end, ends[symb])
			start += 1
		string.append(res)
		out.append(start)
	return [out[i] - out[i - 1] for i in range(1, len(out))], string  # Out => for lengths 

sti = "ababcbacadefegdehijhklij"
print(PartitionLabels(sti))