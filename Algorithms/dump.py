from collections import defaultdict 
class graph:
	def __init__(self):
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
					visited[i]=True 
	def dfs(self,v):
		s=set()
		self.dfsu(s,v)
	def dfsu(self,s,v):
		s.add(v)
		print(v)
		for i in self.graph[v]:
			if i not in s:
				self.dfsu(s,i)

g=graph()
g.append(0,1)
g.append(1,2)
g.append(1,3)
g.append(3,4)
g.append(4,4)
g.bfs(0)