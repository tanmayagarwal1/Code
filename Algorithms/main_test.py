def reve(arr):
	n=len(arr)
	j=0 
	i=n-1
	while i>n//2:
		if arr[i].isalpha():
			while j<i:
				if arr[j].isalpha():
					arr[i],arr[j]=arr[j],arr[i]
					j+=1
					i-=1
				else: 
					j+=1
	return arr
str="tan$$may"
print(reve(list(str)))