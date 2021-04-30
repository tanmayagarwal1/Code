'''

In This algorithm we are given an array of strings and we need to find which of the strings 
in the array match the other given seperate string. To to this we loop over the array using
'i' which gives us access to individual strings and then we loop over the length of the other 
string using j. We say that if i[j]==sti[j](If the two match) then increment a count. Else,
We break because we want the words to match in order(The first letter of the string in the array
must match the first letter of our explicit string). Then incide the second loop itself we check, 
if count==len(sti), which means all starting elements match, we append the array string in a queue
and finally return the queue

'''


def Startingwith(arr,sti):
	n=len(sti)
	q=[]
	for i in arr:
		count=0 
		for j in range(len(sti)):
			if i[j]==sti[j]:
				count+=1
			else:
				break 
			if count==len(sti):
				q.append(i)
	if q==[]:
		return 0 
	return q 

print(Startingwith(['tanmay','shivika','tanuuuu'],'tan'))
