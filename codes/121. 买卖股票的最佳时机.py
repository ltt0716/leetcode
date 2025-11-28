from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0

        min_p=prices[0]

        for p in prices:
            ans=max(p-min_p,0)
            min_p=min(min_p,p)

        return ans
