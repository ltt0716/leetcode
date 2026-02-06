class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        
        l,r=0,n-1


        while l<=r:
            if l==r:
                return nums[l]
        
            mid=(l+r)//2

            val=nums[mid]

            if nums[l]<nums[r]:
                r=mid
            else:
                if val<=nums[r]:
                    r=mid
                else:
                    l=mid+1
