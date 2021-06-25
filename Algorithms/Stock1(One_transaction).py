def Stocks1(arr):
	if not arr : raise ValueError 
	max_profit, min_price = 0, float('inf')
	for price in arr:
		min_price = min(min_price, price) # minimum betwee current price and price 
		profit = price - min_price # Calcuate local profit 
		max_profit = max(max_profit, profit)
	return max_profit 

arr = [7,1,5,3,6,4]
print(Stocks1(arr))