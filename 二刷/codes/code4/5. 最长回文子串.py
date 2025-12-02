class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        n=len(s)

        def dfs(l,r):
            nonlocal ans
            while l>=0 and r<n:
                if s[l]==s[r]:
                    if len(ans)<r-l+1:
                        ans=s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
        

        for i in range(n):
            dfs(i,i)
            if i <n-1:
                dfs(i,i+1)
        
        return ans

s="a"

print(Solution.longestPalindrome(s))
