from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
        ans=[]
        m,n=len(matrix),len(matrix[0])
        i,j,index=0,0,0
        for _ in range(m*n):
            ans.append(matrix[i][j])
            matrix[i][j]=''

            x,y=i+dirs[index][0],j+dirs[index][1]
            if 0<=x<m and 0<=y<n and matrix[x][y]!='':
                i,j=x,y
            else:
                index=(index+1)%4
                i,j=i+dirs[index][0],j+dirs[index][1]


        return ans

