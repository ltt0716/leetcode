from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        path=[]
        n=len(s)

        def backtracking(i,start):
            nonlocal path

            if i ==n:
                ans.append(path[:])
                return

            for j in range(i,n):
                t=s[start:j+1]
                if t==t[::-1]:
                    path.append(t)
                    backtracking(j+1,j+1)
                    path.pop()

        backtracking(0,0)
        return ans


