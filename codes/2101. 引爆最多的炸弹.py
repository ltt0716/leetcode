from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)

        adj=[[] for i in range(n)]

        for index1,li1  in enumerate(bombs):
            x1,y1=li1[0],li1[1]
            for index2,li2  in enumerate(bombs):
                x2,y2=li2[0],li2[1]
                r=((y2-y1)**2+(x2-x1)**2)**0.5
                adj[index1].append(r)


        def dfs(v:int):
            nonlocal visited,size
            visited.add(v)
            size+=1

            for index,r in enumerate(adj[v]):
                if index not in visited and r<=bombs[v][2]:
                    dfs(index)

        ans=0
        for v in range(n):
            visited=set()
            size=0
            dfs(v)
            ans=max(ans,size)

        return ans



bombs = [[2,1,3],[6,1,4]]

print(Solution().maximumDetonation(bombs))