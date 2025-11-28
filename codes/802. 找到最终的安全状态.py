from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        color=[0]*n

        def dfs(v:int):
            if color[v]>0:
                return color[v]==2

            color[v]=1

            for u in graph[v]:
                if not dfs(u):
                    return False


            color[v]=2
            return True



        return [ i for i in range(n) if dfs(i)]

