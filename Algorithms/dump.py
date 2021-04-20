from collections import defaultdict
def ini(self,v):
	self.graph=defaultdict(list)
	self.v=v
def append(self,s,d):
	self.graph[s].append(d)
def maxpath(self,v,d):
	visited=[False]*(self.v)
	q=[]
	self.maxpathu(v,d,q,visited)	
def maxpathu(self,v,d,q,visited):
	visited[v]=True 
	q.append(v)
	if v==d:
		print(q) 
	else:
		for i in self.graph[v]:
			if visited[i]==False:
				self.maxpathu(i,d,q,visited)
	q.pop()
	visited[v]=False
graph=type('graph',(),{'__init__':ini,'append':append,'maxpath':maxpath,'maxpathu':maxpathu})
g = graph(4)
g.append(0, 1)
g.append(0, 2)
g.append(0, 3)
g.append(2, 0)
g.append(2, 1)
g.append(1, 3)
print(g.maxpath(2,3))


