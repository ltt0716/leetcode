from collections import defaultdict
from typing import List


class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #
    #     ans=0
    #     for i in range(len(nums)):
    #         sum=0
    #         for j in range(i,-1,-1):
    #             sum+=nums[j]
    #             if sum==k:
    #                 ans+=1
    #     return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        mp=defaultdict(int)
        sum=0
        count=0
        for num in nums:
            mp[sum]+=1
            sum+=num
            count+=mp[sum-k]

        return count

nums =[1,1,1]
k =2
print(Solution().subarraySum(nums,k))