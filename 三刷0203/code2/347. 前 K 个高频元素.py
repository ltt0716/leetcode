import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=collections.defaultdict(int)

        for i in nums:
            mp[i]+=1

        heap=[]

        for key,val in mp.items():
            if len(heap)<k:
                heapq.heappush((val,key))

            else:
                if val>heap[0][0]:
                    heapq.heappushpop((val,key))

        return [key for _,key in heap]


        
