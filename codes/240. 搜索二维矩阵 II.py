from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n,m=len(matrix),len(matrix[0])

        flag=False
        def search(i,j):
            nonlocal flag
            if matrix[i][j]==target:
                flag=True
                return

            if matrix[i][j]>target:
                x,y=i,j-1
                if y>0:
                    search(x,y)

            if matrix[i][j]<target:
                x,y=i+1,j
                if x<n:
                    search(x,y)

        search(0,m-1)
        return flag
