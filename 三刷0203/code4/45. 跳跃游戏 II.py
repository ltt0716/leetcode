class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n=len(nums)
        ans=0
        end=0
        max_r=0
        for i in range(n-1):
            max_r=max(max_r,i+nums[i])

            if i==end:
                ans+=1
                end=max_r


        
        return ans