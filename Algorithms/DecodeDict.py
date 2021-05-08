def Decode(sti,order):
	d=dict()
	count=0 
	flag=0
	for i in order:
		d[i]=count
		count+=1
	for i in range(len(sti)-1):
		for j in range(len(sti[i])):
			if d[sti[i][j]]==d[sti[i+1][j]]:
				continue 
			if d[sti[i][j]]<d[sti[i+1][j]]:
				break
			if d[sti[i][j]]>d[sti[i+1][j]]:
				flag=1 
	return True if flag==0 else False



sti=['word','world']
order='hlabcdefgijkmnopqrstuvwxyz'
print(Decode(sti,order))
