from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)

        l,r=0,n-1

        while l<r and l<n and r>-1:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1


