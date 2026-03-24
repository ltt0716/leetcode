class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        left=[nums[0]]*n
        right=[nums[-1]]*n

        for i in range(1,n):
            left[i]=left[i-1]*nums[i]

        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i]
        

        ans=[0]*n

        for i in range(n):
            if i>0:
                ans[i]=left[i-1]
            if i+1<n:
                ans[i]*=right[i+1]
            
        return ans