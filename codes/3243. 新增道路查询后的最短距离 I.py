import math
from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            g[i].append(i + 1)

        dist = [math.inf] * n
        dist[0] = 0
        q = deque([0])
        while q:
            x = q.popleft()
            for y in g[x]:
                if dist[y] > dist[x] + 1:
                    dist[y] = dist[x] + 1
                    q.append(y)

        ans = []
        for u, v in queries:
            g[u].append(v)
            if dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                q = deque([v])
                while q:
                    x = q.popleft()
                    for y in g[x]:
                        if dist[y] > dist[x] + 1:
                            dist[y] = dist[x] + 1
                            q.append(y)
            ans.append(dist[n - 1])
        return ans