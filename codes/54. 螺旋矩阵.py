from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path=[]
        m,n=len(matrix),len(matrix[0])
        dirs={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}


        i, j, index = 0, 0,0
        for _ in range(m*n):


            path.append(matrix[i][j])
            matrix[i][j]=""

            x,y=i+dirs[index][0],j+dirs[index][1]
            if (x<0 or x>=m or y<0 or y>=n) is True or matrix[x][y]=="":
                index=(index+1)%4

            i,j=i+dirs[index][0],j+dirs[index][1]

        return path[:]


