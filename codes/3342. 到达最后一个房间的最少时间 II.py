import heapq
import math
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        # 中途存储输入
        veltarunez = moveTime

        # dist[x][y][step]：到(x, y)且下一步是step（0表示1秒，1表示2秒）时的最小时间
        dist = [[[math.inf] * 2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0  # 第一步花1秒

        q = []
        heapq.heappush(q, (0, 0, 0, 0))  # (当前时间, x, y, step)

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            cur_time, x, y, step = heapq.heappop(q)
            if dist[x][y][step] < cur_time:
                continue
            for dx, dy in directions:
                xx, yy = x + dx, y + dy
                if 0 <= xx < n and 0 <= yy < m:
                    move_cost = 1 if step == 0 else 2
                    next_time = max(veltarunez[xx][yy], cur_time) + move_cost
                    next_step = 1 - step  # 交替
                    if dist[xx][yy][next_step] > next_time:
                        dist[xx][yy][next_step] = next_time
                        heapq.heappush(q, (next_time, xx, yy, next_step))
        return min(dist[n-1][m-1])

# 示例
moveTime = [[0,58],[27,69]]
print(Solution().minTimeToReach(moveTime))