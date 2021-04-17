from collections import defaultdict
class graph: 
    def __init__(self):
        self.graph=defaultdict(list)
    def push(self,s,d):
        self.graph[s].append(d)
    def bfs(self,v):
        q=[]
        q.append(v)
        visited=[False]*(max(self.graph)+10)
        visited[v]=True
        while q:
            s=q.pop()
            print(s)
            for i in self.graph[s]:
                if visited[i]==False:
                    q.append(i)
                    visited[i]=True 
    def dfs(self,v):
        visited=set()
        self.dfsu(visited,v)
    def dfsu(self,visited,v):
        visited.add(v)
        print(v)
        for i in self.graph[v]:
            if i not in visited:
                self.dfsu(visited,i)
g=graph()
g.push(0,1)
g.push(1,2)
g.push(3,4)
g.push(2,4)
g.push(4,5)
g.push(4,6)
g.bfs(0)
