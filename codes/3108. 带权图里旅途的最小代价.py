from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g=[[]for i in range(n)]

        for (u,v,w) in edges:
            g[u].append((v,w))
            g[v].append((u,w))

        def dfs(v:int):
            nonlocal g,connected_graph,visited,ands,index

            visited.add(v)
            connected_graph[v]=index

            for u,w in g[v]:
                ands[index]&=w
                if u not in visited:
                    dfs(u)


        connected_graph=[-1]*n
        ands=defaultdict(lambda:-1)
        visited = set()
        index=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                index+=1


        ans=[]
        for u,v in query:
            if connected_graph[v]==connected_graph[u]:
                ans.append(ands[connected_graph[v]])
            else:
                ans.append(-1)

        return ans

n =3
edges =[[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
query =[[1,2]]

# print(Solution().minimumCost(n,edges,query))