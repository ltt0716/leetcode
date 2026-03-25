class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])

        ans=[]
        dir={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

        def dfs(x,y,key):
            ans.append(matrix[x,y])
            matrix[x,y]=''
            dx,dy=dir[key]

            while not ( 0<=dx+x<m and 0<=y+dy<n and matrix[dx+x][y+dy]!=''):
                key=(key+1)%4
                dx,dy=dir[key][0],dir[key][1]
            
            dfs(dx+x,y+dy,key)
        
        dfs(0,0,0)

        return ans

