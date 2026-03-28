class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)

        min_dp=nums.copy()
        max_dp=nums.copy()

        for i in range(1,n):
            max_dp[i]=max(nums[i]*min_dp[i-1],nums[i]*max_dp[i-1],max_dp[i])

            min_dp[i]=min(nums[i]*min_dp[i-1],nums[i]*max_dp[i-1],min_dp[i])
        
        return max(max_dp)