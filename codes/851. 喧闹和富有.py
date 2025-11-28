from collections import defaultdict
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n=len(quiet)
        graph=defaultdict(list)

        for v,u in richer:
            graph[u].append(v)

        quietest={}

        def dfs(u):
            if u in quietest:
                return quietest[u]

            min_p=u

            for v in graph[u]:
                minq=dfs(v)
                if quiet[minq]<quiet[min_p]:
                    min_p=minq

            quietest[u]=min_p
            return min_p

        return [dfs(v) for v in range(n)]



richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(Solution().loudAndRich(richer, quiet))