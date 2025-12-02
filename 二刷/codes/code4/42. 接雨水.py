from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        left=[0]*n
        maxl=left[0]=0
        right=[0]*n
        maxr=right[n-1]=height[n-1]
        for i in range(n):
            maxl=max(maxl,height[i])
            left[i]=maxl

        for i in range(n-1,-1,-1):
            maxr=max(maxr,height[i])
            right[i]=maxr

        ans=0
        for i in range(n):
            ans+=min(left[i],right[i])-height[i]

        return ans
        