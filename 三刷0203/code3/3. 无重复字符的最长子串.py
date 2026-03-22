class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r=0,0

        n=len(s)

        ans=0

        cnt=set()

        while r<n:
            c=s[r]

            while c in cnt:
                cnt.remove(s[l])
                l+=1
            ans=max(ans,r-l+1)
            cnt.add(c)
            r+=1

        return ans