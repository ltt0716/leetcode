from typing import List
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp_max=nums.copy()
        dp_min=nums.copy()

        for i in range(n):
            if i==0:
                continue

            big=dp_max[i-1]
            small=dp_min[i-1]
            cur1=big*nums[i]
            cur2=small*nums[i]

            dp_max[i]=max(dp_max[i],cur1,cur2)
            dp_min[i]=min(dp_min[i],cur1,cur2)

        return max(dp_max)
