from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumall = sum(nums)
        if sumall % 2 != 0:
            return False

        n=len(nums)
        half = sumall // 2

        dp=[False]*(half+1)
        dp[0]=True

        for i in range(half,0,-1):
            for j in range(n-1,-1,-1):
                if i>=nums[j]:
                    dp[i]=dp[i] or dp[i-nums[j]]

        return dp[half]