from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l,r=0,n-1

        newsnums=[]

        while l<r:
            if nums[l]**2<=nums[r]**2:
                newsnums.insert(0,nums[r]**2)
                r=r-1
            elif nums[l]**2>nums[r]**2:
                newsnums.insert(0,nums[l]**2)
                l=l+1

        newsnums.insert(0, nums[l] ** 2)

        return newsnums
