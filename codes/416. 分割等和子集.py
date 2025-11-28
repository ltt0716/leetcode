from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)

        sumcount=sum(nums)

        if sumcount%2==1:
            return False
        half=sumcount/2

        if max(nums)>half:
            return False
        cnt={}

        def dfs(i,j):

            if j<0:
                return False
            if j==0:
                return True

            if i<0:
                return False

            if (i,j) in cnt:
                return cnt[(i,j)]

            t=dfs(i-1,j-nums[i]) or dfs(i-1,j)
            cnt[(i,j)]=t
            return t

        return dfs(n-1,half)