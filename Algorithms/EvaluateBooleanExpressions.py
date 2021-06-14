def EvaluateExpression(sti):
	if len(sti) == 0 : return - 1
	return NumWays(sti, 0, len(sti) - 1, True)

def NumWays(sti, i, j, bool):
	if i > j : 
		return False 
	if i == j :
		if bool == True:
			return True
		elif bool == False:
			return False
	ans = 0
	for k in range(i + 1, j, 2):
		Left_True   = NumWays(sti, i, k - 1, True)
		Left_False  = NumWays(sti, i, k - 1, False)
		Right_True  = NumWays(sti, k + 1, j, True)
		Right_False = NumWays(sti, k + 1, j, False)
		if sti[k] == '&':
			if bool == True:
				ans = ans + Left_True*Right_True
			else:
				ans = ans + Left_True*Right_False + Right_True*Left_False + Right_False*Left_False

		elif sti[k] == '|':
			if bool == True:
				ans = ans + Left_False*Right_True + Left_True*Right_False + Left_True*Right_True
			else:
				ans = ans + Left_False*Right_False

		elif sti[k] == '^':
			if bool == True:
				ans = ans + Left_False*Right_True + Right_False*Left_True
			else:
				ans = ans + Left_True*Right_True + Left_False*Right_False

	return ans 

Exp = "T^F&T"
print(EvaluateExpression(Exp))