from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt={}
        for index,c in enumerate(s):
            cnt[c]=index


        start,end=0,0
        n=len(s)
        ans=[]
        mr=0
        for i in range(n):
            print(i)
            if mr>=i:
                mr=max(mr,cnt[s[i]])
                if i==mr:
                    ans.append(mr-start+1)
                    start=mr+1
                    mr=mr+1
        return ans
s ="eccbbbbdec"

print(Solution().partitionLabels(s))