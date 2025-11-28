# Definition for singly-linked list.
from collections import deque
from typing import List



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ans = 0
        fresh = 0
        q = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:

            i, j, t = q.popleft()

            ans = max(ans, t)

            for dx, dy in dirs:
                x = dx + i
                y = dy + j
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh -= 1
                    q.append((x, y, t + 1))


        return ans if fresh == 0 else -1

