from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n

        adj=[[] for _ in range(n)]

        for neighbor in edges:
            a,b=neighbor[0],neighbor[1]
            adj[a].append(b)
            adj[b].append(a)


        vnums=enums=0
        def dfs(v):
            nonlocal vnums,enums
            vnums=vnums+1
            enums += len(adj[v])

            visited[v] = True

            for i in adj[v]:
                if not visited[i]:

                    dfs(i)


        ans=0

        for i in range(n):
            vnums = enums = 0
            if not visited[i]:
                dfs(i)
            if vnums!=0 and vnums*(vnums-1)==enums:
                ans+=1


        return ans


n =6
edges =[[0,1],[0,2],[1,2],[3,4]]

print(Solution().countCompleteComponents(n,edges))