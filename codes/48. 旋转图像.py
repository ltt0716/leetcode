from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        newmatrix=[[0 for i in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                newmatrix[j][n-1-i]=matrix[i][j]

        matrix[:]=newmatrix

