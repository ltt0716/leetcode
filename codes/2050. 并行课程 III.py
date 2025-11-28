from typing import List
from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph=[[]for i in range(n)]
        indegree=[0 for i in range(n)]

        for u,v in relations:
            graph[u-1].append(v-1)
            indegree[v-1]+=1

        q=deque([index for index,val in enumerate(indegree) if val==0])
        finished = [time[index] if val==0 else 0 for index,val in enumerate(indegree) ]


        while q:
            cur=q.popleft()
            for v in graph[cur]:
                indegree[v]-=1
                finished[v]=max(finished[v],finished[cur]+time[v])
                if indegree[v]==0:
                    q.append(v)
        return max(finished)

n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]
print(Solution().minimumTime(n, relations, time))
