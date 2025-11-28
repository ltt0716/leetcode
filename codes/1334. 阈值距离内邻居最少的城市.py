from functools import cache
from typing import List
from math import inf

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[inf]*n for _ in range(n)]
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w


        val=inf
        ans=-1
        # @cache
        # def Floyd(k,i,j):
        #     if k<0:
        #         return dist[i][j]
        #     return min(Floyd(k-1,i,j),Floyd(k-1,i,k)+Floyd(k-1,k,j))
        #
        # for i in range(n):
        #     cnt=0
        #     for j in range(n):
        #         if i!=j and Floyd(n-1,i,j)<=distanceThreshold:
        #             cnt+=1
        #
        #     if cnt<=val:
        #         val=cnt
        #         ans=i

        f=[[[inf]*n for _ in range(n)] for _ in range(n+1)]
        f[0]=dist

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    f[k+1][i][j]=min(f[k][i][j],f[k][i][k]+f[k][k][j])

        for i in range(n):
            cnt=0
            for j in range(n):
                if i!=j and f[n][i][j]<=distanceThreshold:
                    cnt+=1

            if cnt<=val:
                val=cnt
                ans=i


        return ans