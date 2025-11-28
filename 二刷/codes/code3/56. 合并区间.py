from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        ans=[]

        for start,end in intervals:
            if not ans or start>ans[-1][1]:
                ans.append([start,end])
            else:
                if end>ans[-1][1]:
                    ans[-1][1]=end
        
        return ans