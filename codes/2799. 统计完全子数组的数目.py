import collections
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        k=len(set(nums))

        l,r=0,0

        dir=collections.defaultdict(int)

        while r<n:
            dir[nums[r]]+=1

            while len(dir) >=k:
                dir[nums[l]]-=1
                if dir[nums[l]]==0:
                    del dir[nums[l]]
                l+=1

            ans+=l
            r+=1
        return ans 
