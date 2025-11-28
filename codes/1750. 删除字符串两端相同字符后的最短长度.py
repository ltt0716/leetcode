class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)

        l,r=0,n-1

        while l<r and s[l]==s[r]:

            ch=s[l]

            while l<=r and s[l]==ch:
                l+=1
            while r>=l and s[r]==ch:
                r-=1

        return r-l+1







s="aabccabba"
print(Solution().minimumLength(s))


