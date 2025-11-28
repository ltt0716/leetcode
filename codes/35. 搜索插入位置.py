from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i, j = 0, len(nums)

        while i<j:
            mid=(i+j)//2

            if nums[mid]<target:
                i=mid+1
            elif nums[mid]>=target:
                j=mid


        return i


