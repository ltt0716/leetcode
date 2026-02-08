class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        n=len(s)
        l,r=0,0
        ans=0
        now=set()
        while r<n:
            c=s[r]
            if c not in now:
                now.add(c)
                ans=max(ans,r-l+1)
            else:
                while s[l]!=c:
                    now.remove(s[l])
                    l+=1
                l+=1
            r+=1

        return ans


