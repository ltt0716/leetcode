import heapq
import math
from typing import List


class State:
    def __init__(self,y,dist):
        self.y = y
        self.dist = dist
    def __lt__(self, other):
        return self.dist < other.dist

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g=[{} for _ in range(n)]

        for u,v,d in edges:
            if v in g[u].keys():
                if d < g[u][v]:
                    g[u][v] = d
            else:
                g[u][v] = d

            if u in g[v].keys():
                if d < g[v][u]:
                    g[v][u] = d
            else:
                g[v][u] = d

        dist=[math.inf for _ in range(n)]
        dist[0]=0

        q=[]

        heapq.heappush(q, State(0,0))

        while  q:
            s=heapq.heappop(q)

            y,d=s.y,s.dist

            if dist[y]<d:
                continue

            for dy in g[y].keys():
                dd=g[y][dy]

                dis=dist[y]+dd

                if dis<disappear[dy]:
                    if dis<dist[dy]:
                        dist[dy]=dis
                        heapq.heappush(q,State(dy,dis))


        return [i if i !=math.inf else -1 for i in dist]

n = 2
edges = [[0,1,1]]
disappear = [1,1]
print(Solution().minimumTime(n, edges, disappear))