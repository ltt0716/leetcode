import heapq
import math
from typing import List

class State:
    def __init__(self,x,y,dis):
        self.x = x
        self.y = y
        self.dis = dis
    def __lt__(self,other):
        return self.dis < other.dis

def getNear(n,m,x,y):
    ans=[]
    if 0<=x-1 and x-1<n:
        ans.append((x-1,y))
    if 0<=x+1 and x+1<n:
        ans.append((x+1,y))
    if 0<=y-1 and y-1<m:
        ans.append((x,y-1))
    if 0<=y+1 and y+1<m:
        ans.append((x,y+1))
    return ans



class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n=len(moveTime)
        m=len(moveTime[0])

        visited=[[False]*m for _ in range(n)]
        dist=[[math.inf]*m for _ in range(n)]

        dist[0][0]=0

        q=[]

        heapq.heappush(q,State(0,0,0))

        while q:
            s=heapq.heappop(q)
            x, y, dis=s.x, s.y, s.dis
            if visited[x][y]==True:
                continue
            visited[x][y]=True

            ans=getNear(n,m,x,y)
            for dx,dy in ans:
                d=max(dist[x][y],moveTime[dx][dy])+1
                if d<dist[dx][dy]:
                    dist[dx][dy]=d
                    heapq.heappush(q,State(dx,dy,d))

        return dist[n-1][m-1]


moveTime =[[0,4],[4,4]]
print(Solution().minTimeToReach(moveTime))