from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp={}
        for key in nums:
            if key not in mp.keys():
                mp[key]=1
            else:
                mp[key]+=1

        min_heap=[]

        for key,val in mp.items():
            if len(min_heap)<k:
                heapq.heappush(min_heap,(val,key))
            else:
                if min_heap[0][0]<val:
                    heapq.heappushpop(min_heap,(val,key))

        return [ key for val,key in min_heap]