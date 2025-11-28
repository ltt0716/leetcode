import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[math.inf]*(amount+1)
        dp[0]=0
        for x in coins:
            for i in range(1,amount+1):
                if i >=x:
                    dp[i]=min(dp[i],dp[i-x]+1)

        return  dp[amount] if dp[amount]!=math.inf else -1
