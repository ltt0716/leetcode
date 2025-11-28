import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(nums,target,type):
            l,r=0,len(nums)-1
            ans = -1

            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                elif nums[mid]==target:
                    ans=mid
                    if type=="left":
                        r=mid-1
                    else:
                        l=mid+1

            return ans

        return [search(nums,target,"left"),search(nums,target,"right")]
