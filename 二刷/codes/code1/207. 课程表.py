from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color=[0]*numCourses
        adj=[[]for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)


        def dfs(i):
            color[i]=1

            for u in adj[i]:
                if color[u]==1 or(color[u]==0 and dfs(u)):
                    return True

            color[i]=2
            return False

        for index,val in enumerate(color):
            if val==0 and dfs(index):
                return False

        return True

