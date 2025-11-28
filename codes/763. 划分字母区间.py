from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        cnt={}

        for index,val in enumerate(s):
            cnt[val]=index

        ans=[]
        start,end=0,0
        for index,val in enumerate(s):
            if end>=index:
                if index !=cnt[val]:
                    end=max(end,cnt[val])
                else:
                    if end==index:
                        ans.append(end-start+1)
                        start=index+1
                        end=index+1

        return ans
s ="ababcbacadefegdehijhklij"

print(Solution().partitionLabels(s))