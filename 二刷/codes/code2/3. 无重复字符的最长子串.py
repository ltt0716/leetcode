class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n=len(s)

        l,r=0,0

        cur=""
        ans=0
        while r<n:
            if s[r] not in cur:
                cur+=s[r]
                ans=max(ans,len(cur))
                r+=1
            else:
                cur=cur[1:]
                l+=1

        return  ans