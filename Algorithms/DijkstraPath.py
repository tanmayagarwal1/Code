class graph:
	def __init__(self,v):
		self.v=v
		self.graph=[[0 for i in range(self.v)]for j in range(self.v)]
	def shortestPath(self,source):
		dist=[float("inf")]*self.v
		dist[source]=0 
		visited=[False]*self.v
		for i in range(self.v):
			u=self.smalldistance(dist,visited)
			visited[u]=True 
			for x in range(self.v):
				if self.graph[u][x]>0 and visited[x]==False and dist[x]>dist[u]+self.graph[u][x]:
					dist[x]=dist[u]+self.graph[u][x]
		self.printsol(dist)
	def smalldistance(self,dist,visited):
		min=float("inf")
		for i in range(self.v):
			if dist[i]<min and visited[i]==False:
				min=dist[i]
				min_index=i 
		return min_index
	def printsol(self,dist):
		for i in range(self.v):
			print(f"{i} : {dist[i]}")

g = graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]
g.shortestPath(0)