class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n=len(s)

        dp=[0]*n

        for i  in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=2+ (dp[i-2] if i-2>=0 else 0)
                elif s[i-1]==')':
                    lenth=dp[i-1]
                    index=i-1-lenth
                    if index>=0 and s[index]=='(':
                        dp[i]= 2+dp[i-1] + (dp[index-1] if index-1>=0 else 0)
            
        return max(dp)

                        
                            

                    

