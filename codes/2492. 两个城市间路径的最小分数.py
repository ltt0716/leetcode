import math
from typing import List

class Graph:
    def __init__(self,n):
        self.adj=[[] for _ in range(n)]

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        G=Graph(n)
        visited=[False]*n
        for road in roads:
            a,b,dis=road[0],road[1],road[2]
            G.adj[a-1].append([b-1,dis])
            G.adj[b-1].append([a-1,dis])
        ans=math.inf

        # print(G.adj)
        def dfs(v):
            visited[v]=True
            for adj in G.adj[v]:
                if not visited[adj[0]]:
                    dfs(adj[0])

        dfs(0)

        for index,val in enumerate(visited):
            if val==True:
                for adj in G.adj[index]:
                    v,dis=adj[0],adj[1]
                    if visited[v]==True:
                        ans=min(ans,dis)

        return ans

roads =[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
n=4

print(Solution().minScore(n,roads))