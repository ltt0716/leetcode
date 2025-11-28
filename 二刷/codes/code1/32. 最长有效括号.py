class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0


        n=len(s)

        dp=[0 for _ in range(n)]

        for index,ch in enumerate(s):
            if ch ==")":
                if index-1>=0:
                    if s[index-1]==')':
                        if index-1-dp[index-1]>=0 and s[index-1-dp[index-1]]=='(':
                            dp[index]=dp[index-1]+2
                            if index-1-dp[index-1]-1>=0:
                                dp[index]+=dp[index-1-dp[index-1]-1]

                    else:
                        dp[index]=2
                        if index - 2 >= 0:
                            dp[index] += dp[index - 2]
        print(dp)
        return max(dp)
s =")()())"

print(Solution().longestValidParentheses(s))