class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack = [-1]
        # maxl = 0
        # for index, val in enumerate(s):
        #     if val == '(':
        #         stack.append(index)
        #     elif val == ')':
        #         stack.pop()
        #         if (len(stack) == 0):
        #             stack.append(index)
        #         else:
        #             maxl = max(maxl, index - stack[0])
        #
        # return maxl

        n=len(s)
        if n==0:
            return 0

        def check(i):
            if i>=0:
                return True
            return False
        dp=[0]*(n)

        for  i in range(n):
            if i>0 and s[i]==')':
                if s[i-1]=='(':
                    if check(i-2):
                        dp[i]=dp[i-2]+2
                    else:
                        dp[i]=2
                elif s[i-1]==')':
                    if check(i-dp[i-1]-1):
                        if s[i-dp[i-1]-1]=='(':
                            if check(i-dp[i-1]-2):
                                dp[i]=dp[i-dp[i-1]-2]+2+dp[i-1]
                            else:
                                dp[i]=2+dp[i-1]


        print(dp)
        return max(dp)
s="(()))())("

print(Solution().longestValidParentheses(s))