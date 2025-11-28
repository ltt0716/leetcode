from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans=False

        m,n=len(matrix),len(matrix[0])

        i,j=0,m*n-1
        while i<=j:
            mid=(i+j)//2

            row=mid//n
            col=mid%n

            if matrix[row][col]==target:
                ans=True
                break

            if matrix[row][col]>target:
                j=mid-1
            if matrix[row][col]<target:
                i=mid+1

        return ans
