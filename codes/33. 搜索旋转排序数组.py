from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2

            x=nums[mid]

            if x==target:
                return mid

            if nums[0]<=x:
                if nums[0]<=target<x:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if x<target<=nums[-1]:
                    l=mid+1
                else:
                    r=mid-1

        return -1