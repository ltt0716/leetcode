class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])

        line=set()
        col=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    line.add(i)
                    col.add(j)
        
        for i in line:
            matrix[i]=[0]*n
        
        for j in col:
            for i in range(n):
                matrix[i][j]=0
                

        
