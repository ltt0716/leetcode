from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)

        target_index=n-k

        def quickchoose(left,right,k):
            if left==right:
                return nums[left]
            
            privot=nums[left]
            i,j=left-1,right+1

            while i<j:

                i+=1
                while nums[i]<privot:
                    i+=1
                j-=1
                while nums[j]>privot:
                    j-=1

                if i<j:
                    nums[i],nums[j]=nums[j],nums[i]

            if k<=j:
                return quickchoose(left,j,k)
            else:
                return quickchoose(j+1,right,k)

        return quickchoose(0,n-1,target_index)
             
