import math
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp=[math.inf]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(n+1):
            for j in range(1,math.floor(sqrt(i))+1):
                dp[i]=min(dp[i-j*j]+1,dp[i])
        return dp[n]
