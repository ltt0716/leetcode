from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)

        cnt={}

        for i in range(n-1,-1,-1):
            ch=s[i]

            if ch not in cnt.keys():
                cnt[ch]=i
        
        ans=[]

        start,end=0,0

        for i in range(n):
            ch=s[i]
            if cnt[ch]>end:
                end=cnt[ch]


            if i==end:
                ans.append(end-start+1)
                start,end=end+1,end+1
        
        return ans

        