from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n =len(candidates)
        ans =[]
        path=[]
        def backtracking(i,cur):
            if cur>target or i ==n:
                return

            if cur==target:
                ans.append(path[:])
                return

            backtracking(i+1,cur)

            path.append(candidates[i])
            backtracking(i,cur+candidates[i])
            path.pop()

        backtracking(0,0)
        return ans

