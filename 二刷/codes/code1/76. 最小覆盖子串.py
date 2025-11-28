import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur=collections.defaultdict(int)
        need=collections.defaultdict(int)

        for c in t :
            need[c]+=1

        l,r,n=0,0,len(s)
        valid=0
        t_valid=len(need.items())
        ans=""

        while r<n:
            ch=s[r]

            if ch in need:
                cur[ch]+=1
                if cur[ch]==need[ch]:
                    valid+=1

            while valid==t_valid:
                if ans=="" or r-l+1<len(ans):
                    ans=s[l:r+1]
                ch=s[l]
                if ch in need:
                    if need[ch]==cur[ch]:
                        valid-=1
                    cur[ch]-=1
                l+=1
            r+=1

        return ans
s ="ADOBECODEBANC"
t ="ABC"

print(Solution().minWindow(s,t))