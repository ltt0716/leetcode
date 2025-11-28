from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        linksheet=[[] for i in range(n)]

        exits=False
        def dfs(node):
            nonlocal exits
            visited[node] = True
            for neighbor in linksheet[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

            if node == destination:
                # print(node, destination, node == destination)
                exits=True


        for list in edges:
            v1=list[0]
            v2=list[1]

            linksheet[v1].append(v2)
            linksheet[v2].append(v1)
        # print(linksheet)

        visited = [False]*n
        dfs(source)
        return  exits


edges=[[0,1],[1,2],[2,0]]
n=3
source=0
destination=2

print(Solution().validPath(n,edges,source,destination))



