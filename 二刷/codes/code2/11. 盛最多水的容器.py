from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        ans=0
        while l<r:
            cur=min(height[l],height[r])*(r-l)

            ans=max(ans,cur)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans