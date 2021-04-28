'''
GOOGLE KICKSTART HOUSE BUYING PROBLEM :

In this problem we are given an array and a budget. The array contains listing of the houses.
Now we need to output how many total number of houses can be bought based on our curent budget.

AUTHOR: 

TANMAY AGARWAL @code repo 

SOLUTION :

we initialise an empty queue in the beginning. Then we start our i index from the last to go 
all the way to the first(Can be done from first to last too). We check whether the current value
at i exceeds our budget or not. If yes, we skip this value of i and move on to the next one.
If no, we declare an initial variable which is nothing but the initial value of the house we 
bought. Now we also start count=1 beacsue we have bought the house that i currently recides on. 
Now we start j from 0 all the way through to the end. If i==j, we just skip that value of j. 
Now if the value of initial+arr[j]<budget, new initial value will be initial+arr[j] and count 
will be incremented(as we have now procured this house). we continue this loop. Now when we come
out of the j loop we append the count value to q. This will be done for all the count values in 
i loop. This is done so that we know how many houses can be bought when we start from different i 
values. In the end we take the maximum element from q and display it. If q is empty that means 
that we cannot buy any house, and we return 0 

'''


def houses(arr,budget):
	n=len(arr)
	q=[]
	for i in range(n-1,-1,-1):
		if arr[i]>budget:
			continue 
		initial=arr[i]
		count=1
		for j in range(n):
			if j==i:
				continue 
			if initial+arr[j]<=budget:
				initial=initial+arr[j]
				count +=1
		q.append(count)
	if not q:
		return 0 
	res=q[0]
	for i in range(len(q)):
		res=max(res,q[i])
	return res 


print(houses([20,90,40,90],100))

		 
