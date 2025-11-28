from typing import List

class Graph:
    def __init__(self,n):
        self.n=n
        self.adj=[[ ]for _ in range(n)]

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        G=Graph(n)

        if n-1>len(connections):
            return -1

        for list in connections:
            v1,v2=list[0],list[1]
            G.adj[v1].append(v2)
            G.adj[v2].append(v1)


        visited=[False]*n

        def dfs(v):
            visited[v]=True
            for adj in G.adj[v]:
                if not visited[adj]:
                    dfs(adj)

        count=0

        for  i in range(n):
            if not visited[i]:
                dfs(i)
                count+=1

        return count-1


