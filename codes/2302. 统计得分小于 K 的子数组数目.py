from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)

        l=r=s=ans=0
        mk=1

        while r<n:
            s+=nums[r]
            mk=s*(r-l+1)

            while mk>=k :
                s-=nums[l]
                l += 1
                mk = s * (r - l + 1)
            ans+=r-l+1
            r+=1
        return ans


