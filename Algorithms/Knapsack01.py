def Knapsack(wt, val, constraint):
	if not wt or not val : return - 1
	return KnapsackUtil(wt, val, constraint, len(wt))

def KnapsackUtil(wt, val, max_wt, n):
	if n == 0 or max_wt == 0 :
		return 0
	if wt[n - 1] <= max_wt:
		return max(val[n - 1] + KnapsackUtil(wt, val, max_wt - wt[n - 1], n - 1), KnapsackUtil(wt, val, max_wt, n - 1))
	elif wt[n - 1] >= max_wt :
		return KnapsackUtil(wt, val, max_wt, n - 1)

val = [350, 400, 450, 20, 70, 8, 5, 5]
wt  = [25, 35, 45, 5, 25 ,3, 2, 2]
w   = 104
print(Knapsack(wt, val, w))