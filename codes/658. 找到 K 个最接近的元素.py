from bisect import bisect, bisect_left
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)

        index=bisect_left(arr,x)
        l,r=index-1,index

        for _ in range(k):
            if l<0:
                r+=1
            elif r>=n:
                l-=1
            else:
                if abs(arr[l]-x) <=abs(arr[r]-x):
                    l-=1
                else:
                    r+=1
        return arr[l+1:r]
