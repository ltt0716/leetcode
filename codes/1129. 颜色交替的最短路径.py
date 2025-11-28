import math
from collections import defaultdict,deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        g=defaultdict(set)

        for v,u in redEdges:
            g[v].add((u,0))

        for v,u in blueEdges:
            g[v].add((u,1))

        q=deque()
        q.append((0,-1))
        dis=[[math.inf]*2 for i in range(n)]
        dis[0][0]=0
        dis[0][1]=0
        # visited=set()
        q.append((0, 0))  # 节点0，上一条边是红色
        q.append((0, 1))  # 节点0，上一条边是蓝色
        while q:

            cur,last=q.popleft()

            for v,color in g[cur]:
                if  color!=last and dis[v][color]==math.inf:
                    dis[v][color] = dis[cur][last] + 1
                    q.append((v,color))

        return [ min(a,b) if min(a,b)!=math.inf else -1 for a,b in dis ]


n =3
redEdges =[[0,1],[0,2]]
blueEdges =[[1,0]]
print(Solution().shortestAlternatingPaths(n,redEdges,blueEdges))




