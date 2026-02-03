import math
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[math.inf]*(amount+1)
        dp[0]=0

        coins.sort()

        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i]=min(dp[i],dp[i-coin]+1)
                else:
                    break
    
        
        return dp[amount] if dp[amount]!=math.inf else -1

coins =[2]
amount =3

print(Solution().coinChange(coins,amount))