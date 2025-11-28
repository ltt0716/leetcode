from collections import defaultdict
from itertools import groupby
from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knows = set([0, firstPerson])

        meets=defaultdict(list)

        for li in meetings:
            meets[li[2]].append((li[0], li[1]))

        meets=dict(sorted(meets.items()))

        def dfs(v:int):
            nonlocal visited,graph,knows
            visited.add(v)
            knows.add(v)
            for u in graph[v]:
                if u not in visited:
                    dfs(u)


        for key,val in meets.items():
            visited=set()
            graph=defaultdict(list)
            for (v,u) in val:
                graph[v].append(u)
                graph[u].append(v)

            for v in knows.copy():
                if v not in visited:
                    dfs(v)

        return list(knows)







n =5
meetings =[[3,4,2],[1,2,1],[2,3,1]]
firstPerson =1

print(Solution().findAllPeople(n, meetings, firstPerson))
