from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_r,end=0,0
        n=len(nums)
        for index,val in enumerate(nums):
            if index>=max_r:
                max_r=max(max_r,index+val)
                if max_r>=n-1:
                    return True
                if index==end:
                    end=max_r
        return  False