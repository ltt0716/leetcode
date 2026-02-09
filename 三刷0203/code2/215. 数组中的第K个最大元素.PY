import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]

        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap,-num)
            else:
                if  num>=-heap[-1]:
                    heapq.heappushpop(heap,-num)
        
        while len(heap)!=1:
            heapq.heappop(heap)

        return heap[0]
