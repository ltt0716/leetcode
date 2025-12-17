from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m,n=len(matrix),len(matrix[0])

        i,j=1,m*n

        while i<=j:
            mid=(i+j)//2

            x=(mid-1)//n
            y=(mid-1)%n

            if matrix[x][y]==target:
                return True

            elif matrix[x][y]>target:
                j=mid-1
            else:
                i=mid+1
             
        return False