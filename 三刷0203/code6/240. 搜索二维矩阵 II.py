class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])

        def dfs(x,y):
            
            if x>=m or x<0 or y<0 or y>n:
                return False
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                return dfs(x,y-1)
            else:
                return dfs(x+1,y)
            
        return dfs(0,n-1)