from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)

        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]

        for i in range(n):
            for j in range(i):
                matrix
        

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)

        
                 