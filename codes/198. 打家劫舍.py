from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        ans=[0 for _ in range(n)]

        ans[0]=nums[0]
        if n==1:
            return ans[n-1]
        
        ans[1]=max(nums[0],nums[1])

        for i in range(2,n):
            ans[i]=max(ans[i-2]+nums[i],ans[i-1])

        return ans[n-1]


