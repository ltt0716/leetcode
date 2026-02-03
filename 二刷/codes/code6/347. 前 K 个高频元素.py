from typing import List
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=collections.defaultdict(int)

        for key in nums:
            mp[key]+=1

        
        heap=[]

        for key,val in mp.items():
            if len(heap)<k:
                heapq.heappush(heap,(val,key))
            else:
                if val>heap[0][0]:
                    heapq.heappushpop(heap,(val,key))

        return [key for val,key in heap]
    
