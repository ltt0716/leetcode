from typing import List
from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=[[] for i in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves=[index for index,neighbor in enumerate(graph) if len(neighbor)==1]

        nodes=set([i for i in range(n)])

        # print(nodes,leaves)
        while len(nodes)>2:

            for i in leaves.copy():
                nodes.remove(i)
                leaves.remove(i)
                neighbor=graph[i][0]
                graph[neighbor].remove(i)
                if len(graph[neighbor])==1:
                    leaves.append(neighbor)
        return list(nodes)





n = 6
edges =[[0,1],[0,2],[0,3],[3,4],[4,5]]
print(Solution().findMinHeightTrees(n,edges))


