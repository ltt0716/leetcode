from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(candidates)
        path=[]

        candidates.sort()
        def  backtracking(i,left):
            nonlocal path
            if left==0:
                ans.append(path[:])
                return

            if  i==n or left<candidates[i]:
                return

            for j in range(i,n):
                if left<candidates[j]:
                    break

                path.append(candidates[j])
                backtracking(j,left-candidates[j])
                path.pop()

        backtracking(0,target)

        return ans
