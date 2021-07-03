def PhoneCombinations(digits):
	def Helper(d, digits, path, res):
		if not digits:
			res.append(path)
			return 
		for char in d[digits[0]]:
			Helper(d, digits[1:], path + char, res)

	if not digits : raise ValueError 
	d = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
	res = []
	Helper(d, digits, '', res)
	return res 

digits = '23'
print(PhoneCombinations(digits))
