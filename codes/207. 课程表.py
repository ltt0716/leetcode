from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses

        adj=[[] for _ in range(n)]

        for (v,u) in prerequisites:
            adj[v].append(u)

        visited=set()
        color=[0]*n

        def dfs(v:int):
            visited.add(v)
            color[v]=1
            for u in adj[v]:
                if u not in visited:
                    if dfs(u):
                        return True
                elif color[u]==1:
                    return True

            color[v]=2
            return False



        for i in range(n):
            if i not in visited:
                if dfs(i):
                    return False

        return True