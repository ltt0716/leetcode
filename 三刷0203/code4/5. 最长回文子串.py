class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ll,rr=0,0
        def dfs(l,r):
            nonlocal ll,rr
            while l>0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            
            if r-l+1-2>rr-ll+1:
                ll,rr=l,r
                
        
        for i in range(n):
            dfs(i,i)
            dfs(i,i+1)


            


        return s[ll+1:rr]