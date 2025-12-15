from typing import List
import math

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)

        for i in range(n):
            if nums[i]<=0:
                nums[i]=n+1
        
        for i in range(n):
            abs=nums[i] if nums[i] >0 else -nums[i]
            if abs>=n+1:
                continue

            if nums[abs-1]>0:
                nums[abs-1]=-nums[abs-1]
        
        for i in range(n):
            if nums[i]>0:
                return i+1
            
        return n+1
    


