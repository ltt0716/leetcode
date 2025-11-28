from typing import List
from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        graph1=[[] for i in range(k)]
        line={}
        indegree1=[0]*k
        for u,v in rowConditions:
            graph1[u-1].append(v-1)
            indegree1[v-1]+=1

        q1=deque()

        for index,val in enumerate(indegree1):
            if val==0:
                q1.append(index)

        index=0

        while q1:
            cur=q1.popleft()
            line[cur]=index
            index+=1

            for v in graph1[cur]:
                if indegree1[v]>=1:
                    indegree1[v]-=1
                if indegree1[v]==0:
                    q1.append(v)

        if index!=k:
            return []

        graph2 = [[] for i in range(k)]
        col = {}
        indegree2 = [0] * k
        for u, v in colConditions:
            graph2[u - 1].append(v - 1)
            indegree2[v - 1] += 1

        q2 = deque()

        for index, val in enumerate(indegree2):
            if val == 0:
                q2.append(index)

        index = 0

        while q2:
            cur = q2.popleft()
            col[cur] = index
            index += 1

            for v in graph2[cur]:
                if indegree2[v] >= 1:
                    indegree2[v] -= 1
                if indegree2[v] == 0:
                    q2.append(v)
        if index!=k:
            return []

        ans=[[0 for i in range(k)] for i in range(k)]

        for index,val in line.items():
            ans[val][col[index]]=index+1
        return ans

k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]

print(Solution().buildMatrix(k,rowConditions,colConditions))


