import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        df=[math.inf]*(amount+1)

        df[0]=0

        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    df[i]=min(df[i],df[i-j]+1)

        return int(df[amount]) if df[amount]!=math.inf else -1
coins = [1, 2, 5]
amount = 11

print(Solution().coinChange(coins,amount))