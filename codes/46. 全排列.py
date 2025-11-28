from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result=[]
        n=len(nums)

        def backtracking(path: List[int],choose :List[int]):
            nonlocal result

            if len(path)==n:
                result.append(path)
                return

            for i in choose:
                newpath=path.copy()
                newpath.append(i)
                newchoose=[ j  for j in choose  if j!=i ]
                backtracking(newpath,newchoose.copy())


        backtracking([],nums)
        return result
