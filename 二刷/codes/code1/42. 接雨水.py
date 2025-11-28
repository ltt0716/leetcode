from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        ans=0
        left,right=0,n-1
        lmax,rmax=0,0

        while left<right:

            lmax=max(lmax,height[left])
            rmax=max(rmax,height[right])

            if lmax<rmax:
                ans+=lmax-height[left]
                left+=1
            else:
                ans+=rmax-height[right]
                right-=1

        return ans
