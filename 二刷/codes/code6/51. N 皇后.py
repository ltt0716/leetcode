from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]


        matrix=[['.' for _ in range(n)] for _ in range(n)]
        cols=[]
        dir1=[]
        dir2=[]

        
        def backtracking(row):
            if row==n:
                if len(cols)==n:
                    temp=[]
                    for i in range(n):
                        s=""
                        for j in range(n):
                            s+=matrix[i][j]
                        temp.append(s)

                    
                    ans.append(temp)
                return
            
            for i in range(n):
                if i not in cols and row-i not in dir1 and row+i not in dir2:
                    matrix[row][i]='Q'
                    cols.append(i)
                    dir1.append(row-i)
                    dir2.append(row+i)
                    backtracking(row+1)
                    matrix[row][i]='.'
                    cols.pop()
                    dir1.pop()
                    dir2.pop()
        
        backtracking(0)
        
        return ans