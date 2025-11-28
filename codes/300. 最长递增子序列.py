from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            num=nums[i-1]
            for j in range(0,i-1):
                if num>nums[j]:
                    dp[i]=max(dp[i],dp[j+1]+1)


        return max(dp)

