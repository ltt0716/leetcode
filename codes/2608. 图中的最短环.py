import collections
import math
from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g=[[] for _ in range(n)]

        for u,v in edges:
            g[v].append(u)
            g[u].append(v)

        min_dis=math.inf

        for i in range(n):
            q=collections.deque([i])
            parent=[-1]*n
            dis=[None]*n
            dis[i]=0

            while q:
                u=q.popleft()
                for v in g[u]:
                    if dis[v] == None:
                        dis[v] = dis[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif v != parent[u]:
                         min_dis = min(min_dis, dis[v] + dis[u]+1)


        return min_dis if min_dis!=math.inf else -1






