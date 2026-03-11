class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        l,r=0,0

        while l<n:

            while nums[l]!=0:
                l+=1
                if l>=n-1 :
                    return nums
            
            
            r=r+1
            while r<n and nums[r]==0 :
                r+=1
            if r<n:
                nums[l],nums[r]=nums[r],nums[l]

        