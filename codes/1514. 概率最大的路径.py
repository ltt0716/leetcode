import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
         graph=[[] for i in range(n)]

         for (u,v),w in zip(edges,succProb):
             graph[u].append((v,w))
             graph[v].append((u,w))

         dist=[-1]*n

         q=[]
         dist[start_node]=1

         heapq.heappush(q,(-1,start_node))

         while q:
             w,u=heapq.heappop(q)

             if (-w)<dist[u]:
                 continue

             for v,k in graph[u]:
                 d=dist[u]*k
                 if dist[v]<d:
                     dist[v]=d
                     heapq.heappush(q,(-d,v))

         return dist[end_node] if dist[end_node]>0 else 0
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
print(Solution().maxProbability(n, edges, succProb, start, end))