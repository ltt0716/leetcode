from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)

        ans=[]
        cur=[]
        def backtracking(i):

            if i==n:
                ans.append(cur[:])
            else:
                for j in range(n):
                    if nums[j] not in cur:
                        cur.append(nums[j])
                        backtracking(i+1)
                        cur.pop()

        backtracking(0)
        return ans