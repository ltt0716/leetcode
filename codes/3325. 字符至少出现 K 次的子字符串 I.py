import collections

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n=len(s)

        r,l=0,0

        ans=0

        dir=collections.defaultdict(int)

        while r<n:
            dir[s[r]]+=1

            while max(dir.values())>=k:
                dir[s[l]]-=1
                l+=1
            ans+=l
            r+=1
        return ans
    
