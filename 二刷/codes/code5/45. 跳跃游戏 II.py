from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        n=len(nums)

        index=end=0
        ans=0

        for i in range(n):
            if index>=i:
                index=max(index,i+nums[i])
                if index>=n-1:
                    return ans+1
                if i==end:
                    ans+=1
                    end=index
