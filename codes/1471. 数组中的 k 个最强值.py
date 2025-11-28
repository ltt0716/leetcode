from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        arr.sort()

        index=(n-1)//2

        l,r=0,n-1
        m=arr[index]
        ans=[]
        for _ in range(k):
            if  abs(m-arr[l])<=abs(arr[r]-m):
             ans.append(arr[r])
             r-=1
            else:
                ans.append(arr[l])
                l+=1

        return ans