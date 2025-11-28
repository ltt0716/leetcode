from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        n=len(nums)

        l=r=ans=0
        s=1

        while  r<n:
            s*=nums[r]

            while s>=k and l<=r:
                s/=nums[l]
                l+=1
            ans += r - l+1
            r+=1



        return ans




nums =[10,5,2,6]
k=100
print(Solution().numSubarrayProductLessThanK(nums,k))