import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap=[(-nums[i],i) for i in range(k)]
        heapq.heapify(heap)
        ans=[-heap[0][0]]

        for i in range(k,len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            peek,index=-heap[0][0],heap[0][1]
            while i-index+1>k:
                heapq.heappop(heap)
                peek,index=-heap[0][0],heap[0][1]
            
            ans.append(peek)

        return ans


