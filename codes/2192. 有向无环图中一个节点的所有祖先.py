from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans=[[] for i in range(n)]
        adj=[[] for i in range(n)]
        visited=[-1 for i in range(n)]

        for list in edges:

            a,b=list[0],list[1]

            adj[a].append(b)


        def dfs(v:int):

            visited[v]=i

            for u in adj[v]:
                if visited[u]!=i:
                    ans[u].append(i)
                    dfs(u)

        for i in range(n):
            dfs(i)


        return ans
n =5
edges =[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(Solution().getAncestors(n,edges))