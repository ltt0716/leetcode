import collections
import math
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n=len(patience)

        g=[[] for i in range(n)]

        for u,v in edges:
            g[v].append(u)
            g[u].append(v)

        dist=[None]*n
        dist[0]=0

        q=collections.deque([0])

        while q:
            cur=q.popleft()

            for v in g[cur]:
                if dist[v]==None:
                    dist[v]=dist[cur]+1
                    q.append(v)

        max_time=0

        for index,dis in enumerate(dist):
            if 2*dis<=patience[index]:
                max_time=max(max_time,2*dis)
            else:
                t=(2*dis-1)//patience[index]
                time=t*patience[index]+2*dis
                max_time=max(max_time,time)


        # print(times)
        return max_time+1

edges =[[3,8],[4,13],[0,7],[0,4],[1,8],[14,1],[7,2],[13,10],[9,11],[12,14],[0,6],[2,12],[11,5],[6,9],[10,3]]
patience =[0,3,2,1,5,1,5,5,3,1,2,2,2,2,1]
print(Solution().networkBecomesIdle(edges, patience))