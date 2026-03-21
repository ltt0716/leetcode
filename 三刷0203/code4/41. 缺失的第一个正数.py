import math
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)

        for i in range(n):
            if nums[i] <=0:
                nums[i]=n+1
        
        for i in range(n):
            if abs(nums[i])<n+1:
                nums[abs(nums[i])-1]=-nums[abs(nums[i])-1]
            
  

        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1




nums =[3,4,-1,1]

print(Solution().firstMissingPositive(nums))