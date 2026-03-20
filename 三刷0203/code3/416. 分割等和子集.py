class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)

        if total %2==1:
            return False
        
        n=total//2

        dp=[False]*(n+1)
        dp[0]=True



