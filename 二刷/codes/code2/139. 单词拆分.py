from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)

        dp=[False]*(n+1)

        dp[0]=True

        for index in range(1,n):
            for i in range(index):
                if dp[i] and s[i:index] in wordDict:
                    dp[index]=True
                    break

        return dp[n]