import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        n=len(nums)

        ans=[]
        
        for i in range(n):
            heapq.heappush(heap,(-nums[i],i))
            
            if i>=k-1:
                max_val,max_index=heap[0]
                while i-max_index+1>k:
                    heapq.heappop(heap)
                    max_val,max_index=heap[0]

                ans.append(-max_val)
        return ans
