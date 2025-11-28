from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        n=len(candidates)

        def dfs(i,left):
            if i==n or left<0:
                return

            if left==0:
                ans.append(path[:])
                return
            path.append(candidates[i])
            dfs(i,left-candidates[i])
            path.pop()
            dfs(i + 1, left)


        dfs(0, target)
        return  ans