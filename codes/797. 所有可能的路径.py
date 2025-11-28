from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)

        paths=[]
        path=[]
        path.append(0)
        dfs(0,n-1,graph,path,paths)

        return paths






def dfs(node,destination,graph,path,paths):
    if node==destination:
        paths.append(path.copy())
    else:
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor,destination,graph,path,paths)
            path.pop()


graph =[[1,2],[3],[3],[]]

print(Solution().allPathsSourceTarget(graph))


