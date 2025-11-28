import heapq
import math
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        graph=[[] for _ in range(n)]
        for u,v,w in edges:
            graph[u].append((v,w))
        self.graph=graph


    def addEdge(self, edge: List[int]) -> None:
        u,v,w = edge
        self.graph[u].append((v,w))

    def shortestPath(self, node1: int, node2: int) -> int:
        q=[]
        heapq.heappush(q,(0,node1))
        dist=[math.inf]*len(self.graph)
        dist[node1]=0
        while q:
            w,u = heapq.heappop(q)
            if w>dist[u]:
                continue

            for v,w in self.graph[u]:
                d=w+dist[u]
                if d<dist[v]:
                    dist[v]=d
                    heapq.heappush(q,(w,v))
        return dist[node2] if dist[node2]!=math.inf else -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)