from typing import List
from collections import deque
import math
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap=[]

        
        res=[]

        for index,val in enumerate(nums):
            heapq.heappush(heap,(-val,index))
            if index<k-1:
                continue
            v,i =heap[0]
            while index-i+1>k:
                heapq.heappop(heap)
                v,i =heap[0]
            res.append(-v)
        return res