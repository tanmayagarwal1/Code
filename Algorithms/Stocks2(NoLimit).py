# No transaction Limit 
def Stock2(arr):
	return sum([tomorrow - today for today, tomorrow in zip(arr, arr[1:]) if tomorrow - today > 0])

def Stock2Readable(arr):
	# Basically we need to find the profit in as many transactions as we want. So we just have to some up positive differeces betweem tomorrow and today
	res = [0] # Initialise to zero in case nothing gets adder to the array. Not necessary to do this 
	for today, tomorrow in zip(arr, arr[1:]):
		if tomorrow - today > 0:
			res.append(tomorrow - today)
	return sum(res)

arr = [7,1,5,3,6,4]
print(Stock2(arr))