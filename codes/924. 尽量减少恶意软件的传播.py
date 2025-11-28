from typing import List


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        initial.sort()
        visited = set()

        def dfs(v:int)->None:
            visited.add(v)

            for index,u in enumerate(graph[v]):
                if index!=v and u==1 and index not in visited:
                    dfs(index)

        for v in initial:
            if v not in visited:
                dfs(v)

        infectnum=len(visited)
        # print(infectnum)
        minindex=0
        afterinfect=0

        n=len(initial)
        i=0
        while  i<n:
            visited = set()
            for index,v in enumerate(initial):
                if i!=index:
                    dfs(v)

            if infectnum-len(visited)>afterinfect:
                afterinfect=infectnum-len(visited)
                minindex=i

            i+=1
            # print(len(visited))


        return initial[minindex]

graph =[[1,0,0,0,1,0,0,0,0,0,1],[0,1,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0,0,0],[0,1,0,1,0,1,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,1,1,0],[0,0,0,0,0,0,1,1,0,0,0],[0,0,1,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,0,1]]
initial =[7,8,6,2,3]

print(Solution().minMalwareSpread(graph,initial))