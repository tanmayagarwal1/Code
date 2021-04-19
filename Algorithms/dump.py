def paranthesis(st):
	q=[]
	v={'(':')','{':'}','[':']'}
	open_br=set(['{','(','['])
	for i in st:
		if i in open_br:
			q.append(i)
		else:
			if i==v[q[-1]]:
				q.pop()
			else:
				return False
	return True 

print(paranthesis('{()}'))