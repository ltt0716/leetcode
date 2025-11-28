import collections
from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        g=[[] for _ in range(numCourses)]

        ispre=[[False]*numCourses for _ in range(numCourses)]
        for u,v in prerequisites:
            g[u].append(v)

        visited = [False]*numCourses
        def dfs(u):
            if visited[u]:
                return 
            visited[u] = True

            for v in g[u]:
                    dfs(v)
                    ispre[u][v] = True
                    for i in range(numCourses):
                        ispre[u][i] |= ispre[v][i]

        for i in range(numCourses):
            dfs(i)


        return [ispre[u][v] for u,v in queries]




