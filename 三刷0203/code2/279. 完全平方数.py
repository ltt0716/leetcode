class Solution:
    def numSquares(self, n: int) -> int:
        
        dp=[math.inf for _ in range(n+1)]

        dp[0]=0
        dp[1]=1

        for i in range(1,n+1):
            j=math.sqrt(i)

            for m in range(1,j+1):
                dp[i]=min(dp[i],dp[i-m^2])
        
        return dp[n]