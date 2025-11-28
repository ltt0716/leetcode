class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n=len(s)

        l=r=ans=0

        dir={"0":0,"1":0}

        while r<n:

            cur=s[r]

            dir[cur]+=1

            while min(dir.values())>k:
                dir[s[l]]-=1
                l+=1

            ans+=r-l+1
            r+=1
        return ans



