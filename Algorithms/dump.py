from collections import defaultdict
def ini(self):
	self.graph=defaultdict(list)
def append(self,s,d):
	self.graph[s].append(d)
def bfs(self,v):
	q=[]
	visited=[False]*100 
	visited[v]=True 
	q.append(v)
	while q:
		s=q.pop()
		print(s)
		for i in self.graph[s]:
			if visited[i]==False:
				q.append(i)
				visited[i]==True
 				
def dfs(self,v):
	s=set()
	self.dfsu(v,s)
def dfsu(self,v,s):
	s.add(v)
	print(v)
	for i in self.graph[v]:
		if i not in s:
			self.dfsu(i,s)
graph=type('graph',(),{"__init__":ini,'append':append,'bfs':bfs,'dfs':dfs,'dfsu':dfsu})
g=graph()
g.append(0,1)
g.append(1,2)
g.append(1,3)
g.append(4,5)
g.append(3,4)
g.bfs(0)
print()
g.dfs(0)
