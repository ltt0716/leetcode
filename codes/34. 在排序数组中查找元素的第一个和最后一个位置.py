from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)
        f1=False

        while left<right:
            mid=(left+right)//2

            if nums[mid]==target:
                f1=True

            if nums[mid]<target:
                left=mid+1
            else:
                right=mid

        ans1=left
        left, right = 0, len(nums)

        while left<right:
            mid=(left+right)//2

            if nums[mid]>target:
                right=mid
            else:
                left=mid+1

        ans2=left-1


        return [ans1, ans2] if f1 else [-1,-1]



