from typing import List
from collections import deque,defaultdict

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        visited=[False]*n
        ans=-1

        for i in range(n):
            if visited[i]==False:
                pathmap = defaultdict(int)

                step=0
                next=edges[i]

                while next!=-1 and not visited[next]:
                    visited[next]=True
                    pathmap[next]=step
                    step+=1
                    next=edges[next]
                    if next in pathmap.keys():
                        ans=max(ans,step-pathmap[next])
                        break

        return ans