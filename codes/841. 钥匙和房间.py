from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)

        visited=[False]*n

        def bfs(v):
            visited[v]=True

            for i in rooms[v]:
                if not visited[i]:
                    bfs(i)

        visited[0]=True
        bfs(0)

        ans=True
        for i in range(n):
            if not visited[i]:
                ans=False

        return ans