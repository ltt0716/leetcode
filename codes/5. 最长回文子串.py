class Solution:
    def longestPalindrome(self, s: str) -> str:

        n=len(s)
        cnt={}
        if n==1:
            return s
        elif n==2:
            if s==s[::-1]:
                return s
            else:
                return s[0]

        maxr,start=1,0
        def dfs(i,j):
            nonlocal  maxr,start
            l,r=i,j
            while l>=0 and r<=n-1 and s[l]==s[r]:
                l-=1
                r+=1

            if maxr<r-l-1:
                maxr=r-l-1
                start=l+1

        for i in range(n):
            dfs(i,i)
            dfs(i,i+1)
        return s[start:maxr+start]

s="aaaa"
print(Solution().longestPalindrome(s))