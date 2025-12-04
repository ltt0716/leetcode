import heapq
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        heap=[]
        ans=[]
        for i in range(n):
            if len(heap)<k-1:
                heapq.heappush(heap,(-nums[i],i))
                continue
            heapq.heappush(heap,(-nums[i],i))

            while i-heap[0][1]+1>k:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans
