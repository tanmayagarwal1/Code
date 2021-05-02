'''

LEETCODE HARDEST PROBLEM 
VALID NUMBER 
ACCEPTANCE RATE : 16.1% 
MY SOLUTION FASTER THAN 92.26% SUBMISSIONS
'''

def IsValid(sti):
	n=len(sti)
	flag=0 
	count=0
	if n==1 and sti=='.':
		return False 
	for i in range(n):
		if sti[i]=='.':
			count+=1
		if count>=2:
			return False
	for i in range(n):
		if sti[i].isnumeric():
			continue 
		elif sti[i]=='e' or sti[i]=='E':
			flag=1
			count=0 
			counte=0
			if flag==1:
				for j in range(i,len(sti)):
					if sti[j]=='.':
						return False 
				for k in range(i,-1,-1):
					if sti[k].isnumeric():
						count+=1
				if count==0:
					return False 
				for z in range(i+1,len(sti)):
					if sti[z]=='e':
						counte+=1
				if counte != 0:
					return False 
			if i+1<n:
				if sti[i+1].isnumeric():
					continue
				else:
					if sti[i+1]=='+' or sti[i+1]=='-':
						if i+2<n and (sti[i+2].isnumeric()):
							continue
		elif sti[i]=='.':
			if i+1<n and (sti[i+1]=='+' or sti[i+1]=='-'):
				return False 
			else:
				continue
		elif sti[i]=='+' or sti[i]=='-':
			if i-1<n and i-1>=0:
				if sti[i-1].isnumeric():
					return False 
			if i+1<n:
				if (sti[i+1].isnumeric()):
					continue
				else:
					if (sti[i+1]=='.'):
						if i+2<n and sti[i+2].isnumeric():
							continue
		return False 
	return True 

def test(sti,f):
	correct=[]	
	invalid=[]
	for i in sti:
		correct.append(IsValid(i))
	for i in f:
		invalid.append(IsValid(i))
	print(correct)
	print()
	print(invalid)



sti=["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", \
	 "+6e-1", "53.5e93", "-123.456e789"]

f=["abc", "1a", "1e", ".e3", "99e2.5", "--6", "-+3", \
   "95a54e53",'.','..','..2','9+5','+.','.-4','92e1740e91','e']

test(sti,f)

