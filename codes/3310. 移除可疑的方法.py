from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj=[[]for _ in range(n)]

        for list in invocations:
            v1,v2=list[0],list[1]
            adj[v1].append(v2)


        bads=set()

        def dfs(v):
            bads.add(v)

            for i in adj[v]:
                if i not in bads:
                    dfs(i)

        good=True
        goods=set()

        def dfs2(v):
            nonlocal good
            goods.add(v)

            for i in adj[v]:
                if i not in bads:
                    if i not in goods:
                        dfs2(i)
                else:
                    good=False

        dfs(k)

        for i in range(n):
            if i not in bads and i not in goods:
                dfs2(i)


        if good==False:
            return [ i for i in range(n) ]

        else:
            return [ i for i in range(n) if i not in bads ]


n = 5
k = 0
invocations = [[1, 2], [0, 2], [0, 1], [3, 4]]
print(Solution().remainingMethods(n,k,invocations))
