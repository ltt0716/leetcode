from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return dp[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=nums[1]

        for i in range(2,n):

            dp[i]=max(dp[0:i-1])+nums[i]

        print(dp)
        return max(dp)

nums =[1,2,3,1]

print(Solution().rob(nums))