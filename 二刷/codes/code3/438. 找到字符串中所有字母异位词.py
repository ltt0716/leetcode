import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)
        need=collections.Counter(p)
        windows=collections.defaultdict(int)

        left,right=0,0
        ans=[]
        cur_valid=0
        all_valid=len(need)
        while right<n:
            c=s[right]
            right+=1

            if c in need:
                windows[c]+=1
                if windows[c]==need[c]:
                    cur_valid+=1


            if cur_valid==all_valid:
                ans.append(left)

            while right-left==m:
                t=s[left]
                left+=1
                if t in need:
                    if windows[t]==need[t]:
                        cur_valid-=1
                    windows[t]-=1
        return ans