from typing import List
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[]for i in range(n)]
        k-=1
        dis=[math.inf]*n
        dis[k]=0
        for u,v,w in times:
            graph[u-1].append((v-1,w))
            if u-1==k:
                dis[v-1]=w

        visited = [False for i in range(n)]

        for i in range(n):
            u=-1
            for j in range(n):
                if not  visited[j] and (u==-1 or dis[u]>dis[j]):
                    u=j
                    # print(u)
            if dis[u]==math.inf:
                break

            visited[u]=True
            for v,w in graph[u]:
                if dis[v]>dis[u]+w:
                    dis[v]=dis[u]+w

        # print(dis)

        return max(dis) if max(dis)!=math.inf else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))