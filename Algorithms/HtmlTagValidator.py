def HtmlTagValidator(sti):
	br = ['<', '>', '/']
	Start, i = [], 0
	Ends = []
	while i < len(sti): 
		if sti[i] == br[0] and sti[i+1] != br[2]:
			while sti[i] != br[1]:
				Start.append(sti[i])
				i += 1
		elif sti[i] == br[0] and sti[i+1] == br[2]:
			while sti[i] != br[1]:
				if sti[i] == br[2]:
					i += 1
					continue  
				Ends.append(sti[i])
				i += 1
		else:
			i += 1
	return sorted(Ends) ==  sorted(Start) 

print(HtmlTagValidator("<head><head> This is a Html headline </head></head>"))
