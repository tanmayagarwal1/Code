def CircularProblem(num):
	if not num : raise ValueError

	# 1. Find the largest power to the given num -> largest_pow => Helper()
	# 2. num = largest_pow + y where y = num - laregst_pow => Solver()
	# 3. result = 2 * y + 1 => main function call 

	def Helper(num):
		if not num : return 0 
		res = 0 
		for i in range(int(num**0.5)):
			tmp = 1<<i 
			if tmp > num:
				break 
			res = tmp
		return res 

	def Solver(num, _pow):
		return num - _pow 

	largest_pow = Helper(num)
	y = Solver(num, largest_pow)
	return 2 * y + 1