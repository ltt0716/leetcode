from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        path=[-1]*n
        cols = set()
        d1=set()
        d2=set()

        def backtracking(row):
            if row == n:
                temp=[]
                for c in path:
                    s='.'*c+'Q'+'.'*(n-1-c)
                    temp.append(s)

                if temp not in ans:

                    ans.append(temp)
                return

            for j in range(n):
                if j not in cols and row-j not in d1 and j+row not in d2:
                    cols.add(j)
                    path[row]=j
                    d1.add(row-j)
                    d2.add(j+row)
                    backtracking(row+1)
                    path[row]=-1
                    cols.remove(j)
                    d1.remove(row-j)
                    d2.remove(j+row)

        backtracking(0)
        return ans



