def Sting(arr):
	num_logs, word_log = [], []
	for log in arr:
		nums = log.split(' ')[1]
		if nums.isnumeric():
			num_logs.append(log)
		else:
			word_log.append(log)
	word_log.sort(key = lambda x : (x.split(' ')[1:], x.split(' ')[0]))
	word_log.extend(num_logs)
	return word_log





arr = ['ykc 82 01', 'eo first qpx', '09z cat ham', '06f 12 25 6', 'az0 first qpx', '236 cat dog rabbit']
print(Sting(arr))