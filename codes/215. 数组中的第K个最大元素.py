from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]

        for num in nums:
            if len(min_heap)<k:
                heapq.heappush(min_heap,num)
            else:
                if min_heap[0]<num:
                    heapq.heappushpop(min_heap,num)

        return min_heap[0]