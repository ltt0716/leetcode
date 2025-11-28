import math
from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)
        graph=[[]for _ in range(n)]

        for index,val in enumerate(edges):
            if val!=-1:
                graph[index].append(val)

        dis1={}
        dis2={}

        q1=deque()
        q2=deque()

        q1.append((node1,0))
        q2.append((node2,0))
        vis1=set()
        vis2=set()
        vis1.add(node1)
        vis2.add(node2)

        while q1:
            cur,dis =q1.popleft()
            dis1[cur]=dis

            for v in graph[cur]:
                if v not in dis1:
                    q1.append((v,dis+1))
        while q2:
            cur, dis = q2.popleft()
            dis2[cur] = dis

            for v in graph[cur]:
                if v not in dis2:
                    q2.append((v, dis + 1))

        # print(dis1,dis2)
        ans=math.inf
        nod=[]
        for k1,v1 in dis1.items():
            if k1 not in dis2.keys():
                continue
            else:
                d1=v1
                d2=dis2[k1]

                if ans>max(d1,d2):
                    ans=max(d1,d2)
                    nod=[k1]
                elif ans==max(d1,d2):
                    nod.append(k1)

        if len(nod)==0:
            return -1
        else:
            return min(nod)

edges = [2,2,3,-1]
node1 = 0
node2 = 1

print(Solution().closestMeetingNode(edges, node1, node2))