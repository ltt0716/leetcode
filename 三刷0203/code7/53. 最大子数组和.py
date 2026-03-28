class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[-math.inf]*n
        ans[0]=nums[0]

        for i in range(1,n):
            ans[i]=max(nums[i],ans[i-1]+nums[i])
        
        return max(ans)
