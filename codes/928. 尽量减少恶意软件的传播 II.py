import collections
import math
from typing import List
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)

        def dfs(u:int):
            nonlocal visited,size,nodeid

            visited.add(u)
            size+=1

            for index,val in enumerate(graph[u]):
                if index in initial and val==1:
                    if nodeid==-1:
                        nodeid=index
                    elif nodeid!=-1 and nodeid!=index:
                        nodeid=-2
                    continue
                if val==1 and index not in visited:
                    dfs(index)

        cnt=collections.defaultdict(int)
        visited = set()

        for i  in range(n):
            if i not in initial and i not in  visited:
                size=0
                nodeid=-1
                dfs(i)
                if nodeid>=0:
                    cnt[nodeid]+=size

        return min((-val,key) for  key,val in cnt.items())[1] if cnt else min(initial)

graph =[[1,1,0,0],[1,1,0,1],[0,0,1,0],[0,1,0,1]]
initial =[3,0]
print(Solution().minMalwareSpread(graph,initial))