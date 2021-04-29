'''
GOOGLE CODING INTERVIEW : FIND A SUITABLE APARTMENT

In this problem we are given a list of dictionaries and an array which contains the places 
of interests to us. Each new dictionary represents a block for a place which have gyms,schools
etc etc. Now we need tp write a code to find out which block is best suitated for us to buy a 
house in given our interests. 

SOLUTION: 

We first define a fucntion which takes the array of dics and the interests as input. 
Now we initilise a queue with 0's to the length of the array. each index in our queue 
is an analogie to a block. Now we define count to use as an index into the queue. Initially
looping over the array gives us dictionaries. Hence 'i' is a dictionary. Now for every key
and value in that dictionaries, We check whether they match our interests, and if they do 
we also check whether that paticlar value is True. If Yes, we increment the value at that block's
index in the queue(which is accessed using count). Finally count is incremented, Specifying 
that we are moving to the next bloack and finally the INDEX of max element of queue is returned.
Index specifies the block number and hence index is returned. (We add 1 to the index so that 
its more human redable)

'''

# RAW FIRST RUN 
def BlocksRaw(arr,interests):
	size=0 
	for i in arr:
		size+=1
	reward=[0]*size
	count=0 
	for i in arr:
		for j in i:
			if j==interests[0] and i[interests[0]]==True or j==interests[1] and i[interests[1]]==True:
				reward[count]+=1
		count+=1
	ans=0 
	for i in range(len(reward)):
		ans=max(ans,reward[i])
	return reward.index(ans)

def Blocks(arr,interests):
	size=0 
	for i in arr:
		size+=1
	reward=[0]*size
	count=0 
	for i in arr:
		for j,k in i.items():
			for interest in range(len(interests)):
				if j==interests[interest] and k==True:
					reward[count]+=1
		count+=1
	ans=0 
	for i in range(len(reward)):
		ans=max(ans,reward[i])
	return (reward.index(ans))+1


arr=[{'gym':False,'school':True,'store':False},  \
	 {'gym':True,'school':False,'store':False},  \
     {'gym':True,'school':True,'store':False},   \
     {'gym':False,'school':True,'store':False},  \
     {'gym':False,'school':True,'store':True},]


interests=['gym','store']
print(Blocks(arr,interests))




