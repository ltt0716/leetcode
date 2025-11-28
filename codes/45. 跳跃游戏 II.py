from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans,n,end,maxr=0,len(nums)-1,0,0

        for i in range(n-1):
            if maxr>=i:
                maxr=max(maxr,i+nums[i])

            if i==end:
                end=maxr
                ans+=1



        return ans
