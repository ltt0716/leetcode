class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=""


        def dfs(l,r):
            nonlocal n,ans

            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>len(ans):
                ans=s[l+1:r]

        
        for i in range(n):
            dfs(i,i)

            if i+1<n:
                dfs(i,i+1)
        
        return ans