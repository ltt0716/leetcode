import collections
from typing import List
from math import inf

class Solution:
    def minimumCost(self, source: str, target: str, original:List[str], changed: List[str], cost: List[int]) -> int:

        letters=set(sorted(original+changed))
        letset=collections.defaultdict(int)
        for index, letter in enumerate(letters):
            letset[letter]=index

        n=len(letset)

        g=collections.defaultdict(list)
        for u,v,w in zip(original,changed,cost):
            g[u].append((v,w))

        temp=[[inf]*n for _ in range(n)]
        for key,value in g.items():
            for v,w in value:
                if w <temp[letset[key]][letset[v]]:
                    temp[letset[key]][letset[v]]=w

        f=[[[inf]*n for _ in range(n)] for _ in range(n+1)]
        f[0]=temp

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    f[k+1][i][j]= min(f[k][i][j],f[k][i][k]+f[k][k][j])


        index=0
        ans=0

        while index<len(target):
            a,b=source[index],target[index]
            index+=1
            if a==b:
                continue
            if a not in original:
                return -1
            x1=letset[a]
            x2=letset[b]

            ww=f[n][x1][x2]
            if ww==inf:
                return -1
            else:
                ans+=ww
        return ans



