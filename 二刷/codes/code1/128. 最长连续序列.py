from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)

        ans=0

        for num in nums:
            if num-1 in st:
                continue

            x=num+1

            while x in st:
                x+=1

            ans=max(x-num,ans)
        return ans