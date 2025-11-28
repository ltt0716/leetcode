from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n=len(nums)

        l,r=0,n-1

        while l<=r:
            mid=(l+r)//2

            privot=nums[mid]
            if privot == target:
                return mid

            if nums[0]<=privot:
                if nums[0]<=target<privot:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if privot<target<=nums[n-1]:
                    l=mid+1
                else:
                    r=mid-1

        return -1